class Country:
  def __init__(self, code, name):
      self.code = code
      self.name = name
      self.url = ""
      self.response = None
      self.etree = None
      self.df = None
      self.nodes_data = {
        "GHO": [],
        "COUNTRY": [],
        "COUNTRY_CODE": [],
        "SEX": [],
        "GHECAUSES": [],
        "AGEGROUP": [],
        "YEAR": [],
        "Numeric": [],
        "Display": [],
        "Low": [],
        "High": []
      }


class DeathData:
  def __init__(self):
      self.total_number = None
      self.infant_number = None
      self.under_five_number = None
      self.kids_mortality_rate = None
      self.adult_mortality_rate = None
      self.homicides_number = None
      self.suicide_rates = None
      self.poisoning_rates = None
      self.sex_disease_number = None
      self.road_traffic_rate = None
      self.road_traffic_number = None

class WeightData:
  def __init__ (self):
    self.mean_bmi = None
    self.mean_bmi_aged = None
    self.adult_obesity_percentage = None
    self.young_obesity_percentage = None
    self.adult_overweight_percentage = None
    self.young_overweight_percentage = None
    self.adult_underweight_percentage = None
    self.young_underweight_percentage = None
    
class HealthData:
  def __init__(self):
      self.alcohol_litres_per_capita = None
      self.daily_cigar_percentage = None
      self.daily_tabacco_percentage = None
      self.current_cigar_percentage = None
      self.current_tabacco_percentage = None
      self.mean_blood_preassure = None
      self.mean_blood_glucose = None
      self.mean_total_cholesterol = None
      


      