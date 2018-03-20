from libdw import sm

class SimpleAccount(sm.SM):
    
    def __init__(self, start_deposit):
        self.start_state = start_deposit

    def get_next_values(self, state, inp):
        if inp < 0 and state < 100:
            nextstate = state + inp - 5
        else:
            nextstate = state + inp
            
        output = nextstate
        return nextstate, output