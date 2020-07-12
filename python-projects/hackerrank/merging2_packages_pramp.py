def get_indices_of_item_wights(arr, limit):
  """
  get the indices

  Args:
    arr (List[int]): the list of the package weights
    limit (int): the limit of the weights

  Returns:
    List[int]: the list of the indices
  """
  mapping = {}
  for i, item in enumerate(arr):
    if item in mapping:
      return [i, mapping[item]]
    else:
      diff = limit - item
      mapping[diff] = i

  return []


arr = [4, 6, 10, 15, 16];limit = 21
print(get_indices_of_item_wights(arr, limit))
