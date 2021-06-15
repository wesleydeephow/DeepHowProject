import unittest
from HellowTest import HellowTestCase

# get all tests from SearchProductTest and HomePageTest class
HellowTest = unittest.TestLoader().loadTestsFromTestCase(HellowTestCase)


# create a test suite combining search_test and home_page_test
GroupTests = unittest.TestSuite([HellowTest])
# run the suite
unittest.TextTestRunner(verbosity=2).run(GroupTests)

print()