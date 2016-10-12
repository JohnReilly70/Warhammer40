import Character_Classes
import unittest

class Test_Class_Creation(unittest.TestCase):
    '''

    '''

    def Test_Creating_Character_With_Name(self):
        player = Character_Classes.Character("John")
        #Check if it has the correct name
        self.assertEqual(player.name, "John")
        #Check if the name i not empty
        self.assertNotEqual("", player.name)

    def Test_Atrributes_Created_Empty(self):
        player = Character_Classes.Character("John")
        #Check attributes is not an empty dict/list
        self.assertTrue(player.attributes)
        #Check attributes WS is 0
        self.assertEqual(player.attributes['WS'], 0)

    def Test_Preset_Stats(self):
        #Check Stats are all set up at minimum value
        player = Character_Classes.Character("John")
        self.assertEqual(player.rank, 0)
        self.assertEqual(player.wounds, 1)
        self.assertEqual(player.fate, 0)
        self.assertEqual(player.experience, 0)
        self.assertEqual(player.renown, 0)
        self.assertIsInstance(player.talents_traits, dict)
        self.assertIsInstance(player.psychic, dict)

    def Test_Armour_Dict(self):
        #Check Armour Values are a Dict with 0 as initial
        player = Character_Classes.Character("John")
        self.assertEqual(player.armour['Head'], 0)
        self.assertEqual(player.armour['Chest'], 0)
        self.assertEqual(player.armour['L Arm'], 0)
        self.assertEqual(player.armour['R Arm'], 0)
        self.assertEqual(player.armour['L Leg'], 0)
        self.assertEqual(player.armour['R Leg'], 0)

    def Test_Weapon_Dict(self):
        #Check an empty Dict is started for Weapon
        player = Character_Classes.Character("John")
        self.assertFalse(player.weapons)

if __name__ == '__main__':
    unittest.main()


