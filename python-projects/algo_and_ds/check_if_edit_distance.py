"""
edit distance check

usig the two pointer and keepong count of the number of edits

complexity: O(n+m)

"""

def checking_no_edits(s1, s2):
    # an initial check to avoid the loop if possible
    if abs(len(s1) - len(s2)) > 1:
        return False
    edits = 0
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        # best case. both are the same
        if s1[i] == s2[j]: 
            i += 1
            j += 1
        else: # 00, 
            if i + 1 < len(s1) and s1[i + 1] == s2[j]: #
                # update only pointer for s1
                i += 1 
                edits += 1
            elif j + 1 < len(s2) and s1[i] == s2[j + 1]:
                # update only pointer for s2
                j += 1
                edits += 1
            else:
                # update both the pointers
                i += 1
                j += 1
                edits += 1
        # do an interim check to see if can be exited early
        if edits > 1:
            return False

    # remaining checks    
    if i < len(s1) and len(s1) - 1 - i:
        return False
    if j < len(s2) and len(s2) - 1 - j:
        return False
    return True


print(checking_no_edits('pale', 'ple'))
print('#'*50)
print(checking_no_edits('pale', 'bake'))
print('#'*50)
print(checking_no_edits('pale', 'bale'))
print('#'*50)
print(checking_no_edits('pale', 'pl'))