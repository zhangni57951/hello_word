class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_role(a):
        print('%s:%s ' % (a.name, a.hp))
    def sum(self):
       self.hp+=1
       print('%s:%s ' % (self.name, self.hp))


user1 = Player('Tom', 100)
user2 = Player('jerry', 80)
user1.print_role()
user2.print_role()
user1.sum()
user2.sum()
