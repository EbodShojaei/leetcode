# LC 1472
# see: https://leetcode.com/problems/design-browser-history/description/


class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        # clears up forward history
        node = ListNode(url)
        self.current.next = node
        node.prev = self.current
        self.current = node

    def back(self, steps: int) -> str:
        # i = 0
        # curr = self.current
        # prev = None
        # while curr:
        #     if i == steps:
        #         self.current = curr
        #         return curr.val
        #     prev = curr
        #     curr = curr.prev
        #     i += 1
        # self.current = prev
        # return prev.val
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        # i = 0
        # curr = self.current
        # prev = None
        # while curr:
        #     if i == steps:
        #         self.current = curr
        #         return curr.val
        #     prev = curr
        #     curr = curr.next
        #     i += 1
        # self.current = prev
        # return prev.val
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
