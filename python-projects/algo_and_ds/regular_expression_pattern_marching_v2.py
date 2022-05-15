"""

input: string
pattern: string. this will have . and *
output: boolean

test cases:
input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true


brute force:

 loop over the pattern:
  ch[ch] => match the pattern with the text value.
  ch[.] => match the pattern and incr 1 for both text and pattern
    .* => 
    .ch => go over to the next ch and check
  ch[*] => choose ch 
    or not choose ch
  
input:  text = "acd", pattern = "ab*c."
        text = 'cd' pattern b*c: [text: cd, p: b*c]
          choose b: false
          not choose b: 
        text: 'cd' pattern 'c.'.
        text: 'd' patter '.': true
        
input:  text: 'cde' pattern 'c.*'.
        text: 'def' pattern '.*f'
            choose
       ef,.*f     def,f
  f,.*f     ef,f 
null,.*f; f,f


complexity: len(pattern)**(len(text))
space: len(pattern)**(len(text))


dry run text = "acd", pattern = "ab*c."


"""

def star_helper(text, pattern):
  if text[0] == pattern[0]:
    return is_match_rec(text[1:], pattern) # d,.
  else:
    return False
    
def is_match_rec(text, pattern):
  print(text, pattern)
  if text=="" and pattern =='':
    return True
  if text and pattern=='':
    return False
  if text=='' and pattern:
    if pattern=='.*':
      return True
    else:
      return False
  # base case
  if len(pattern) == 1:
    if len(text) > 1:
      return False
    if pattern == '.':
      return True
    else:
      return pattern == text
  else:
    # chch
    if pattern[0] not in ['.', '*'] and pattern[1] not in ['.', '*']:
      if pattern[0] == text[0]: # acd,ab*c.
        return is_match_rec(text[1:], pattern[1:]) # cd,b*c.
      else:
        return False
    # ch.
    elif pattern[0] not in ['.', '*'] and pattern[1] in ['.']:
      if pattern[0] == text[0]:
        return is_match_rec(text[1:], pattern[1:]) # bc,.c
      else:
        return False
    # .ch
    elif pattern[0] in ['.'] and pattern[1] not in ['.', '*']:
      return is_match_rec(text[1:], pattern[1:]) # c,c
    # ch[*]
    elif pattern[0] not in ['.', '*'] and pattern[1] in ['*']:
      return is_match_rec(text, pattern[2:]) or star_helper(text, pattern) # left cd,cd. right
    # .*
    elif pattern[0] in ['.'] and pattern[1] in ['*']:
      return is_match_rec(text, pattern[2:]) or is_match_rec(text[1:], pattern)
    else:
      print('something')



def is_match(text, pattern):
  return is_match_rec(text, pattern)

    

text = "abbdbb"
pattern = 'ab*d'
print(is_match(text, pattern))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

