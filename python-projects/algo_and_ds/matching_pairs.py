"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=559324704673058&c=1062635970997589&ppid=454615229006519&practice_plan=0

matching pairs

this means that the minimum number is  after removing i and j how many are left.

so basically to find the ones which are not matching and try to match them.

is there something that can be matched and they would be perfect.

brute force is n3

==============================

this looks like dynamic programming. can try that

adcb
abcd

    a   b   c   d
a   _
b   1   _
c   0   1   _
d   1   4    1   _   

========================

for each point what is the similarity

there are two types of letters, same and not same. no point in trying to change the same ones as they are already controbuting. no need to touch them.
for the remainig ones atleast try to make one of them the same.

not same = for the ones that are not the same check if there are any that you can match with the same letter. if for the same set you fine it loops back then you can add 2 and declare success.
thats the maximum that can happen
else just add 1 aand hen return

special case. if all are the same then loop then get the count of the letters and see if there are any that is more than once. then you can maintain the count. else you will have to reduce by 2.

"""


import itertools

def get_diff(s, t):
    return sum(i==j for i, j in zip(s, t))

def brute_force(s, t):
    size = len(s)
    max_val = 0
    for ch1 in range(size):
        for ch2 in range(ch1+1, size):
            s1 = s[:ch1] + s[ch2] + s[ch1+1:ch2] + s[ch1] + s[ch2+1:]
            diff = get_diff(s1, t)
            # print(s1, t, diff)
            max_val = max(diff, max_val)
    return max_val

s = "abcd"
t = "adcb"
print('brute_force', s, t, brute_force(s, t))

# s = 'mno'
# t = 'mno'
# print(brute_force(s, t))


def all_equal(s, t):
    return all(i==j for i, j in zip(s, t))

def run(s, t, non_matchin):
    found_one = False
    found_two = False
    for this, index in non_matchin.items():
        other = t[index] # d
        if other in non_matchin: # true
            found_one = True
            other_indx = non_matchin[other] # 3
            other_1 = t[other_indx] # 
            if other_1 == this:
                found_two = True
                return found_two, found_one
    return found_two, found_one

from collections import Counter

def case1(s, t):
    counts = Counter(s)
    if any(c > 1 for c in counts.values()):
        return len(s)
    else:
        return len(s) - 2


def case2(s, t):
    non_matchin = {}
    for i, (ch1, ch2) in enumerate(zip(s, t)):
        if ch1 != ch2:
            non_matchin[ch1] = i
    # print(non_matchin)
    found_two, found_one = run(s, t, non_matchin)
    # print(found_two, found_one)
    if found_two:
        return len(s) - len(non_matchin) + 2
    if found_one:
        return len(s) - len(non_matchin) + 1
    return len(s) - len(non_matchin)



def v1(s, t):
    if all_equal(s, t):
        return case1(s, t)
    else:
        return case2(s, t)

s = "abcd"
t = "adcb"
print('v1', s, t, v1(s, t))


s = "mno"
t = "mno"
print('v1', s, t, v1(s, t))