from libdw import sm

class CommentsSM(sm.SM):
    start_state = 'out'

    def get_next_values(self, state, inp):
        if state == 'out':
            if inp == '#':
                return ('inside', inp)
            else:
                return ('out', None)
            
        else:
            if inp == '\n':
                return ('out', None)
            else:
                return ('inside', inp)
            

com = CommentsSM()

s = '’ def f ( x ) : # comment \n return 1'

print(com.transduce(s))