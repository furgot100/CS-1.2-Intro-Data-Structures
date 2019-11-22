#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) The bigger the the list the more time it takes to run."""
        length = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            length += 1
        return length 


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Checks the tail, makes the next node into the
        item, then assigning the tail to the new node."""
        node = Node(item)
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) Similar to append, only checks the head and the node
        next to it"""
        node = Node(item)
        if not self.is_empty():
            node.next = self.head
        else:
            self.tail = node
        self.head = node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If the item was in the head or near the beginning
        Worst case running time: O(n) Goes past the first node and continues on"""
        if not self.is_empty():
            current_node = self.head
            while current_node is not None:
                if quality(current_node.data) is True:
                    return current_node.data
                else:
                    current_node = current_node.next
        else:
            return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) If the item was the first node
        Worst case running time: O(n) If item goes past the first node"""
        previous_node = None
        current_node = self.head
        found = False 
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        elif self.head == self.tail:
            if current_node.data== item:
                self.head = None
                self.tail = None
            else:
                raise ValueError('Item not found: {}'.format(item))
        else:
            while current_node is not None:
                if current_node.data == item:
                    found = True
                    if previous_node is None:
                        self.head = current_node.next
                    elif current_node == self.tail:
                        self.tail = previous_node
                        previous_node.next = None
                    else:
                        previous_node.next = current_node.next
                previous_node = current_node
                current_node = current_node.next
            if found is False:
                raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
