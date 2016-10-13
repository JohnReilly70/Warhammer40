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
        self.assertEqual(player.armour['Head'], 0)
        self.assertEqual(player.armour['Chest'], 0)
        self.assertEqual(player.armour['L Arm'], 0)
        self.assertEqual(player.armour['R Arm'], 0)
        self.assertEqual(player.armour['L Leg'], 0)
        self.assertEqual(player.armour['R Leg'], 0)

    def test_Weapon_Dict(self):
        # Check an empty Dict is started for Weapon
        player = Character_Classes.Character("John")
        self.assertFalse(player.weapons)

    def test_Add_Weapon(self):
        player = Character_Classes.Character("John")
        # Weapons SHould Have Name/Class/Dmg/Pen/Special/Weight/Requistion/MinRenown
        player.Add_Weapon("Astartes Chainsword", "Melee", "1d10+3 R", 4, "Balanced, Tearing", 10, 5, 0)
        player.Add_Weapon("Astartes ChainFist", "Melee", "3d10+3 R", 7, "Tearing", 10, 5, 2)
        self.assertEqual(player.weapons['Astartes Chainsword'], ['Melee', '1d10+3 R', 4, 'Balanced, Tearing', 10, 5, 0])
        self.assertEqual(player.weapons['Astartes ChainFist'], ["Melee", "3d10+3 R", 7, "Tearing", 10, 5, 2])

    def test_Add_Weapon_Insufficent_Info(self):
        player = Character_Classes.Character("John")
        player.Add_Weapon("Astartes Bolter", "Melee", "3d10+3 R", 7, "Tearing")
        self.assertEqual(player.weapons['Astartes Bolter'], "KeyError: 'Astartes Bolter'") #Cannot Get to Work, Tired AssertRaises. Look into more.

if __name__ == '__main__':
    unittest.main()
