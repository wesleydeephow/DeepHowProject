import unittest
from HellowTest import HellowTestCase
from Signin import SigninCase

# get all tests from SearchProductTest and HomePageTest class
HellowTest = unittest.TestLoader().loadTestsFromTestCase(HellowTestCase)
Signin = unittest.TestLoader().loadTestsFromTestCase(SigninCase)

# create a test suite combining search_test and home_page_test
GroupTests = unittest.TestSuite([HellowTest, Signin])
# run the suite
unittest.TextTestRunner(verbosity=2).run(GroupTests)

