# lc1700 - number of students unable to eat lunch
# see: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/submissions/1686842035/

from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 is circular sandwich
        # 1 is square sandwich

        # number of sandwiches equal to number of students
        # sandwiches placed in a queue (LIFO), not a stack (FIFO)
        # if student at front of queue prefers sandwich, take it and leave
        # if not, student goes to back of queue
        # continue until none of the queue students want to take the top sandwich
        # thus number of students unable to eat
        skipped = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students:
            if skipped == len(students):
                return len(students)
            student = students.popleft()
            sandwich = sandwiches.popleft()
            if student != sandwich:
                students.append(student)
                sandwiches.appendleft(sandwich)
                skipped += 1
            else:
                skipped = 0

        return len(students)
