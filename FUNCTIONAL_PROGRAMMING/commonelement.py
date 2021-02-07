def common_elements(list_1, list_2):
  a_set = set(list_1)
  b_set = set(list_2)
  if (a_set & b_set):
    print(a_set & b_set)
  else:
    print("No common elements between the two lists")

list_one = [32, 34, 56, 65, 89, 70, 80]
list_two = [1, 2, 0, 67, 80, 89, 56]

common_elements(list_one, list_two)

