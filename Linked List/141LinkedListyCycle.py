#141 Linked List Cycle

##Given a linked list, determine if it has a cycle in it.

#Idea: floyd's slow and fast pointers, if there is a cycle, then the fast pointer could always catch up the slow pointer

##Tradeoff for speed of fast pointer: 
##If the step size of fast pointer is large, then it could catch up the slow one quickly in the cycle.
##However, it could be waste of time before the slow pointer run into the cycle.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        Fast,Slow = head,head
        while Fast and Fast.next:
            Slow = Slow.next
            Fast = Fast.next.next
            if Slow == Fast:
                return True
        return False
