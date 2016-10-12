
class Character:
    '''
    Base Character Class which creates all Players & NPCs

    '''

    def __init__(self, name):
        self.name = name
        self.attributes = {'WS' : 0, 'BS' : 0, 'S' : 0, 'T' :0, 'AG' : 0, 'INT' : 0, 'PER' : 0, 'WP' : 0, 'FEL' : 0}
        self.rank = 0
        self.wounds = 1
        self.fate = 0
        self.experience = 0
        self.renown = 0
        self.talents_traits = dict() # empty dicts equivalent too '== {}'
        self.psychic = dict()
        self.armour = {'Head' : 0, 'Chest' : 0, 'L Arm' : 0, 'R Arm' : 0, 'L Leg' : 0, 'R Leg' : 0}
        self.weapons = dict()



