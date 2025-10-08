# two edge cases: 1. different lengths 2. no input nodes but carry value 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # fake starting node
        cur = dummy # pointer 

        carry = 0 
        while l1 or l2 or carry: # runs as long as there's something left to add 
            v1 = l1.val if l1 else 0 # go thourgh linked list 
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry 
            carry = val // 10 
            val = val % 10 
            cur.next = ListNode(val)

            cur = cur.next 
            l1 = l1.next if l1 else None # checking if l1 exists 
            l2 = l2.next if l2 else None 

        return dummy.next 

    """   
    example: 
    val = 4 + 6 + 0 = 10
    carry = 10 // 10 = 1
    val = 10 % 10 = 0
    """