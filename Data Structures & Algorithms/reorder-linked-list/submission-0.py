# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1,p2= head, head
        while p2!=None and p2.next!=None and p2.next.next!=None:
            p1=p1.next
            p2=p2.next.next
        
        node=p1.next
        prev=None
        while node!=None:
            next_node = node.next
            node.next = prev
            prev= node
            node = next_node
            
        start=head
        while start!=p1:
            next_node = start.next
            start.next = prev
            node = prev.next
            prev.next = next_node
            prev=node
            start = next_node
        start.next=prev

