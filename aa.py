class TextInput:
    num = []

    def add(self, char):
        print(char)
        self.num.append(char)

    def get_value(self):
        print(self.num)
        return "".join(self.num)


class NumericInput(TextInput):
    num = []

    def add(self, char):
        try:
            int(char)
            print(char)
            self.num.append(char)
        except:
            pass


if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())


def find_two_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i

    return None


def find_two_sume(nums, target):
    num_dict = {}
    key = []
    val = []
    index_key = []
    index_val = []

    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums:
            # print("fgfg")
            # print(key)
            # print(val, num)
            # print(complement)
            if num not in val:
                key.append(num)
                index_key.append(i)
                val.append(complement)
                index_val.append(nums.index(complement))
            # return (num_dict[complement], i)
        # num_dict[num] = i
    lo = [(l, u) for l, u in zip(key, val)]
    lol = [(l, u) for l, u in zip(index_key, index_val)]
    print(nums)
    return lo, lol


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
    print(find_two_sume([3, 1, 5, 7, 5, 9], 10))
