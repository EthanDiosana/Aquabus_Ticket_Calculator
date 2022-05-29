import unittest

from .. import Route_Container

class Test_Routes_Loaded(unittest.TestCase):
    """Tests that all of the Routes on the price list have loaded."""

    def setUp(self):
        """This sets up the Routes before each question."""
        self.All_Routes = All_Routes

    def test_hornby_granville_exists(self):
        self.assertEqual(All_Routes.routeIsInContainer("HORNBY", "GRANVILLE"),True)