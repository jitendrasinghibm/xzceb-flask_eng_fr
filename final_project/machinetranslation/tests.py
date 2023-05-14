"""
Unit tests for IBM Watson Language Translator
"""
import unittest
from translator import french_to_english, english_to_french

class TestLanguageTranslator(unittest.TestCase):
    """
    Test cases for translator functions
    """
    def test_french_to_english_ae(self):
        """
        Test case for Fremch To English function: Assert Equal
        """
        french_text= 'Bonjour, comment allez-vous?'
        res = french_to_english(french_text)
        self.assertEqual(res['translations'][0]['translation'], 'Hello, how are you?')

    def test_french_to_english_ane(self):
        """
        Test case for Fremch To English function:Assert Not Equal
        """
        french_text= 'Bonjour, comment allez-vous?'
        res = french_to_english(french_text)
        self.assertNotEqual(res['translations'][0]['translation'], 'Bonjour, comment allez-vous?')

    def test_english_to_french_ae(self):
        """
        Test case for English to French function: Assert Equal
        """
        eng_text= 'Hello, how are you?'
        res = english_to_french(eng_text)
        self.assertEqual(res['translations'][0]['translation'], 'Bonjour, comment allez-vous?')
    
    def test_english_to_french_ane(self):
        """
        Test case for English to French function: Assert Not Equal
        """
        eng_text= 'Hello, how are you?'
        res = english_to_french(eng_text)
        self.assertNotEqual(res['translations'][0]['translation'], 'Hello, how are you?')

if __name__ == '__main__':
    unittest.main()
