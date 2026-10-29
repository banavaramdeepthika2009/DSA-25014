class AVLTree:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.left = [-1] * size
        self.right = [-1] * size
        self.height = [0] * size
        self.root = -1
        self.count = 0
    # Create new node
    def create_node(self, data):
        if self.count == self.size:
            print("Tree is full")
            return -1

        index = self.count
        self.data[index] = data
        self.left[index] = -1
        self.right[index] = -1
        self.height[index] = 1

        self.count += 1

        return index

    # Get height
    def get_height(self, index):

        if index == -1:
            return 0

        return self.height[index]

    # Get balance factor
    def get_balance(self, index):

        if index == -1:
            return 0

        return self.get_height(self.left[index]) - \
               self.get_height(self.right[index])

    # Update height
    def update_height(self, index):

        self.height[index] = 1 + max(
            self.get_height(self.left[index]),
            self.get_height(self.right[index])
        )

    # Right rotation
    def right_rotate(self, index):

        new_root = self.left[index]
        temp = self.right[new_root]

        self.right[new_root] = index
        self.left[index] = temp

        self.update_height(index)
        self.update_height(new_root)

        return new_root

    # Left rotation
    def left_rotate(self, index):

        new_root = self.right[index]
        temp = self.left[new_root]

        self.left[new_root] = index
        self.right[index] = temp

        self.update_height(index)
        self.update_height(new_root)

        return new_root

    # Insert
    def insert_node(self, index, data):

        if index == -1:
            return self.create_node(data)

        if data < self.data[index]:

            self.left[index] = self.insert_node(
                self.left[index], data
            )

        elif data > self.data[index]:

            self.right[index] = self.insert_node(
                self.right[index], data
            )

        else:
            print("Duplicate value")
            return index

        self.update_height(index)

        balance = self.get_balance(index)

        # LL Case
        if balance > 1 and data < self.data[self.left[index]]:
            return self.right_rotate(index)

        # RR Case
        if balance < -1 and data > self.data[self.right[index]]:
            return self.left_rotate(index)

        # LR Case
        if balance > 1 and data > self.data[self.left[index]]:
            self.left[index] = self.left_rotate(self.left[index])
            return self.right_rotate(index)

        # RL Case
        if balance < -1 and data < self.data[self.right[index]]:
            self.right[index] = self.right_rotate(self.right[index])
            return self.left_rotate(index)

        return index

    # Insert function
    def insert(self, data):

        self.root = self.insert_node(self.root, data)

    # Find minimum node
    def minimum(self, index):

        current = index

        while self.left[current] != -1:
            current = self.left[current]

        return current

    # Delete
    def delete_node(self, index, data):

        if index == -1:
            return -1

        if data < self.data[index]:

            self.left[index] = self.delete_node(
                self.left[index], data
            )

        elif data > self.data[index]:

            self.right[index] = self.delete_node(
                self.right[index], data
            )

        else:

            # No child
            if self.left[index] == -1 and self.right[index] == -1:
                return -1

            # Only right child
            elif self.left[index] == -1:
                return self.right[index]

            # Only left child
            elif self.right[index] == -1:
                return self.left[index]

            # Two children
            else:

                temp = self.minimum(self.right[index])

                self.data[index] = self.data[temp]

                self.right[index] = self.delete_node(
                    self.right[index],
                    self.data[temp]
                )

        self.update_height(index)

        balance = self.get_balance(index)

        # LL Case
        if balance > 1 and self.get_balance(self.left[index]) >= 0:
            return self.right_rotate(index)

        # LR Case
        if balance > 1 and self.get_balance(self.left[index]) < 0:
            self.left[index] = self.left_rotate(self.left[index])
            return self.right_rotate(index)

        # RR Case
        if balance < -1 and self.get_balance(self.right[index]) <= 0:
            return self.left_rotate(index)

        # RL Case
        if balance < -1 and self.get_balance(self.right[index]) > 0:
            self.right[index] = self.right_rotate(self.right[index])
            return self.left_rotate(index)

        return index

    # Delete function
    def delete(self, data):

        if self.search(data):
            self.root = self.delete_node(self.root, data)
            print("Element deleted")
        else:
            print("Element not found")

    # Search
    def search_node(self, index, data):

        if index == -1:
            return False

        if self.data[index] == data:
            return True

        if data < self.data[index]:
            return self.search_node(self.left[index], data)

        return self.search_node(self.right[index], data)

    # Search function
    def search(self, data):

        return self.search_node(self.root, data)

    # Inorder
    def inorder(self, index):

        if index != -1:

            self.inorder(self.left[index])

            print(self.data[index], end=" ")

            self.inorder(self.right[index])

    # Preorder
    def preorder(self, index):

        if index != -1:

            print(self.data[index], end=" ")

            self.preorder(self.left[index])

            self.preorder(self.right[index])

    # Postorder
    def postorder(self, index):

        if index != -1:

            self.postorder(self.left[index])

            self.postorder(self.right[index])

            print(self.data[index], end=" ")

    # Display array
    def display(self):

        print("\nIndex\tData\tLeft\tRight\tHeight")

        for i in range(self.count):

            print(
                i,
                "\t",
                self.data[i],
                "\t",
                self.left[i],
                "\t",
                self.right[i],
                "\t",
                self.height[i]
            )

# Main Program

avl = AVLTree(50)

while True:

    print("\n----- AVL TREE USING ARRAY -----")
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
        value = int(input("Enter value: "))
        avl.insert(value)
        print("Element inserted")
    elif choice == 2:
        value = int(input("Enter value: "))
        avl.delete(value)
    elif choice == 3:
        value = int(input("Enter value: "))

        if avl.search(value):
            print("Element found")
        else:
            print("Element not found")
    elif choice == 4:

        print("Inorder:", end=" ")
        avl.inorder(avl.root)
        print()

    elif choice == 5:
        print("Preorder:", end=" ")
        avl.preorder(avl.root)
        print()

    elif choice == 6:

        print("Postorder:", end=" ")
        avl.postorder(avl.root)
        print()

    elif choice == 7:

        avl.display()

    elif choice == 8:

        print("Program ended")
        break

    else:
        print("Invalid choice")
