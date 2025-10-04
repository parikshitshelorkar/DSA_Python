#  CreateaStudentRecordManagementSystemusinglinkedlist
#  •Useasingly/doublylinkedlisttostorestudentdata(RollNo,Name,Marks).
#  •Performoperations:Add,Delete,Update,Search,andSort.
#  •Displayrecordsinascending/descendingorderbasedonmarksorrollnumber

# class Student:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# #Creating Nodes
# node1 = Student(10)
# node2 = Student(20)
# node3 = Student(30)
# node4 = Student(40)
# print("Objects created..")

# # Connecting nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4
# print("Nodes linked..")
 
# # Printing the linked list
# current = node1
# while current is not None:
#     print(current.data , end = "-> ")
#     current = current.next
#     #print(current)
# print(None)
    
class StudentRecord:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        
        self.next = None
        
    #def addInfo(self):
    def printInfo(self):
        print()
        print("Name = ", self.name)
        print("Roll no = ", self.roll)
        print("Marks = ", self.marks)
        print()
    


    def insertData(head, after_roll):
        current = head
        while current is not None:
            name = input("Enter the name: ")
            roll = int(input("Roll No: "))
            marks = int(input("Enter your Marks: "))
            new_node = StudentRecord(name, roll, marks)
            new_node.next = current.next
            current.next = new_node
            return
        return

    def display_list(head):
        current = head
        while current is not None:
            print(f"{current.roll} -> ", end="")
            current = current.next
        print("None")

    def del_student():
        pass

    #object creation
sr1 = StudentRecord("Parikshit", 111, 99)
sr2 = StudentRecord("Sumit", 222, 78)
sr3 = StudentRecord("Yashdeep", 333, 88)
sr4 = StudentRecord("Aditya", 444, 56)
sr5 = StudentRecord("Suraj", 555, 88)

#Linking
sr1.next = sr2
sr2.next = sr3
sr3.next = sr4
sr4.next = sr5
sr5.next = None


current = sr1
while current is not None:
    print(current.roll , end = "-> ")
    current = current.next
    #print(current)

# sr1.printInfo()
# sr2.printInfo()
# sr3.printInfo()
# sr4.printInfo()
# sr5.printInfo()
StudentRecord.insertData(sr1, 204)
StudentRecord.display_list(sr1)
print(sr1.next)
