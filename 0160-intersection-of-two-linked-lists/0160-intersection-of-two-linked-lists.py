# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headASet = set()
        nodeA = headA
        while nodeA:
            headASet.add(nodeA)
            nodeA = nodeA.next
        nodeB = headB
        while nodeB:
            if nodeB in headASet:
                return nodeB
            nodeB = nodeB.next
        return None