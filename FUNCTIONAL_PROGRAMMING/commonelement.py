def common_elements(list_1, list_2):
  a_set = set(list_1)
  b_set = set(list_2)
  if (a_set & b_set):            # or intersection can be used
    print(a_set & b_set)
  else:
    print("No common elements between the two lists")

list_one = [1,2,3,4,5,6,7,8,9]
list_two = [2,4,6,8]

common_elements(list_one, list_two)

