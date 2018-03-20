class Character():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def run(self, dx):
        print('character is running')
        self.x += dx
        
class Jumper(Character):
    def jump(self, dy):
        print('character is jumping')
        self.y += dy

class Talker(Character):
    def talk(self):
        print('I am talking to the screen')
        

person = Character()
person.run(2)
print(person.x, person.y)

jumpee = Jumper(3,4)
print(jumpee.x, jumpee.y)
jumpee.jump(4)
print(jumpee.x, jumpee.y)
jumpee.run(-1)
print(jumpee.x, jumpee.y)


talkee = Talker()
talkee.run(2)
talkee.talk()
print(talkee.x, talkee.y)




