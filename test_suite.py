import unittest


def suite():
    """
     Added test cases to test suites that will verify the tests mentioned in the TestEncryptionDecryption
     It will only run the tests that are added to the suit
    :return: TestSuite
    """
    suites = unittest.TestSuite()
    from test_case import TestEncryptionDecryption
    suites.addTest(TestEncryptionDecryption('test_encrypt', ["another message here!", "1n4th2r m2ss1g2 h2r2!"]))
    suites.addTest(TestEncryptionDecryption('test_decrypt', ["th3s 3s 1 m2ss1g2.", "this is a message."]))
    return suites


if __name__ == '__main__':
    """
        - executed the test suite
    """
    runner = unittest.TextTestRunner()
    runner.run(suite())