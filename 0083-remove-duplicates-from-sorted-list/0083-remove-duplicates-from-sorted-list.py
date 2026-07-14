# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        prev=None
        seen=set()
        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                prev=curr
            else:
                prev.next=curr.next
            
            curr=curr.next
        return head
        