import unittest
from fastname import OpenTest
from easysignin import EasySign
from NewDirectory import NewDirectory1
# get all tests from SearchProductTest and HomePageTest class
fastname = unittest.TestLoader().loadTestsFromTestCase(OpenTest)
easysignin = unittest.TestLoader().loadTestsFromTestCase(EasySign)
NewDirectory = unittest.TestLoader().loadTestsFromTestCase(NewDirectory1)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([fastname, easysignin, NewDirectory])
# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)