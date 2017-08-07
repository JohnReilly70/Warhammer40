import unittest
import Character_Classes


class Test_Class_Creation(unittest.TestCase):


    def test_Creating_Character_With_Name(self):
        player = Character_Classes.Character("John")
        # Check if it has the correct name
        self.assertEqual(player.name, "John")
        # Check if the name is not empty
        self.assertNotEqual("", player.name)

    def test_Atrributes_Created_Empty(self):
        player = Character_Classes.Character("John")
        # Check attributes is not an empty dict/list
        self.assertTrue(player.attributes)
        # Check attributes WS is 0
        self.assertEqual(player.attributes['WS'], 0)

    def test_Preset_Stats(self):
        # Check Stats are all set up at minimum value
        player = Character_Classes.Character("John")

        self.assertEqual(player.rank, 0)
        self.assertEqual(player.wounds, 1)
        self.assertEqual(player.fate, 0)
        self.assertEqual(player.experience, 0)
        self.assertEqual(player.renown, 0)
        self.assertIsInstance(player.talents_traits, dict)
        self.assertIsInstance(player.psychic, dict)

    def test_Armour_Dict(self):
        # Check Armour Values are a Dict with 0 as initial
        player = Character_Classes.Character("John")

        for index, Armour_Piece in enumerate(player.armour['Rating']):
            self.assertEqual(player.armour['Rating'][index], 0)


    def test_Weapon_Dict(self):
        # Check an empty Dict is started for Weapon
        player = Character_Classes.Character("John")

        self.assertFalse(player.weapons['Melee'])
        self.assertFalse(player.weapons['Ranged'])

    def test_Add_Weapon(self):
        player = Character_Classes.Character("John")
        # Weapons SHould Have Name/Class/Dmg/Pen/Special/Weight/Requistion/MinRenown
        player.Add_Weapon("Astartes Chainsword", "Melee", "1d10+3 R", 4, "Balanced, Tearing", 10, 5, 0)
        player.Add_Weapon("Astartes ChainFist", "Melee", "3d10+3 R", 7, "Tearing", 10, 5, 2)

        self.assertEqual(player.weapons['Melee']['Astartes Chainsword'], ['Melee', '1d10+3 R', 4, 'Balanced, Tearing', 10, 5, 0])
        self.assertEqual(player.weapons['Melee']['Astartes ChainFist'], ["Melee", "3d10+3 R", 7, "Tearing", 10, 5, 2])

    def test_Add_Weapon_Insufficent_Info(self):
        # Will not add a weapon if all the info is not there. (Min Info as per Table 5-5 / 5-8 DeathWatch Core RuleBook)
        player = Character_Classes.Character("John")

        self.assertFalse(player.Add_Weapon("Astartes Bolter", "Melee", "3d10+3 R", 7, "Tearing"))

    def test_Remove_Weapon(self):
        # Removes Weapon if Weapon name is correct (Only info required to remove a weapon)
        player = Character_Classes.Character("John")
        player.Add_Weapon("Astartes Chainsword", "Melee", "1d10+3 R", 4, "Balanced, Tearing", 10, 5, 0)
        player.Remove_Weapon("Astartes Chainsword")

        self.assertFalse(player.weapons['Melee'])

    def test_Remove_Weapon_Not_In_Inventory(self):
        # Returns a message stating that weapon name is not in inventory (self.weapons)
        player = Character_Classes.Character("John")
        player.Remove_Weapon("Astartes Chainsword")

        self.assertFalse(player.weapons['Melee'])

    def test_Show_Inventory(self):
        player = Character_Classes.Character("John")
        player.Add_Weapon("Astartes Chainsword", "Melee", "1d10+3 R", 4, "Balanced, Tearing", 10, 5, 0)
        player.Add_Weapon("Astartes Bullet", "Bullet", "1d10+3 R", 4, "Balanced, Tearing", 10, 5, 0)

        print("All Inventory:\n")
        self.assertTrue(player.Show_Inventory())
        print("Melee Inventory:\n")
        self.assertTrue(player.Show_Inventory("Melee"))
        print("Ranged Inventory:\n")
        self.assertTrue(player.Show_Inventory("Ranged"))

    def test_Add_Armour_without_Addition_Info(self):
        player = Character_Classes.Character("John")
        player.Add_And_Replace_Armour("Astartes Power Armour")

        self.assertEqual(player.armour['Info']['Name'], 'Astartes Power Armour')
        self.assertEqual(player.armour['Rating'], '8,10,10,10,10,10')

    def test_Armour_Database_Search_Pass(self):

        player = Character_Classes.Character("John")
        self.assertEqual(player.Search_Armour('Astartes Power Armour'), ('Astartes Power Armour', 'All', '8,10,10,10,10,10', 0, '-'))

    def test_Armour_Database_Search_Fail(self):
        player = Character_Classes.Character("John")
        self.assertEqual(player.Search_Armour('Power Armour'), "No Such Item name in Database")



if __name__ == '__main__':
    unittest.main()
