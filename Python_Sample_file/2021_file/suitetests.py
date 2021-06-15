import unittest
from eeaddcourse import eeaddcourseCase
from eesignup import eesignupCase
from eesignin import eesigninCase

# get all tests from SearchProductTest and HomePageTest class
eeaddcourse = unittest.TestLoader().loadTestsFromTestCase(eeaddcourseCase)
eesignup = unittest.TestLoader().loadTestsFromTestCase(eesignupCase)
eesignin = unittest.TestLoader().loadTestsFromTestCase(eesigninCase)

# create a test suite combining search_test and home_page_test
suitetests = unittest.TestSuite([eeaddcourse, eesignup, eesignin])
# run the suite
unittest.TextTestRunner(verbosity=2).run(suitetests)