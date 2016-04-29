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
        self.open = True # False when a state is won or lost by Steve.
        self.steve_support = 0
        self.opponent_support = 0
        if self.gdp > 0:
            self.steve_support = self.gdp
        else:
            self.opponent_support = self.gdp * -1
        self.multiplier = 1
        self.trend = 0
        if ideology == 0:
            self.trend = 1
        else:
            self.trend = -1
        self.groud_operation_index = 0 # max is 5
        self.num_rally = 0 # max is 10
        self.num_community_outreach = 0 # max is 2
        self.num_fundraising = 0 # max is 1


    def update_support(self):
        'A function invoked after a move is made.'
        has_incident = random.randrange(0, 5)

        # Add support resulted from incident to steve's support.
        if has_incident == 0:
            self.steve_support += random.randrange(-5, 6)

        # Add support from trend to steve's support.
        if trend >= 0:
            self.steve_support += trend
        else:
            self.opponent_support += abs(trend)
               

    def hold_rally():
        'Change the status of state after a rally.'
        SUPPORT_GAINED = 1
        self.steve_support += SUPPORT_GAINED * abs(self.multiplier)
        self.rally += 1

    def hold_community_outreach():
        'Change the status of state after a community outreach.'
        self.community_outreach += 1
        self.steve_support += 2
        if self.num_community_outreach >= 2 and self.trend < 0:
            self.trend = abs(self.trend)

    def hold_fundraising():
        'Change the status of the state after a fundraising event.'
        self.num_fundraising += 1

    def can_hold_rally():
        'Checks if a rally is still doable.'
        return self.num_rally == 10

    def can_community_outreach():
        'Checks if a community outreach is still doable.'
        return self.num_community_outreach == 2

    def can_fundraise():
        'Checks if a fundraising event is still doable.'
        return self.num_fundraising == 1

    def can_ground():
        'Checks if it is still possible to consolidate ground operation.'
        return self.ground_operation_index == 5
        
    
            
        
        
            


    
