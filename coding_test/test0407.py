# 2問目
class Solution:
    def addTwoNumbers(self, l1, l2, up=0):
        val = l1.val + l2.val + up
        up = val // 10
        result = ListNode(val % 10)
        
        if (l1.next != None or l2.next != None or up != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, up)
        return result
        
        