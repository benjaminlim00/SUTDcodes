from libdw import sm

class FirstWordSM(sm.SM):
    start_state = 'before'

    def get_next_values(self, state, inp):
        if state == 'before':
            if inp == ' ' or inp == '\n':
                return ('before', None)
            else:
                return ('inside', inp)
            
        elif state == 'inside':
            if inp == '\n':
                return ('before', None)
            elif inp == ' ':
                return ('after', None)
            else:
                return ('inside', inp)
        else:
            if inp == '\n':
                return('before', None)
            else:
                return('after', None)
            

com = FirstWordSM()

s = 'def f(x): # comment \n return 1'

print(com.transduce(s))