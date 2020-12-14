class FriendShips:
    def __init__(self):
        self.dict = {}

    def make_friends(self, person1, person2):
        self.add_friend(person1, person2)
        self.add_friend(person2, person1)

    def get_friends_list(self, person):
        if person in self.dict:
            return self.dict[person]
        else:
            return 'Person does not exist'

    def are_friends(self, person1, person2):
        if person1 in self.dict and person2 in self.dict[person1]:
            return True
        return False

    def add_friend(self, person, friend):
        if person in self.dict:
            self.dict[person].append(friend)
        else:
            self.dict[person] = [friend]
