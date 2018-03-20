from libdw import sm
class CM(sm.SM):
    start_state = 0

    def get_next_values(self,state, inp):
        if state == 0 and inp == 50:
            nextstate = 1
            output = (50, '--', 0)
        elif state == 1 and inp == 50:
            nextstate = 0
            output = (0, 'coke', 0)
        elif state == 1 and inp == 100:
            nextstate = 0
            output = (0, "coke", 50)
        elif state == 0 and inp == 100:
            nextstate = 0
            output = (0, "coke", 0)
        else:
            nextstate = state
            if state ==  1:
                blalance = 50
                output = (balance, '--', inp)
            else:
                balance = 0
                output = (balance, '--', inp)
        return nextstate, output
    
c = CM()
c.start()
print(c.step(50))
print(c.step(50))
print(c.step(200))


    
    