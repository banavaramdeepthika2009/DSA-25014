class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0

        return self.height(root.left) - self.height(root.right)

    def update_height(self, root):
        root.height = 1 + max(
            self.height(root.left),
            self.height(root.right)
        )

    # Right Rotation
    def right_rotate(self, root):
        new_root = root.left
        temp = new_root.right

        new_root.right = root
        root.left = temp

        self.update_height(root)
        self.update_height(new_root)

        return new_root

    # Left Rotation
    def left_rotate(self, root):
        new_root = root.right
        temp = new_root.left

        new_root.left = root
        root.right = temp

        self.update_height(root)
        self.update_height(new_root)

        return new_root

    # Insert
    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        else:
            return root

        self.update_height(root)

        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # LR Case
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find minimum node
    def min_value_node(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    # Delete
    def delete(self, root, data):

        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:

            # No child
            if root.left is None and root.right is None:
                return None

            # Only right child
            elif root.left is None:
                return root.right

            # Only left child
            elif root.right is None:
                return root.left

            # Two children
            else:
                temp = self.min_value_node(root.right)

                root.data = temp.data

                root.right = self.delete(
                    root.right,
                    temp.data
                )

        self.update_height(root)

        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search
    def search(self, root, data):

        if root is None:
            return False

        if root.data == data:
            return True

        if data < root.data:
            return self.search(root.left, data)

        return self.search(root.right, data)

    # Inorder
    def inorder(self, root):

        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder
    def preorder(self, root):

        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder
    def postorder(self, root):

        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Display tree
    def display(self, root, level=0):

        if root is not None:
            self.display(root.right, level + 1)

            print("    " * level + str(root.data))

            self.display(root.left, level + 1)


# Main program

avl = AVLTree()
root = None

while True:

    print("\n--- AVL TREE USING LINKED LIST ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Display")
    print("8. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        data = int(input("Enter value: "))
        root = avl.insert(root, data)
    elif choice == 2:
        data = int(input("Enter value: "))
        root = avl.delete(root, data)
    elif choice == 3:
        data = int(input("Enter value: "))
        if avl.search(root, data):
            print("Element found")
        else:
            print("Element not found")
    elif choice == 4:
        print("Inorder:", end=" ")
        avl.inorder(root)
        print()
    elif choice == 5:
        print("Preorder:", end=" ")
        avl.preorder(root)
        print()
    elif choice == 6:
        print("Postorder:", end=" ")
        avl.postorder(root)
        print()
    elif choice == 7:
        print("\nAVL Tree:")
        avl.display(root)
    elif choice == 8:
        break
    else:
        print("Invalid choice")
