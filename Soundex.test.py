import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), '')

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("p"), "P000")
        self.assertEqual(generate_soundex("W"), "W000")
        self.assertEqual(generate_soundex("L"), "L000")
        self.assertEqual(generate_soundex("M"), "M000")
        self.assertEqual(generate_soundex("R"), "R000")
        
    def test_start_with_invalid_char(self):
        self.assertEqual(generate_soundex("!pari"), "P600")
        self.assertEqual(generate_soundex("132pari"), "P600")
        self.assertEqual(generate_soundex("  pari"), "P600")
        self.assertEqual(generate_soundex(" - pari"), "P600")
    
    # To test the inputs with only invalid characters 
    def test_invaild_only_input(self):
        self.assertEqual(generate_soundex("!=0234/"), "0000")
        self.assertEqual(generate_soundex("1"), "0000")
        self.assertEqual(generate_soundex("   "), "0000")

    def test_handel_consecutive_duplicte_char(self):
        self.assertEqual(generate_soundex("WWWWW"), "W000")
        self.assertEqual(generate_soundex("PAAWWW"), "P000")
        self.assertEqual(generate_soundex("RRRpari"), "R160")
    
    # to keep the length soundex to 4 irreseptive of any inupt expect NULL 
    def test_size_of_sondex(self):
        self.assertEqual(generate_soundex("      pr"), "P600")
        self.assertEqual(generate_soundex("w e lll d o one "), "W435")
        self.assertEqual(generate_soundex("GG"), "G000")
        self.assertEqual(generate_soundex("AEIOUWHY"), "A000")

    
if __name__ == '__main__':
    unittest.main()
