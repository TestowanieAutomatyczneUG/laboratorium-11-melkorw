import unittest
from unittest.mock import MagicMock
from friend_ships_storage.friend_ships_storage import FriendShipsStorage


class TestFriendShipsStorage(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShipsStorage()
        self.person1 = 'person1'
        self.person2 = 'person2'

    def test_make_friends(self):
        self.temp.friend_ships = MagicMock()
        self.temp.make_friends(self.person1, self.person2)
        self.temp.friend_ships.make_friends.assert_called_with(self.person1,
                                                               self.person2)

    def test_make_friends_exception(self):
        self.temp.friend_ships.make_friends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.make_friends, 1, True)
        self.temp.friend_ships.make_friends.assert_called_with(1,
                                                               True)

    def test_get_friends_list(self):
        self.temp.get_friends_list = MagicMock(return_value={self.person1: [
            'person2']})
        self.assertEqual(self.temp.get_friends_list(self.person1), {self.person1: [
            'person2']})

    def test_are_friends_no_existing_friend(self):
        self.temp.friend_ships.dict = MagicMock()
        self.temp.friend_ships.dict.__contains__.return_value = False
        self.temp.friend_ships.dict[self.person1].__contains__.return_value \
            = False
        self.assertEqual(self.temp.are_friends(self.person1, self.person2), False)

    def test_are_friends_existing_friend(self):
        self.temp.friend_ships.dict = MagicMock()
        self.temp.friend_ships.dict.__contains__.return_value = True
        self.temp.friend_ships.dict[self.person1].__contains__.return_value \
            = True
        self.assertEqual(self.temp.are_friends(self.person1, self.person2),
                         True)

