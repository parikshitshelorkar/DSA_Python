# Implementing hash table using 2D arrary
class HashTable:
    size = int(input("Enter the size of the HashTable..: "))
    def __init__(self, size):
        self.size = size
        self.table = [[None, None] for i in range(size)]

    def gethashvalue(self, key):
        return key % self.size

    def insert(self, key, value):
        h = self.gethashvalue(key)
        for i in range(self.size):
            idx = (h+i) % self.size
            #insert if slot is empty or key matches
            if self.table[idx][0] is None or self.table[idx][0] == key:
                self.table[idx] = [key, value]
                return
        print("Hashtable is full..!")

    def search(self, key):
        if result is not None:
            result = self.table[key]
            print(f"The key and value are {result}")
        else:
            print("Entries not Found..! ")

    def delete(self, key):
        if self.table[key] is None:
            print("Nothing to delete..!")
        else:
            self.table[key] = [None],[None]
            print("Deletion Sucessfull...!")

    # def display(self):
    #     for i, item in enumerate(self.table):
    #         print(f"Index {i}: {item}")

    def display(self):
        for i in range(self.size):
            item = self.table[i]
            print(f"Index {i}: {item}")

t = HashTable(HashTable.size)
u = HashTable(HashTable.size)



while(1):
    print("*******MENU*******")
    print("1: Insert")
    print("2: Search")
    print("3: Display")
    print("4: Delete")
    print("5: Exit")
    choice = int(input("Select any operation..!"))
    if choice == 1:
        x = int(input("Enter the key: "))
        y = input("Enter the value: ")
        t.insert(x, y)
        print("Value inserted Sucessfully..!")

    elif choice == 2:
        c = int(input("Enter the key: "))        
        t.search(c)

    elif choice == 3:
        t.display()

    elif choice == 4:
        c = int(input("Enter the key: "))        
        t.delete(c)

    elif choice == 5:
        exit()
    else:
        print("Invalid input")
