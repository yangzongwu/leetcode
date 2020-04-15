class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.cnt=0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index>=self.cnt:
            return -1
        else:
            p=self.head
            while index>0:
                p=p.next
                index-=1
            return p.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.cnt+=1
        newhead=ListNode(val)
        newhead.next=self.head
        self.head=newhead

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.cnt+=1
        if not self.head:
            self.head=ListNode(val)
        else:
            p=self.head
            while p.next:
                p=p.next
            p.next=ListNode(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index==0:
            return self.addAtHead(val)
        elif index==self.cnt:
            return self.addAtTail(val)
        elif index>self.cnt:
            return
        else:
            self.cnt+=1
            p=self.head
            while index>1:
                p=p.next
                index-=1
            node=ListNode(val)
            node.next=p.next
            p.next=node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index==0:
            self.head=self.head.next
            self.cnt-=1
        elif index>=self.cnt:
            return
        else:
            self.cnt-=1
            p=self.head
            while index>1:
                p=p.next
                index-=1
            p.next=p.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
