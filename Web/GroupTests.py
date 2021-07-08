import unittest
from HellowTest import HellowTestCase
from Signin import SigninCase
from Business import BusinessCase

# get all tests from SearchProductTest and HomePageTest class
HellowTest = unittest.TestLoader().loadTestsFromTestCase(HellowTestCase)
Signin = unittest.TestLoader().loadTestsFromTestCase(SigninCase)
Business = unittest.TestLoader().loadTestsFromTestCase(BusinessCase)

# create a test suite combining search_test and home_page_test
GroupTests = unittest.TestSuite([HellowTest, Signin, Business])
# run the suite
unittest.TextTestRunner(verbosity=2).run(GroupTests)

