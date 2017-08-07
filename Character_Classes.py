class Character:
    '''
    Base Character Class which creates all Players & NPCs
    '''

    def __init__(self, name):
        self.name = name
        self.attributes = dict(WS=0, BS=0, S=0, T=0, AG=0, INT=0, PER=0, WP=0, FEL=0)
        self.rank = 0
        self.wounds = 1
        self.fate = 0
        self.experience = 0
        self.renown = 0
        self.talents_traits = dict()  # Empty dicts equivalent too '== {}'
        self.psychic = dict()
        # Ratings Values going left to right should be 'Head' : 0, 'Chest' : 0, 'L Arm' : 0, 'R Arm' : 0, 'L Leg' : 0, 'R Leg' : 0
        self.armour = {'Rating': [], 'Info': {'Name': '', 'Weight': 0, 'Req': 0, 'Renown': 0}}
        self.weapons = {'Melee': {}, 'Ranged': {}}

    def Add_Weapon(self, *args):
        '''
        Add Weapons to the Character Weapons Dict.
        Doesn't Matter If not all info is provided
        '''
        if len(args) >= 2:
            if args[1] == 'Melee':
                self.weapons['Melee'][args[0]] = list(args[1:])
            else:
                self.weapons['Ranged'][args[0]] = list(args[1:])
        else:
            print(
                "\nFailed to Enter Correct Weapon Data\n\nWords in same column should be kept together ie \"Tearing, Balanced\"")

    def Remove_Weapon(self, Weapon_Name):
        '''
        Check If the weapon they have named is in either Melee or Ranged Dicts of the weapon Dict
        Else Print the name does not have that weapon
        '''
        if Weapon_Name in self.weapons['Melee']:
            del self.weapons['Melee'][Weapon_Name]
        elif Weapon_Name in self.weapons['Ranged']:
            del self.weapons['Ranged'][Weapon_Name]
        else:
            print("\n{} does not have that in his armoury.".format(self.name))

    def Show_Inventory(self, Inv_Type=''):
        '''
        Shows All Inventory if Method receives no args or incorrectly spelled arg
        '''
        if Inv_Type == 'Melee':
            print("{}\n".format(self.weapons['Melee']))
            return True
        elif Inv_Type == 'Ranged':
            print("{}\n".format(self.weapons['Ranged']))
            return True
        else:
            print("{}\n".format(self.weapons))
            return True
        # If this IF statement fails it should return False. Should NEVER return False
        return False

    def Add_And_Replace_Armour(self, Armour_Search_Name):
        import sqlite3
        try:
            db_conn = sqlite3.connect('Armoury.db')
            cursor = db_conn.cursor()
            cursor.execute("SELECT * FROM Armoury WHERE NAME == '{}'".format(Armour_Search_Name))
        except sqlite3.OperationalError:
            print("Cannot Find Database")

        Armour = cursor.fetchone()

        self.armour['Info']['Name'] = Armour[0]
        self.armour['Rating'] = Armour[2]

        # Add lines to complete the addition info such as Req Renown Weight ETC

    def Search_Armour(self, Armour_Search_Name):
        import sqlite3
        try:
            db_conn = sqlite3.connect('Armoury.db')
            cursor = db_conn.cursor()
            if Armour_Search_Name != "":
                cursor.execute("SELECT * FROM Armoury WHERE NAME == '{}'".format(Armour_Search_Name))
            else:
                cursor.execute("SELECT * FROM Armoury")

        except sqlite3.OperationalError:
            print("Cannot Find Database")


        if not cursor.fetchone():
            return "No Such Item name in Database"
        else:
            for Armour in cursor:
                print(Armour)