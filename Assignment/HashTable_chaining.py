class HashTable:
    size = int(input("Enter the size of hash table: "))
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        self.a = []

    def gethashvalue(self, key):
        return key % self.size
    
    def insert(self, key, value):
        h = self.gethashvalue(key)
        for i in range(self.size):
            if self.table[h] is None :
                self.table[h] = [key, value]
                return
            else:
                if self.table[h][0] == key: 
                    self.a[h] = value
                    print("Value entered in the Array!")
                else: 
                    h=h+1
                    self.a[h] = value
        return    
                
    def search(self, key):
        if result is not None:
            result = self.table[key]
            print(f"The key and value are {result}")
        else:
            result = self.a[key]
            print(f"The key and value are {result}")
            

    def delete(self, key):
        if self.table[key] is None:
            print("Nothing to delete..!")
        elif(self.table[key] is not None):
            self.table[key] = [None],[None]
            print("Deletion Sucessfull...!")
        else:
            for i in range(self.a):
                if self.a[i] == key:
                    print(self.a[i])
                else:
                    print("key not found..!")


    def display(self):
        for i in range(self.size):
            print(f"Index {i} : value: {self.table[i]}")
            
                


t = HashTable(HashTable.size)
while(1):
    print("*******MENU*******")
    print("1: Insert")
    print("2: Search")
    print("3: Display")
    print("4: Exit")
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
        exit()
    else:
        print("Invalid input")