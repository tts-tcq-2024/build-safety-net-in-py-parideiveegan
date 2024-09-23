import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def ReturnsEmptyStringForEmptyString(self):
        self.assertEqual(generate_soundex(""), '')

    def RetrunsSodexcodeSingleCharacterInput(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("p"), "P000")
        self.assertEqual(generate_soundex("W"), "W000")
        self.assertEqual(generate_soundex("L"), "L000")
        self.assertEqual(generate_soundex("M"), "M000")
        self.assertEqual(generate_soundex("R"), "R000")
        
    def RetrunsSoundexCodeRemovingInvalidCharInInput(self):
        self.assertEqual(generate_soundex("!pari"), "P600")
        self.assertEqual(generate_soundex("132pari"), "P600")
        self.assertEqual(generate_soundex("  pari"), "P600")
        self.assertEqual(generate_soundex(" - pari"), "P600")
    
    # To test the inputs with only invalid characters 
    def ReturnsaZeroPaddedforAllCharAsInvalidInInput(self):
        self.assertEqual(generate_soundex("!=0234/"), "0000")
        self.assertEqual(generate_soundex("1"), "0000")
        self.assertEqual(generate_soundex("   "), "0000")

    def RetursSondexCodeRemovingVowelsInInput(self):
        self.assertEqual(generate_soundex("WWWWW"), "W000")
        self.assertEqual(generate_soundex("PAAWWW"), "P000")
        
    def ReturnsSoundexCodeFirstCharReservedForVowelasFirstChar(self):
        self.assertEqual(generate_soundex("RRRpari"), "R160")
        
    def ReturnsSoundexCodeIgnoringReptedLettersInInput(self):
        self.assertEqual(generate_soundex("Butter"), "B360")
        
    def ReturnsSoundexCodeIgnoringCosecutivelettersSepratedByHWYInInput(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        
    def ReturnsSoundexCodeReservingCosecutivelettersSepratedByVowelsInInput(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")
        
    def ReturnsSoundexCodeLimitingCodeLengthToFourByPaddingZeroOrTruncating(self):
        self.assertEqual(generate_soundex("All"), "A400")
        
    def ReturnsSoundexCodeKeppingTheFirstLetterSameAsInTheInput(self):
        self.assertEqual(generate_soundex("Pari"), "P600")
    
if __name__ == '__main__':
    unittest.main()
