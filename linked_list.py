from mylistiterator import MyListIterator

class ListNode:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class MyList:
    def __init__(self):
        self.head = None
        self.last = None
 
    def enqueue(self, data):
        if self.last is None:
            self.head = ListNode(data)
            self.last = self.head
        else:
            self.last.next = ListNode(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

    def __iter__( self ):
        return MyListIterator(self.head)
