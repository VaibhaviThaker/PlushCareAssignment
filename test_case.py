import unittest
from encrypt_decrypt import encrypt, decrypt


class TestEncryptionDecryption(unittest.TestCase):

    def __init__(self, testName, extraArgs):
        super(TestEncryptionDecryption, self).__init__(testName)
        self.input_message = extraArgs[0]
        self.output_message = extraArgs[1]

    def setUp(self):
        self.encrypt_codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

    def test_encrypt(self):
        self.assertEqual(encrypt(self.input_message, self.encrypt_codes), self.output_message, "Encryption failed")

    def test_decrypt(self):
        self.assertEqual(decrypt(self.input_message, self.encrypt_codes), self.output_message, "Decryption failed")

    def tearDown(self):
        self.encrypt_codes = None
        self.input_message = None
        self.output_message = None
