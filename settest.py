#!/anaconda/bin/python
from sets import Set

set1=Set()
set2=Set()
set1.Add(1)
set1.Add(3)
set1.Add(5)
set2.Add(2)
set2.Add(4)
set2.Add(6)
print(set1.Size())
print(set2.Size())
print(set1&set2)
print(set1|set2)
print(set1-set2)

