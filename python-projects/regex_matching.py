import re
with open('logfile.txt') as f:
    mylogs = f.read()
    pattern = r'.*([45][0-9][0-9]\s).*'
    match = re.search(pattern, mylogs)
    # If-statement after search() tests if it succeeded
    if match:
      print('found', match.groups()) ## 'found word:cat'
    else:
      print('did not find')
