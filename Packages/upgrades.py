class upgrades:
    '''Class to upgrade attack and defense system'''
    def __init__(self,x,y,file):
        base_dir = 'images\\upgrades\\'
        super().__init__(x, y, file, base_dir)
        self.damage = 0
        self.defence = 0
        self.health = 0
        self.file = file
    def attack_damage(self,damage,cost):
        global damage
        damage += damage/10
        cost += cost / 3
    def max_health(self,health,cost):
        global health
        health += health/4
        cost += cost / 3
    def shield(self,defence,cost):
        global defence
        import random
        x=50
        y=250
        shld = random.randint(x,y)
        defence += health + shld
        x += 25
        y += 25
        cost += cost / 3
