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


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_tail(self,data):
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

    def remove_from_tail(self):
        if self.head is None:
            return None
        else:
            curr_node = self.head
            prev_node = self.head
            while curr_node.next:
                prev_node = curr_node
                curr_node = curr_node.next
            prev_node.next = None

    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_from_head(self):
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


linkedlist = LinkedList()

with open("cars.txt", "r") as cars_file:
    reader = csv.reader(cars_file)
    header = next(reader)
    for row in reader:
        car = Car(row[0],row[1],row[2],row[3],row[4],row[5])
        linkedlist.add_to_tail(car)

print(" ====================================================================== ")
print("|                                                                      |")
print("|                        Linked List Operations                        |")
print("|                                                                      |")
print(" ====================================================================== ")

while True:
    try:
        print("\n")
        print("Please select from the options below:  \n")
        print("1. Search")
        print("2. Delete")
        print("3. Show")
        print("4. Append")
        print("5. Remove")
        print("6. Exit")
        print("\n")

        opt_key = int(input())

        if opt_key == 1:
            cid = input("Please enter car ID to be searched:  \n")
            linkedlist.search_car(cid)
        elif opt_key == 2:
            cid = input("Please enter car ID to be deleted:  \n")
            linkedlist.delete_car(cid)
        elif opt_key == 3:
            linkedlist.print_list()
        elif opt_key == 4:
            print("Please select from the options below:  \n")
            print("1. Append to Head")
            print("2. Append to Tail")
            append_key = int(input())
            print("\n")
            if append_key == 1:
                print ("Enter car information: \n")
                cid = input("Car ID: \n")
                make = input("Make: \n")
                model = input("Model: \n")
                year = input("Year: \n")
                mileage = input("Mileage: \n")
                price = input("Price: \n")
                linkedlist.add_to_head(Car(cid, make, model, year, mileage, price))
            elif append_key == 2:
                print("Enter car information: \n")
                cid = int(input("Car ID: \n"))
                make = str(input("Make: \n"))
                model = str(input("Model: \n"))
                year = int(input("Year: \n"))
                mileage = int(input("Mileage: \n"))
                price = int(input("Price: \n"))
                linkedlist.add_to_tail(Car(cid, make, model, year, mileage, price))
            else:
                print("Please enter a valid option")

        elif opt_key == 5:
            print("Please select from the options below:  \n")
            print("1. Remove from Head")
            print("2. Remove from Tail")
            remove_key = int(input())
            print("\n")
            if remove_key == 1:
                linkedlist.remove_from_head()
            else:
                linkedlist.remove_from_tail()
        elif opt_key == 6:
            exit()
        else:
            print ("Please enter a valid option")
    except KeyboardInterrupt:
        LinkedList.__del__()
        exit()
