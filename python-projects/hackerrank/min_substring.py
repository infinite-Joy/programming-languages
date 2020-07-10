from collections import deque


def get_shortest_unique_substring(arr, fullstr):
  if fullstr == "":
    return ""
  if len(fullstr) == 1 and len(arr) == 1 and arr[0] == fullstr:
    return fullstr
  fullset = set(arr)
  i = 0
  j = 0
  this_set = {}
  sub_string = deque([])
  found = False
  min_len_str = fullstr
  min_len = len(fullstr)

  while j <= len(fullstr):
      #__import__('pudb').set_trace()

      if len(fullset) == len(this_set):
        found = True

        # do the checks
        min_len = min(len(min_len_str), len(sub_string))
        if min_len == len(sub_string):
          min_len_str = sub_string

        #update the substring
        ch = fullstr[i]
        if ch in this_set:
          this_set[ch] -= 1
          if this_set[ch] == 0:
            del this_set[ch]
        if len(sub_string):
          sub_string.popleft()
        i += 1

      elif j < len(fullstr):
        ch = fullstr[j]
        sub_string.append(ch)
        if ch in fullset:
          if ch in this_set:
            this_set[ch] += 1
          else:
            this_set[ch] = 1
        j += 1
      else:
        j += 1


  if found is False:
    return ""

  return "".join(min_len_str)


print(get_shortest_unique_substring(['x','y','z'], "xyyzyzyx")) # answer zyx
print(get_shortest_unique_substring(["A","B","C"], "ADOBECODEBANCDDD")) # answer BANC


"""

create a map from the elements in the array

create a 2 pointr method.

keeping i constant move j till all the elements are covered. this can be done by len set is not set

once matched move i and start again and keep to see.

if at first only j goes to the end then return ""

complexity  is O(n+k)

"""

