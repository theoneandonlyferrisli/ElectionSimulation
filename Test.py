from StateObject import State


def test():
    state1 = State("Washington", 1)
    print(state1.name)
    print(state1.steve_support)
    print(state1.opponent_support)
    state1.update_support()
test()
