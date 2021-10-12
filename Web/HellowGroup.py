import unittest
from HellowTest import HellowTestCase
#from HellowWhile import HellowWhileCase

# get all tests from SearchProductTest and HomePageTest class
HellowTest = unittest.TestLoader().loadTestsFromTestCase(HellowTestCase)
#HellowWhile = unittest.TestLoader().loadTestsFromTestCase(HellowWhileCase)


# create a test suite combining search_test and home_page_test
HellowGroup = unittest.TestSuite([HellowTest])#, HellowWhile])

# run the suite
unittest.TextTestRunner(verbosity=2).run(HellowGroup)

