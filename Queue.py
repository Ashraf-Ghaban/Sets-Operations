"""
===========================================================
==========          Ashraf Haj Ghaban           ===========
===========================================================
"""


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


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = None
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = None

    def dequeue(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(str(curr_node.data))
            curr_node = curr_node.next

    def search_car(self,cid):
        if self.head:
            curr_node = self.head
            while curr_node:
                if curr_node.data.cid == cid:
                    print(str(curr_node.data))
                    return curr_node.data.cid
                curr_node = curr_node.next
        else:
            print("List is Empty...")
            return None
        print("Requested car can not be found")

    def delete_car(self,cid):
        if self.head:
            curr_node = self.head
            while curr_node.next:
                prev_node = curr_node
                curr_node = curr_node.next
                if curr_node.data.cid == cid:
                    prev_node.next =curr_node.next
                    return

        else:
            print("List is Empty...")
            return

        print("Requested car can not be found")


queue = Queue()

with open("cars.txt", "r") as cars_file:
    reader = csv.reader(cars_file)
    header = next(reader)
    for row in reader:
        car = Car(row[0],row[1],row[2],row[3],row[4],row[5])
        queue.enqueue(car)

print(" ====================================================================== ")
print("|                                                                      |")
print("|                        Queue Operations                              |")
print("|                                                                      |")
print(" ====================================================================== ")

while True:
    try:
        print("\n")
        print("Please select from the options below:  \n")
        print("1. Search")
        print("2. Delete")
        print("3. Show List")
        print("4. Enqueue")
        print("5. Dequeue")
        print("6. Exit")
        print("\n")

        opt_key = int(input())

        if opt_key == 1:
            cid = input("Please enter car ID to be searched:  \n")
            queue.search_car(cid)
        elif opt_key == 2:
            cid = input("Please enter car ID to be deleted:  \n")
            queue.delete_car(cid)
        elif opt_key == 3:
            queue.print_list()
        elif opt_key == 4:
                print("Enter car information: \n")
                cid = int(input("Car ID: \n"))
                make = str(input("Make: \n"))
                model = str(input("Model: \n"))
                year = int(input("Year: \n"))
                mileage = int(input("Mileage: \n"))
                price = int(input("Price: \n"))
                queue.enqueue(Car(cid, make, model, year, mileage, price))
        elif opt_key == 5:
                queue.dequeue()
        elif opt_key == 6:
            exit()
        else:
            print ("Please enter a valid option")
    except KeyboardInterrupt:
        Queue.__del__()
        exit()
