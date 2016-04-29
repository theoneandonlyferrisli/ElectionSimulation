import random

class State:
    def __init__(self, name, elector_count):
        # constants
        self.name = name
        self.elector_count = elector_count

        # Randomly generated from -15 to 15,
        # which will later be added to steve_support
        self.gdp = random.randrange(-15, 16)

        # Ideology 0 = liberal and 1 = conservative
        self.idealogy = random.randrange(0, 2)
        
        # variables
        self.open = True
        self.steve_support = 0
        self.opponent_support = 0
        if self.gdp > 0:
            self.steve_support = self.gdp
        else:
            self.opponent_support = self.gdp * -1
        self.multiplier = 1
        self.groud_operation_index = 0 # max is 5
        self.community_outreach_event = 0 # max is 2
        self.local_fundraising = 0 # max is 1


    def update_support(self):
        'A function invoked after a move is made.'
        has_incident = random.randrange(0, 5)
        if has_incident == 0:
            self.steve_support += random.randrange(-5, 6)
        print('Update_support worked!')
            


    
