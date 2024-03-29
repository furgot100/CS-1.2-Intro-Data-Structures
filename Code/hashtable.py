#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) We go through all the nodes in every bucket"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) We go through all the nodes in every bucket"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: 
        Best Case: O(1) One or few items in the buckets
        Average Case: O(n) Multiple items in multiple buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) Goes through every node in every bucket 
        of n length"""
        size = 0
        for bucket in self.buckets:
            size += bucket.length()
        return size
        

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: 
        Best case: O(1) key is in the first node of specific bucket
        Average case: O(l) goes through all nodes in the specific bucket
        """
        bucket = self.get_bucket(key)
        for current_key, value in bucket.items():
            if current_key == key:
                return True
        return False



    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: 
        Best Case: O(1) Key was in the first node of the specific bucket
        Average Case: O(l) Must go through all nodes in specific bucket to find key"""
        bucket = self.get_bucket(key)
        for current_key, value in bucket.items():
            if current_key == key:
                return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: 
        Best Case: O(1) Key to be updated or inserted is in the first node of the bucket
        Average Case: O(l) Have to go through most nodes to find given key"""
        bucket = self.get_bucket(key)
        if self.contains(key):
            for current_key, current_value in bucket.items():
                if current_key == key:
                    bucket.delete((current_key, current_value))
                    bucket.append((key, value))
        else:
            bucket.append((key,value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: 
        Best Case: O(1) Key given is in first node of bucket
        Average Case: O(l) Goes through most nodes to find given key in bucket"""
        bucket = self.get_bucket(key)
        if self.contains(key):
            for current_key, value in bucket.items():
                if current_key == key:
                    bucket.delete((current_key, value))
        else:
            raise KeyError('Key not found: {}'.format(key))
    
    def get_bucket(self,key):
        '''Returns the bucket based on the has value'''
        return self.buckets[self._bucket_index(key)]


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
