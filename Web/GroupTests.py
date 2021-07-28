import unittest
from Signin import SigninCase
from Business import BusinessCase
from Workspaces import WorkspacesCase
from InviteUser import InvitesUserCase
from Teams import TeamsCase

# get all tests from SearchProductTest and HomePageTest class
Signin = unittest.TestLoader().loadTestsFromTestCase(SigninCase)
Business = unittest.TestLoader().loadTestsFromTestCase(BusinessCase)
Workspaces = unittest.TestLoader().loadTestsFromTestCase(WorkspacesCase)
InviteUser = unittest.TestLoader().loadTestsFromTestCase(InvitesUserCase)
Teams = unittest.TestLoader().loadTestsFromTestCase(TeamsCase)

# create a test suite combining search_test and home_page_test
GroupTests = unittest.TestSuite([Signin, Business, Workspaces, InviteUser, Teams])

# run the suite
unittest.TextTestRunner(verbosity=2).run(GroupTests)

