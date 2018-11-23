

import csv


class Car:
    def __init__(self, cid, make, model, year, mileage, price):
        self.cid = cid
        self.make = str(make)
        self.model = str(model)
        self.year = int(year)
        self.mileage = mileage
        self.price = price

    def __str__(self):
        return '{}-{}-{}-{}-{}-{}'.format(self.cid,self.make,self.model,self.year,self.mileage,self.price)


class MaxHeap:

    def __init__(self, cars = []):
        self.heap = []

    def heapify(self, parent):
        l_son = parent * 2 +1
        r_son = parent * 2 + 2
        largest = parent

        if self.heap[l_son].price > self.heap[parent].price and l_son < len(self.heap):
            largest = l_son

        if self.heap[r_son].price > self.heap[largest].price and r_son < len(self.heap):
            largest = r_son

        if largest != parent:
            self.heap[parent],self.heap[largest] = self.heap[largest], self.heap[parent]
            self.heapify(largest)

    def build_heap(self):
        for i in range((len(self.heap)//2),0):
            self.heapify(i)

    def extract_max(self):
        maxh = self.heap[0]
        heap_size = len(self.heap)
        self.heap[0] = self.heap[heap_size - 1]
        heap_size -= 1
        self.heapify(0)
        return maxh

    def heap_insert(self, car):
        self.heap.append(car)
        index = len(self.heap) - 1
        parent = index // 2

        while True:
            if index <= 1:
                return
            elif self.heap[index].price > self.heap[parent].price:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            else:
                return

    def print_heap(self):
        # for counter in range (0, len(self.heap)):
        for car in self.heap:
            print (str(car))


the_heap = MaxHeap()

with open("cars.txt", "r") as cars_file:
    reader = csv.reader(cars_file)
    header = next(reader)
    for row in reader:
        car = Car(row[0],row[1],row[2],row[3],row[4],row[5])
        the_heap.heap_insert(car)

print(" ====================================================================== ")
print("|                                                                      |")
print("|                        Max Heap Operations                           |")
print("|                                                                      |")
print(" ====================================================================== ")

while True:
    try:
        print("\n")
        print("Please select from the options below:  \n")
        print("1. Insert")
        print("2. Extract")
        print("3. Show")
        print("4. Exit")
        print("\n")

        opt_key = int(input())

        if opt_key == 1:
            print("Enter car information: \n")
            cid = input("Car ID: \n")
            make = input("Make: \n")
            model = input("Model: \n")
            year = input("Year: \n")
            mileage = input("Mileage: \n")
            price = input("Price: \n")
            the_heap.heap_insert(Car(cid, make, model, year, mileage, price))
        elif opt_key == 2:
            the_heap.extract_max()
            print("The car with the highest price has been deleted  \n")
        elif opt_key == 3:
            the_heap.print_heap()
        elif opt_key == 4:
            exit()
        else:
            print ("Please enter a valid option")
    except KeyboardInterrupt:
        MaxHeap.__del__()
        exit()
