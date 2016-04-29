import random

class State:
    def __init__(self, name, elector_count):
        # constants
        self.name = name
        self.elector_count = elector_count
        self.gdp = random.randrange(-15, 16)
        self.idealogy = random.randrange(0, 2)
        self.has_incident = random.randrange(0, 5)
        self.incident_type = random.randrange(-5, 5)
        
        # variables
        self.open = True
        self.steve_support = 0
        self.opponent_support = 0
        if self.gdp > 0:
          steve_support = self.gdp
        else:
          opponent_support = self.gdp * -1
        self.multiplier = 1
        self.groud_operation_index = 0 # max is 5
        self.community_outreach_event = 0 # max is 2
        self.local_fundraising = 0 # max is 1


    def update_support(self):
        has_incident = random.randrange(0, 5)
        if has_incident == 0:
            self.steve_support += random.randrange(-5, 6)
        print('Update_support worked!')
            


    
