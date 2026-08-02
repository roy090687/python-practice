def is_balanced(input):
    stack = []
    for ch in input:
        if ch in ('(', '{', '['):
            stack.append(ch)
        elif ch in (')', '}', ']'):
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (ch == ')' and top != '(') or \
                    (ch == '}' and top != '{') or \
                    (ch == ']' and top != '['):
                return False

    # Finally if stack is empty, all brackets matched successfully.
    n = len(stack)
    if n == 0:
        return True
    else:
        return False


input1 = "abc((12))45T{[se]}"
input2 = "([)]"
input3 = "((())"
input4 = "())"
input5 = "er2({550}[tr==0(fr)]78"
input6 = "({[()]})"

print(f"{input1} --> {is_balanced(input1)}")
print(f"{input2} --> {is_balanced(input2)}")
print(f"{input3} --> {is_balanced(input3)}")
print(f"{input4} --> {is_balanced(input4)}")
print(f"{input5} --> {is_balanced(input5)}")
print(f"{input6} --> {is_balanced(input6)}")

