
def bubleSort(arr, n):
	for i in  range(n):
		for j in range(n-1):
			if arr[j] > arr[j+1]:
				arr[j+1], arr[j] = arr[j], arr[j+1]
	return arr
	

def selectionSort(arr, n):
	
	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if arr[min_index] > arr[j] :
				#min_index = j
				arr[j], arr[min_index] = arr[min_index], arr[j]
	return arr



arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
	element = int(input(f"Enter the elements: {i+1} -->"))
	arr.append(element)
def menu():
	print("Select the appropriate option: ")
	print("1: Bubble Sort")
	print("2: Selection Sort")
	print("3: Exit")
while(1):
	menu()
	choice = int(input("Enter your choice: "))

	if choice == 1 :
		print("Bubble Sort: ", bubleSort(arr, n))
	elif choice == 2 :
		print("Selection Sort: ", selectionSort(arr, n))
	elif choice == 3 :
		print("Exit")
	else :
		print("Please Select Appropriate choice")

	

