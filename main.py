from linked_list import MyList, ListNode
from myclass import Circle
a=Circle(10,1,2)
b=Circle(8,2,2)
c=Circle(12,3,1)
lst = MyList()
lst.enqueue(a)
lst.enqueue(b)
lst.enqueue(c)
print("obj is added")
for i in lst:
    i.values()
lst.dequeue()
print("Dequeued")
for i in lst:
    i.values()
