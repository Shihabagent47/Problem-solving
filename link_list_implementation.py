class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize next as None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head as None

    def append(self, data):
        """Add a node with the specified data to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Set the new node as the next of the last node

    def insert(self, data, position):
        """Insert a node with the specified data at the given position."""
        new_node = Node(data)
        if position == 0:  # Insert at the head
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if not current:  # Position is out of bounds
                    raise IndexError("Position out of bounds")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, key):
        """Delete the first node with the specified key (data)."""
        current = self.head
        if current and current.data == key:  # If head node holds the key
            self.head = current.next
            return
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if not current:  # Key not found in the list
            return
        previous.next = current.next  # Unlink the node from the list

    def display(self):
        """Print the linked list as a sequence of nodes."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def search(self, key):
        """Search for a node by its data and return True if found, else False."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def size(self):
        """Return the number of nodes in the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count




#Exmplses

# Create a linked list
ll = SinglyLinkedList()

# Append elements to the linked list
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3