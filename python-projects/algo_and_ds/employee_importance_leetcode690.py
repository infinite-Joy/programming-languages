from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from functools import reduce
class Solution:
    def dfs(self, emp, emps):
        print(emp)
        print(emp.subordinates)
        if emp is not None:
            return reduce(lambda s, sub: s + self.dfs(self.search(emps, sub), emps), emp.subordinates, emp.importance)
    def search(self, emps, id):
        for emp in emps:
            if emp.id == id:
                return emp
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        starting_emp = self.search(employees, id)
        return self.dfs(starting_emp, employees)

# test code
arr = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
employees = []
for item in arr:
    emp = Employee(*item)
    employees.append(emp)
sol = Solution()
print(sol.getImportance(employees, 1))
