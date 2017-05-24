#!/anaconda/bin/python

class Set:
    def __init__(self):
        self.set=[]
    def __repr__(self):
        return str(self.set)
        
    def Contains(self,element):
        if element in self.set:
            return True
        else:
            return False

    def Add(self,newElement):
        if self.Contains(newElement) == False:
            self.set.append(newElement)

    def Remove(self,element):
        try:
            self.set.remove(element)
        except ValueError:
            print("The value is not in the list. Try another value")

    def Size(self):
        return len(self.set)

    def __or__(self,setB):
        setC=Set()
        for z in setB.set:
            setC.Add(z)
        for z in self.set:
            setC.Add(z)
        return setC

    def __and__(self,setB):
        setC=Set()
        for z in setB.set:
            if self.Contains(z)==True:
                setC.Add(z)
        return setC

    def __sub__(self,setB):
        setC=Set()
        for z in self.set:
            if setB.Contains(z)==False:
                setC.Add(z)
        return setC


                  
              
                  
