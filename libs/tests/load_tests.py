from unit_tests_structure import TestStructureMethods
from unit_tests_api import TestAPIMethods
from unittest import TestSuite


test_cases = (TestStructureMethods, TestAPIMethods)

def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
