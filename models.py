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

      


      