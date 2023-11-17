def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.next == None and l2.next == None:
            return l1.val + l2.val
        
        carry = 0
        returnList = ListNode(l1.val + l2.val, None)
        if l1.next != None:
                l1 = l1.next
        if l2.next != None:
                l2 = l2.next
        returnList.next = ListNode(2,None)
        traverser = returnList
        traverser = traverser.next
        traverser.next = ListNode(3,None)
        
        
        while(l1.next != None or l2.next != None):
            sum = l1.val + l2.val # remember to add carry 
            if sum >= 10:
                
                returnList_val = sum % 10 
                returnList_next = next
                returnList.next = ListNode(returnList_val, returnList_next)
                # returnList.next = newNode
                # returnList = returnList.next
                carry = 1
                
                print("asd")
            else:# sum < 10
                
                returnList_val = sum 
                returnList_next = None
                newNode = ListNode(returnList_val, returnList_next)
                returnList.next = newNode
                carry = 0
                
                print("qwe")
            if l1.next != None:
                l1 = l1.next
            if l2.next != None:
                l2 = l2.next
        
