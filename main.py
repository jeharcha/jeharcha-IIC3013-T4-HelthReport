from pandas.core.frame import DataFrame
import requests
from requests.models import Response
from parameters import URL, country_codes, indicators_wanted_v2
from models import Country
import gspread
from gspread_dataframe import set_with_dataframe
import xml.etree.ElementTree as ET
import pandas as pd
import json


def init_country_objects(country_codes):
  countries = {}
  for code in country_codes:
    countries[code[0]] = Country(code[0], code[1])
  return countries

def get_url_by_country(base_url, country_code):
  return base_url + "/gho_" + country_code + ".xml"

def get_and_write_xml_by_country():
  countries = init_country_objects(country_codes)
  for country_code in countries.keys():
    country_url = get_url_by_country(base_url=URL, country_code=country_code )
    countries[country_code].url = country_url
    print("country_URL: " + countries[country_code].url+ "\n")  
    response = requests.get(countries[country_code].url)
    # xml_path_name = './xml_files/' + countries[country_code].name + '.xml'
    # with open(xml_path_name, 'wb') as f:
    #     f.write(response.content)
    countries[country_code].response = response    
  return countries;
     
def create_df(countries, indicators_wanted):
  all_countries_df = pd.DataFrame(data=None)
  for country_code in countries.keys():
    print(country_code)
    countries[country_code].etree = ET.fromstring(countries[country_code].response.content)
    gho_set = {None}
    for node in countries[country_code].etree:
      indicator = node.find("GHO").text if node.find("GHO") is not None else None
      gho_set.add(indicator)
      if indicator in indicators_wanted: 
        country = node.find("COUNTRY").text if node.find("COUNTRY") is not None else None
        sex = node.find("SEX").text if node.find("SEX") is not None else None
        ghecauses = node.find("GHECAUSES").text if node.find("GHECAUSES") is not None else None
        age_group = node.find("AGEGROUP").text if node.find("AGEGROUP") is not None else None
        year = node.find("YEAR").text if node.find("YEAR") is not None else None
        numeric = node.find("Numeric").text if node.find("Numeric") is not None else None
        display = node.find("Display").text if node.find("Display") is not None else None
        low = node.find("Low").text if node.find("Low") is not None else None        
        high = node.find("High").text if node.find("High") is not None else None

        countries[country_code].nodes_data["GHO"].append(indicator)
        countries[country_code].nodes_data["COUNTRY"].append(country)
        countries[country_code].nodes_data["COUNTRY_CODE"].append(country_code)
        countries[country_code].nodes_data["SEX"].append(sex)
        countries[country_code].nodes_data["GHECAUSES"].append(ghecauses)
        countries[country_code].nodes_data["AGEGROUP"].append(age_group)
        countries[country_code].nodes_data["YEAR"].append(year)
        countries[country_code].nodes_data["Numeric"].append(numeric)
        countries[country_code].nodes_data["Display"].append(display)
        countries[country_code].nodes_data["Low"].append(low)
        countries[country_code].nodes_data["High"].append(high)
    
    countries[country_code].df = pd.DataFrame(data=countries[country_code].nodes_data)
    all_countries_df = all_countries_df.append(countries[country_code].df)
  return all_countries_df
  

def dict_to_txt(dict_input):
  gho_str =  "GHO_DICT = "         
  gho_str += json.dumps(dict_input)
  with open("gho_dict.txt", 'w') as f:
      f.write(gho_str)
    

def open_df_in_spreadsheets(df):

  # Access Google Sheet
  gc = gspread.service_account(filename="helthreportsfromwho-cb747e651db1.json")
  sh = gc.open_by_key("1v1ADDrxvLpQ0ZVtaagcYNT--Ik3lu7pEmIpdfJCUEQQ")
  worksheet = sh.get_worksheet(0)
  worksheet.clear()
  
  # Append Data to Sheet
  set_with_dataframe(worksheet, df)
  return True

if __name__ == "__main__": 
  countries = get_and_write_xml_by_country()
  the_df = create_df(countries, indicators_wanted_v2)
  open_df_in_spreadsheets(the_df)
  print("finished")

