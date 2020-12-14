from friend_ships.friend_ships import FriendShips


class FriendShipsStorage:
    def __init__(self):
        self.friend_ships = FriendShips()

    def make_friends(self, person1, person2):
        self.friend_ships.make_friends(person1, person2)

    def get_friends_list(self, person):
        return self.friend_ships.get_friends_list(person)

    def are_friends(self, person1, person2):
        return self.friend_ships.are_friends(person1, person2)