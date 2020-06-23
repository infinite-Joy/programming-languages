def integer_check(x, y, z):
  """
  @param x: first digit
  @param y: sec digit
  @param z: third digit

  @return bool
  """
  #print("checking integer check")
  return 100*x + 10*y + z <= 255

def validateIP_rec(ip, N, n, x=0, y=0, z=0, dot_cnt=0, last_dot=0):
  """
  @param ip: str
  @param N: total len
  @param n: curr index
  @param x: first digit
  @param y: sec digit
  @param z: third digit
  @param last_dot: last dot time

  @return: bool
  """

  #print(ip, N, n, x, y, z, dot_cnt, last_dot)
  if dot_cnt > 3:
    return False
  if n >= N:
    return True
  try:
      int(ip[n])
  except ValueError:
      if ip[n] != ".":
          return False
  if last_dot == 0:
    z = ip[n]
    if z == '.':
      return False
    z = int(z)
    last_dot += 1
    return validateIP_rec(ip, N, n+1, x, y, z, dot_cnt, last_dot)
  if last_dot == 1:
    y = z
    z = ip[n]
    if z == ".":
      dot_cnt += 1
      last_dot = 0
      return validateIP_rec(ip, N, n+1, x, y, 0, dot_cnt, last_dot)
    z = int(z)
    # print(z)
    last_dot += 1
    # print(last_dot)
    return validateIP_rec(ip, N, n+1, x, y, z, dot_cnt, last_dot)
  if last_dot == 2:
    x = y
    y = z
    z = ip[n]
    #print(z)
    if z == ".":
      dot_cnt += 1
      last_dot = 0
      #print()
      return validateIP_rec(ip, N, n+1, x, y, 0, dot_cnt, last_dot)
    z = int(z)
    #print("last dot 2", x, y, z)
    if integer_check(x,y,z) is True:
      x, y, z = 0, 0, 0
      dot_cnt += 1
      last_dot += 1
      #print(n,x,y,z,dot_cnt,last_dot)
      return validateIP_rec(ip, N, n+1, x, y, z, dot_cnt, last_dot)
  if last_dot == 3:
    #print("last dot is 3", last_dot, ip[n], x, y, z, dot_cnt, last_dot)
    if ip[n] == ".":
      last_dot = 0
      return validateIP_rec(ip, N, n+1, x, y, z, dot_cnt, last_dot)
    else:
      return False

    return False

  return False # if number of values are more than 3 digits

def validateIP(ip):
  return validateIP_rec(ip, len(ip), 0)



print(validateIP("0.0.0.0"))
print(validateIP("192.168.0.1"))
print(validateIP("1.2.3.0x1"))
