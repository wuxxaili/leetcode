#142 Linked List Cycle II

##Given a linked list, return the node where the cycle begins. 

# First, we use fast ans slow pointers to find if there is a cycle
# Let the length of cycle is N, the head to node of cycle begins is L1
# slow pointer total number of steps is L1+L2
# fast pointer total number of steps is (L1+L2)*2 = L1+L2 + N*m (fast pointer walk N*m steps more than slow)
# we have L1+L2 = N*m, then let another pointer slow2 start from head
# it will take L1 steps to the node of cycle begins
# meanwhile, slow will walk N*m - L2 steps, they meet at the node of cycle begins

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
            
        if fast and fast.next:
            slow2 = head
            while slow2!= slow:
                slow2 = slow2.next    
                slow = slow.next
            return slow
        return None
        
       