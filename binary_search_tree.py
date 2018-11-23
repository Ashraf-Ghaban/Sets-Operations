

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
        self.right = None
        self.left = None
        # self.id = 0

    def insert(self,data):
        if self.data.cid == data.cid:
            return False
        elif self.data.price > data.price:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self,data):
        if self.data.cid == data:
            print(str(self.data))
            return True
        elif self.data.cid > data:
            if self.left:
                return self.left.find(data)
            else:
                print ("Requested car is not found!")
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                print ("Requested car is not found!")
                return False

    def pre_order(self):
        if self:
            print(str(self.data))
            if self.left:
                self.left.pre_order()
            if self.right:
                self.right.pre_order()

    def post_order(self):
        if self:
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
            print(str(self.data))

    def in_order(self):
        if self:
            if self.left:
                self.left.in_order()
            print(str(self.data))
            if self.right:
                self.right.in_order()


class BST:
    def __init__(self):
        self.root = None

    def bst_insert(self,data):

        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find_node(self, data):
        if self.root:
            return self.root.find(data)

        else:
            return False

    def print_bst(self, type):
        if type == 1:
            self.root.pre_order()
        elif type == 2:
            self.root.in_order()
        else:
            self.root.post_order()

    def delete_node(self,cid):
        if self.root is None:
            print("Tree is empty!")
            return False
        elif self.root.data.cid == cid:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                temp_parent = self.root
                temp = self.root.right
                while temp.left:
                    temp_parent = temp
                    temp = temp.left
                self.root.data.cid = temp.data.cid
                if temp.right:
                    if temp_parent.data.cid > temp.data.cid:
                        temp_parent.left = temp.right
                    elif temp_parent.data.cid < temp.data.cid:
                        temp_parent.right = temp.right
                else:
                    if temp.data.cid < temp_parent.data.cid:
                        temp_parent.left = None
                    else:
                        temp_parent.right = None
            return True

        parent = None
        node = self.root

        while node and node.data.cid != cid:
            parent = node
            if cid < node.data.cid:
                node = node.left
            elif cid > node.data.cid:
                node = node.right

        if node is None or node.data.cid != cid:
            return False

        elif node.left is None and node.right is None:
            if cid < parent.data.cid:
                parent.left = None
            else:
                parent.right = None
            return True

        elif node.left and node.right is None:
            if cid < parent.data.cid:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        elif node.left is None and node.right:
            if cid < parent.data.cid:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        else:
            temp_parent = node
            temp = node.right
            while temp.left:
                temp_parent = temp
                temp = temp.left

            node.cid = temp.data.cid
            if temp.right:
                if temp_parent.data.cid > temp.data.cid:
                    temp_parent.left = temp.right
                elif temp_parent.data.cid < temp.data.cid:
                    temp_parent.right = temp.right
            else:
                if temp.data.cid < temp_parent.data.cid:
                    temp_parent.left = None
                else:
                    temp_parent.right = None

bst = BST()


with open("cars.txt", "r") as cars_file:
    reader = csv.reader(cars_file)
    header = next(reader)
    for row in reader:
        car = Car(row[0],row[1],row[2],row[3],row[4],row[5])
        bst.bst_insert(car)

print(" ====================================================================== ")
print("|                                                                      |")
print("|                    Binary Search Tree Operations                     |")
print("|                                                                      |")
print(" ====================================================================== ")

while True:
    try:
        print("\n")
        print("Please select from the options below:  \n")
        print("1. Search")
        print("2. Delete")
        print("3. Show")
        print("4. Insert")
        print("5. Exit")
        print("\n")

        opt_key = int(input())

        if opt_key == 1:
            cid = input("Please enter car ID to be searched:  \n")
            bst.find_node(cid)
        elif opt_key == 2:
            cid = input("Please enter car ID to be deleted:  \n")
            bst.delete_node(cid)
        elif opt_key == 3:
            print("Please select your print option:  \n")
            print("1. Pre-Order")
            print("2. In-Order")
            print("3. Post-Order")
            p_type = input()
            bst.print_bst(int(p_type))
        elif opt_key == 4:
                print ("Enter car information: \n")
                cid = input("Car ID: \n")
                make = input("Make: \n")
                model = input("Model: \n")
                year = input("Year: \n")
                mileage = input("Mileage: \n")
                price = input("Price: \n")
                bst.bst_insert(Car(cid, make, model, year, mileage, price))
        elif opt_key == 5:
            exit()
        else:
            print ("Please enter a valid option")
    except KeyboardInterrupt:
        bst.__del__()
        exit()
