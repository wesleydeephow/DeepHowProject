import unittest
from Signin import SigninCase
from Business import BusinessCase
from Workspaces import WorkspacesCase
from InviteUser import InvitesUserCase

# get all tests from SearchProductTest and HomePageTest class
Signin = unittest.TestLoader().loadTestsFromTestCase(SigninCase)
Business = unittest.TestLoader().loadTestsFromTestCase(BusinessCase)
Workspaces = unittest.TestLoader().loadTestsFromTestCase(WorkspacesCase)
InviteUser = unittest.TestLoader().loadTestsFromTestCase(InvitesUserCase)

# create a test suite combining search_test and home_page_test
GroupTests = unittest.TestSuite([Signin, Business, Workspaces, InviteUser])

# run the suite
unittest.TextTestRunner(verbosity=2).run(GroupTests)

