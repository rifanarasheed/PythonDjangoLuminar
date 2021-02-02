# define : to create empty set you have to use set()
# insertion order is not preserved
# set does not support indexing
# empty {} is taken as dictionary
# duplicate are not allowed

st = {10,11,"hello",12,13}
st2 = {50,60}
st.update(st2)
print(st)