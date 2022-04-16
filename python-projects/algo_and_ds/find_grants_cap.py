"""
grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

[2, 47, 47, 47, 47]

cap out: return

input: arr[int]
output: int

[] => 0

trivial: [a] => min(a, newbudget)

general:
  total_sum ; obj is to make total sum <= new budget.
  sort the list in increasing: 2 50 100 120 1000
  for loop: start from the left
    cap amount is the previous val 2 50 100 120 120
    
2 50 100 120 1000
              _
2 50 100 120 120 then check if the sum is less than new budget
          _
2 50 100 100 100
      _
2 50 50 50 50
  _

.... 2 | 2 2 2 2 2 sum is less than new budget.
     _
     
(new budget - curr sum) / len(arr) - pointer


=============================

sort the list in increasing:

loop and start from the left

[2, 47, 47, 47, 47]

2 50

============================


heaps: O(n)

"""



def find_grants_cap(grantsArray, newBudget):
  avg_grant = float(newBudget)/len(grantsArray)
  
  sortedArr = sorted(grantsArray)
  for i in range(len(sortedArr)): 
    if sortedArr[i] > avg_grant: 
      diff = avg_grant - sortedArr[i]
      break 
      
  return avg + diff/(len(grantsArr)-i) 
  

strat to see this as a difficult problem.
things are not very precise
make this simple yet precise.
this makes things to fix the problem
we need the 100% of the idea
play around with the example.