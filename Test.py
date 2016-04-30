from StateObject import State


def test():
    state1 = State("Washington", 1)
    state1.hold_rally();
    state1.hold_community_outreach()
    state1.hold_fundraising()
    state1.update_support()
    state1.bribe_voters()
    print(state1.evaluate())
test()


