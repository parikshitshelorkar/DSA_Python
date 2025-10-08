class HashTable:
    def _init_(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Each bucket is a list

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        # Check if key exists; if yes, update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, append new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            for pair in bucket:
                print(f"({pair[0]}: {pair[1]}) ->", end=" ")
            print("None")

# ----------------- Menu Driven -----------------

ht = HashTable()

while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert key-value pair")
    print("2. Search for a key")
    print("3. Remove a key")
    print("4. Display hash table")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        ht.insert(key, value)
        print("Inserted successfully!")
    elif choice == "2":
        key = input("Enter key to search: ")
        value = ht.get(key)
        if value is not None:
            print(f"Value: {value}")
        else:
            print("Key not found!")
    elif choice == "3":
        key = input("Enter key to remove: ")
        if ht.remove(key):
            print("Key removed successfully!")
        else:
            print("Key not found!")
    elif choice == "4":
        ht.display()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")

