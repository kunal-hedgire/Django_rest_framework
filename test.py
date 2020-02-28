# open_b = "{[("
# closing_b = "}])"
# b_dict = {"(": ")", "{":"}", "[":"]"}
#
#
# def parenthesis_check(temp):
#     stack = []
#     for val in temp:
#         if val in open_b:
#             stack.append(val)
#         if val in closing_b:
#             bracket = stack.pop()
#             if not b_dict[bracket] == val:
#                 return False
#     if not stack:
#         return True
#     else:
#         return False
#
# sample_string = "{[()]}"
# print(parenthesis_check(sample_string))


# class contextManager:
#     def __init__(self):
#         print("Init method")
#
#     def __enter__(self):
#         print("Inside the enter method")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Inside the exit method")
#
#
# with contextManager() as manager:
#     print("with block")


# class Error(Exception):
#     pass
#
# class ValueTooSmall(Error):
#     pass
#
# class ValueTooLargeError(Error):
#    """Raised when the input value is too large"""
#    pass
#
# number = 10
#
# while True:
#     try:
#         i_num = int(input("Enter the number:"))
#         if i_num < number:
#             raise ValueTooSmall
#
#         elif i_num> number:
#             raise ValueTooLargeError
#
#         break
#     except ValueTooSmall:
#        print("This value is too small, try again!")
#
#     except ValueTooLargeError:
#        print("This value is too large, try again!")
#        print()
# print("Congratulations! You guessed it correctly.")


# n = 5
# with open('myfile.txt') as file:
#     for _ in range(n):
#         print(file.readline())


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def pathToNode(root, path, k):
    # base case handling
    if root is None:
        return False

    # append the node value in path
    path.append(root.data)

    # See if the k is same as root's data
    if root.data == k:
        return True

    # Check if k is found in left or right
    # sub-tree
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right != None and pathToNode(root.right, path, k))):
        return True

    # If not present in subtree rooted with root,
    # remove root from path and return False
    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        # store path corresponding to node: data1
        path1 = []
        pathToNode(root, path1, data1)

        # store path corresponding to node: data2
        path2 = []
        pathToNode(root, path2, data2)

        # iterate through the paths to find the
        # common path length
        i = 0
        while i < len(path1) and i < len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i + 1

        # get the path length by deducting the
        # intersecting path length (or till LCA)
        return (len(path1) + len(path2) - 2 * i)
    else:
        return 0


# Driver Code to test above functions
root = Node(5)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.right.right = Node(1)
root.right.left = Node(4)
# root.left.right = Node(5)
# root.right.left.right = Node(8)
dist = distance(root, 5, 4)
print("Distance between node {} & {}: {}".format(5, 4, dist))
