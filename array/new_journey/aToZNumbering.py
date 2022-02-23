# The ord() function returns an integer representing the Unicode character. For example, 'a' in Unicode character is 96, '
# 'A' is 66, 'b' is 97 and 'c' is 98.
# so to mape a to 1, b to 2, z to 26 (minus 96 from ord for small lettes , for capital minus 64)

l = 'Z'
print(ord(l)-64)