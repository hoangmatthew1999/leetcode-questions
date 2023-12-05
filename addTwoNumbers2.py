# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.next == None and l2.next == None and l1.val + l2.val < 10:
            return ListNode(l1.val + l2.val)
        sum = l1.val + l2.val
        carry = 0
        if sum >= 10:
            returnList = ListNode(sum % 10)
            returnListHead = returnList
            carry = 1
            l1 = l1.next
            l2 = l2.next
        elif sum < 10:
            returnList = ListNode(sum)
            returnListHead = returnList
            l1 = l1.next
            l2 = l2.next
        while l1 != None or l2 != None:
    
            if l1 == None:
                sum = l2.val + carry
                if sum < 10:
                    insertNode = ListNode(sum)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 0
                elif sum > 10:
                    insertNode = ListNode(sum % 10)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 0
                elif sum == 10:
                    insertNode = ListNode(sum%10)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 1
            if l2 == None:
                sum = l1.val + carry
                if sum < 10:
                    insertNode = ListNode(sum)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 0
                elif sum > 10:
                    insertNode = ListNode(sum % 10)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 0
                elif sum == 10:
                    insertNode = ListNode(sum%10)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 1
            if l1 != None and l2 != None:
                sum = l1.val + carry + l2.val
                print(sum)
                if sum < 10:
                    insertNode = ListNode(sum)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 0
                elif sum > 10:
                    insertNode = ListNode(sum % 10)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 1
                elif sum == 10:
                    insertNode = ListNode(sum%10)
                    returnList.next = insertNode
                    returnList = returnList.next
                    carry = 1

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            
        if carry == 1:
            #at end of loop, if there is still a carry, need to   manually add it
            newNode = ListNode(1)
            returnList.next = newNode
            
        return returnListHead
                
            
        




        
