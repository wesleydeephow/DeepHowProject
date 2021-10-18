import unittest
#from HellowWhile import HellowWhileCase
from HellowTest import HellowTestCase


# get all tests from SearchProductTest and HomePageTest class
#HellowWhile = unittest.TestLoader().loadTestsFromTestCase(HellowWhileCase)
HellowTest = unittest.TestLoader().loadTestsFromTestCase(HellowTestCase)



# create a test suite combining search_test and home_page_test
#HellowGroup = unittest.TestSuite([HellowWhile, HellowTest])
HellowGroup = unittest.TestSuite([HellowTest])

# run the suite
unittest.TextTestRunner(verbosity=2).run(HellowGroup)

