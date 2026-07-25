a = 30
b = 20
c = 40

if a > b:
    print("Print ", a)
else:
    print("Print ", b)

# Another Way
if a > b: print("Print ", a)
else: print("Print ", b)

# If-Else condition check with 3 variables
if a > b and a > c:
    print("Print ", a)
elif b > a and b > c:
    print("Print ", b)
else:
    print("Print ", c)

# Pass statement => It checks IF condition, if satisfies then print the value else go to "ELSE" and pass the statement
# It actually checks the condition internally in "pass" but doesn't allow to print. It simply pass to next statement.
# pass - case 1
if a > b:
    print("CASE1-A")
else:
    pass

# pass - case 2
if a > b and a > c:
    print("CASE2-A")
elif b > a and b > c:
    pass
else:
    pass

