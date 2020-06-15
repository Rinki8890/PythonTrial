def reverse_recursion(s):
    if len(s) == 1:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]

print(reverse_recursion("aks"))
print(2*'a')