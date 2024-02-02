from collections import OrderedDict
from collections import Counter


def find_two_sum(nums, target):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = i
    return num_dict


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict(
            [(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        # import pdb
        # pdb.set_trace()
        score = 0
        name = ""
        palyed = 0
        print(self.standings.keys())
        print(self.standings)
        for i in self.standings.keys():

            if self.standings[i]['score'] > score:
                name = i
                palyed = self.standings[i]['games_played']
                score = self.standings[i]['score']
            elif self.standings[i]['score'] == score and self.standings[i]['games_played'] < palyed:
                name = i
                palyed = self.standings[i]['games_played']
                score = self.standings[i]['score']
            print(i, score, palyed, name)
        return name


if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 1)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        visited = set()

        current_song = self
        while current_song:
            if current_song.name in visited:
                return True
            visited.add(current_song.name)
            current_song = current_song.next
            print("abc")
            print(visited)
        return False

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.song_name = super(Song, cls).__new__(cls)
    #     return cls.song_name


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
print("BATAS")
second.next_song(first)
print("mkm")

print(first.is_in_repeating_playlist())
# print(second.is_in_repeating_playlist())
