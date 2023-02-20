# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']
    stack = []
    closing_stack = []
    opening_stack = []

    for i, c in enumerate(code):
        if c in opening_brackets:
            stack.append(c)
            opening_stack.append(i + 1)
        elif c in closing_brackets:
            if not stack:
                return i + 1
            if closing_brackets.index(c) == opening_brackets.index(stack[-1]):
                stack.pop()
                closing_stack.pop()
            else:
                return i + 1
        else:
            continue




def main():
    text = input()
    mismatch = find_mismatch(text)
    if stack:
        return closing_stack[0]
    elif opening_stack:
        return opening_stack[0]
    else:
        return "Success"


if __name__ == "__main__":
    main()
