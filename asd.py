from queue import SimpleQueue
import collections


class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        # Use a nested list comprehension to generate all combinations of one ingredient and one topping
        return [[ingredient, topping] for ingredient in self.ingredients for topping in self.toppings]


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    # should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
    print(machine.scoops())


###########################

def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    # Get the number of rows and columns in the map matrix
    num_rows = len(map_matrix)
    num_cols = len(map_matrix[0])

    # Create a set to keep track of visited positions
    visited = set()

    # Define a recursive helper function for DFS
    def dfs(row, col):
        # Check if the current position is out of bounds or not traversable
        if row < 0 or row >= num_rows or col < 0 or col >= num_cols or not map_matrix[row][col]:
            return False

        # Check if the current position is the destination
        if row == to_row and col == to_column:
            return True

        # Mark the current position as visited
        visited.add((row, col))

        # Recursive DFS in all possible directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if (new_row, new_col) not in visited:
                if dfs(new_row, new_col):
                    return True

        return False

    # Start DFS from the initial position
    return dfs(from_row, from_column)


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ]

    print(route_exists(0, 0, 2, 2, map_matrix))


########################


Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    if root is None:
        return False

    queue = SimpleQueue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        if current_node.value == value:
            return True
        if current_node.left:
            queue.put(current_node.left)
        if current_node.right:
            queue.put(current_node.right)

    return False


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))
#######################
########################


Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    if root is None:
        return False

    if root.value == value:
        return True

    return contains(root.left, value) or contains(root.right, value)


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))
# call to contains(n2,3) should return True since tree with root at n2 contains number 3
#  https://app.testdome.com/screening/test/08280085de1342ffa73023e9b8f49c58


######################

def unique_names(names1, names2):
    return None


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    # should print Ava, Emma, Olivia, Sophia
    print(unique_names(names1, names2))

# please complete the unique_names


def unique_names(names1, names2):
    combined_names = names1 + names2  # Combine the two input lists
    # Remove duplicates using a set and convert back to a list
    unique_names = list(set(combined_names))
    return unique_names


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    # should print Ava, Emma, Olivia, Sophia
    print(unique_names(names1, names2))


############################
