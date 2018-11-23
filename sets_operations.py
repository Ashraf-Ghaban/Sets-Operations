"""

 This class will apply differnet operations on two sets of intergers
 as well as on cartesian products.

"""
 


class Set:
      
    def __init__(self):
                
        print("===========================================================")
        print("====================== Sets Operations ====================")
        print("===========================================================")
        
        print("                                                           ")
        print("                                                           ")


    def __del__(self):
        
        print ("Thank you for using the program")
        
        
    def union(self, Set1, Set2):
        
        uSet =  set(Set1)
        
        return uSet.union(Set2)
    
    
    def intersection(self, Set1, Set2):
        
        iSet=set(Set1)
       
        return iSet.intersection(Set2)


    def difference(self, Set1, Set2):
        
        diffSet =  set(Set1)
        
        return diffSet.difference(Set2)
    
    def cartesian(self, Set1, Set2):
        
        cartSet1 =  set(Set1)
        cartSet2 = set(Set2)
        
        
        product = [[s1,s2] for s1 in cartSet1 for s2 in cartSet2]
        
        
        return product
    
    
    
    def subset(self, Set1, Set2):
        
        sSet=set(Set1)
        
        return sSet.issubset(Set2)
       
     
    
    def isEmpty(self, Set1):
        
        empSet = set(Set1)
        
        if empSet == set():
            return True
        else:
            return False
        
            
    
    def isElement(self,elm, Set1):
        
        
        if elm in Set1:
            return True
        else:
            return False
        
     
        
    def isEqual(self, Set1, Set2):
        
        eqSet1 = set(Set1)
        eqSet2= set(Set2)
        
        if  (eqSet1.difference(eqSet2) == set() and eqSet2.difference(eqSet1)) == set():
            return True
        else:
            return False
        
    
    
    def getCardinality(self, Set1):
        
        cardSet = len(Set1)
        
        return cardSet
       
        
    def addElement(self, elm, Set1):
        
        addSet = set(Set1)
        
        addSet.add(elm)
        
        return addSet
        
    
    
    def removeElement(self, elm, Set1):
        
        remSet = set(Set1)
        
        remSet.remove(elm)
        
        return remSet
             
    
    
    def clearSet(self,Set1):
        
        clsSet = set(Set1)
        
        clsSet.clear()
        
        return clsSet



    def toArray(self,Set1):
        
        arr=[]
        arrSet = set(Set1)
        for elm in arrSet:
            arr.append(elm)
        
        return arr



    def printSet(self,Set1):
        
        prntSet = set(Set1)
        
              
        return prntSet



result = Set()

s1 = input("Enter the primary set (elements are integers and comma delimited):  ").split(",")
s1=set(map(int,s1))

s2 = input("Enter any given set (elements are integers and comma delimited):  ").split(",")
s2=set(map(int,s2))

arr=[]


while True:
    try:
        
    
        print("                                                           ")
        print("                                                           ")
        print("1.  Union ")
        print("2.  Intersection ")
        print("3.  Difference ")
        print("4.  Cartesian Product ")
        print("5.  Subset Check")
        print("6.  Empty Check ")
        print("7.  Element Exist Check ")
        print("8.  Equality Check ")
        print("9.  Set Cardinality")
        print("10. Add Element")
        print("11. Delete Element ")
        print("12. Clear Set ")
        print("13. Convert to Array ")
        print("14. Print Set ")

        print("===========================================================")
        menuID = int (input("Select the operation from the menu above - (press Alt+c to exit):   "))
        
        print("===========================================================")

        print("                                                           ")









        if menuID == 1:
            
            s3 = result.union(s1,s2)
            if s3 == set():
                print ("{}")
            else:
                print (s3)

        elif menuID == 2:
            

            s3 = result.intersection(s1,s2)
            if s3 == set():
                print ("{}")
            else:
                print (s3)
            
        elif menuID == 3:
            
            
            s3 = result.difference(s1,s2)
            if s3 == set():
                print ("{}")
            else:
                print (s3)

        elif menuID == 4:
            
            s3 = result.cartesian(s1,s2)
            print (s3)
            
        elif menuID == 5:
            
            if result.subset(s1,s2) == True:
                print("The primary set is subset of the given set")
            else:
                print("The primary set is not subset of the given set")
                
        elif menuID == 6:
            
            if result.isEmpty(s1) == True:
                print("The primary set is empty")
            else:
                print("The primary set is not empty")
                
        elif menuID == 7:
                
            elm = int(input("Enter an integer to check if it exists in the set:     "))
                
            if result.isElement(elm,s1) == True:
                print("The entered number is an element of the parimary set")
            else:
                print("The entered number is not an element of the parimary set")
            
        elif menuID == 8:
            
            if result.isEqual(s1,s2) == True:
                print("Sets are equal")
            else:
                print("Sets are not equal")
                
        elif menuID == 9:
                
            s3 = result.getCardinality(s1)
            print("The parimary set consist of " + str(s3) + " elements")
            
            
        elif menuID == 10:
            
            elm = int(input("Enter an integer to add to the parimary set:     "))
            
            if not (result.isElement(elm,s1)):
                s3= result.addElement(elm,s1)
                print(s3)
            else:
                print("Element already exists!")
                
            
        elif menuID == 11:
            
            elm = int(input("Enter an integer to remove from the parimary set:     "))
            
            if (result.isElement(elm,s1)):
                s3= result.removeElement(elm,s1)
                print(s3)
            else:
                print("Element does not exist!")
                
                
        elif menuID == 12:
            
            s3 = result.clearSet(s1)
            if s3 == set():
                print ("{}")
            else:
                print(s3)
                
        elif menuID == 13:
                
            arr = result.toArray(s1)
            if arr == []:
                print ("[]")
            else:
                print(arr)    
                
                
        elif menuID == 14:
                
            s3 = result.printSet(s1)
            print(s3)

        else:
            print("Select an option from the menu above!")

    except KeyboardInterrupt:
        result.__del__()
        exit()

        
