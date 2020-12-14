import unittest
from friend_ships.friend_ships import FriendShips


class TestFriendShips(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShips()

    def test_make_friends(self):
        friend1 = 'abc'
        friend2 = 'abc2'
        self.temp.make_friends(friend1, friend2)
        self.assertEqual(self.temp.dict, {'abc': ['abc2'], 'abc2': ['abc']})

    def test_make_friends_exception(self):
        friend1 = 2
        friend2 = 'abc2'
        self.assertRaises(TypeError, self.temp.make_friends, friend1, friend2)

    def test_are_friends(self):
        friend1 = 'abc'
        friend2 = 'abc2'
        self.temp.make_friends(friend1, friend2)
        self.assertTrue(self.temp.are_friends(friend1, friend2))

    def test_get_friends_list(self):
        friend1 = 'abc'
        friend2 = 'abc2'
        friend3 = 'abc3'
        self.temp.make_friends(friend1, friend2)
        self.temp.make_friends(friend1, friend3)
        self.assertEqual(self.temp.get_friends_list(friend1), [friend2,
                                                               friend3])

    def test_add_friend(self):
        friend1 = 'abc'
        friend2 = 'abc2'
        self.temp.add_friend(friend1, friend2)
        self.assertEqual(self.temp.dict, {'abc': ['abc2']})

    def tearDown(self):
        self.temp = None