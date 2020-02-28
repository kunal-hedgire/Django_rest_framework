'''
Binary Search Tree :

'''

class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


# element insert a item into BST
def insert(root, node):
    if root is None:
        root = node

    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node

            else:
                insert(root.right,node)

        else:
            if root.left is None:
                root.left = node

            else:
                insert(root.left,node)


# print the BST
def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


# Search a element in BST
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key),True


# Find the lowest value in the BST
def minValueNode(node):
    current = node
    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


# Find the inorder successor.
def find_inorder(root, data):
    if root.right is not None:
        return minValueNode(data.right)


# function for 2nd highest element
def second_highest(root, index):
    c = [0]
    second_highest_util(root, c, index)


# Util function to find the second largest element in BST
def second_highest_util(root, c, index):
    if root is None or c[0] >= index:
        return

    second_highest_util(root.right, c, index)
    c[0] += 1
    if c[0] == index:
        print(index,"th item in BST is", root.val)

    second_highest_util(root.left, c, index)


# Delete the Node from BST
def delete_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)

    elif key > root.val:
        root.right = delete_node(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.val)
    return root


# Swap the node and its child.
# util function for swap the node.
def swap_node_util(root, level, key):
    if root is None or (root.left is None and root.right is None):
        return

    if (level+1)% key == 0:
        root.left, root.right = root.right, root.left

    swap_node_util(root.right, level+1, key)
    swap_node_util(root.left, level+1, key)


# Swap node function.
def swap_node(root, k):
    swap_node_util(root, 1, k)


# Find the the distance of two node.
def path_to_node(root, path, data):
    if root is None:
        return False
    path.append(root.val)

    if root.val == data:
        return True

    if root.left is not None and path_to_node(root.left, path, data) or \
            root.right \
            is not None and path_to_node(root.right, path, data):
        return True
    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        path1 = []
        path_to_node(root, path1, data1)

        path2 = []
        path_to_node(root, path2, data2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return (len(path1) + len(path2) - 2*i)
    else:
        return 0





r = Node(15)
insert(r,Node(10))
insert(r,Node(20))
insert(r,Node(16))
insert(r,Node(25))
insert(r,Node(8))
insert(r,Node(12))
in_order(r)

dis = distance(r, 25, 12)
print("10,8 distance", dis)

# second_highest(r,4)
# print("after")
# swap_node(r, 2)
# in_order(r)

# delete_node(r, key=70)
# print("printing elements")
# in_order(r)
# print("Searching element...")
# if search(r, 80):
#     print("the element is found")
# else:
#     print("element is not found")
