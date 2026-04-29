# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        follow = head
        if head != None:
            while  follow.next != None:
                save = follow.next # Save the next element in the first list 
                print(follow.val)
                print(save.val)
                follow.next = tail # Assign next to the tail of the array
                tail = follow 
                follow = save # set follow to the next element in the linked list
            save = follow.next # Save the next element in the first list 
            follow.next = tail # Assign next to the tail of the array
        return follow
        