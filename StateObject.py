class State:
  def __init__(self, name, elector_count, gdp_growth, idealogy, incidents):
    # constants
    self.name = name
    self.elector_count = electors_count
    self.gdp_growth = gdp_growth
    self.idealogy = self.idealogy
    self.incidents = incidents
    
    # variables
    self.open = True
    self.steve_support = 0
    self.opponent_support = 0
    if gdp_growth > 0:
      steve_support = gdp_growth
    else:
      opponent_support = gdp_growth * -1
    self.multiplier = 1
    self.groud_operation_index = 0 # max is 5
    self.community_outreach_event = 0 # max is 2
    self.local_fundraising = 0 # max is 1
    
