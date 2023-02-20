# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
   opening_brackets = "[{("
    closing_brackets = "]})"
    stack = []
    for i, char in enumerate(code):
        if char in opening_brackets:
            stack.append((char, i))
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack[-1][0]) != closing_brackets.index(char):
                return i + 1
            stack.pop()
    if stack:
        return stack[0][1] + 1

    opening_brackets = opening_brackets + closing_brackets
    closing_brackets = ""
    stack = []
    for i, char in enumerate(code):
        if char in opening_brackets:
            stack.append((char, i))
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack[-1][0]) != opening_brackets.index(char) - len(opening_brackets) // 2:
                return i + 1
            stack.pop()
   



def main():
    text = input()
    mismatch = find_mismatch(text)
    if stack:
       return stack[0][1] + 1
    else:
        return "Success"


if __name__ == "__main__":
    choice = input("Enter F to choose test files or I to input the brackets: ")
    if choice == "F":
        file_name = input("Enter test file name: ")
        with open(file_name, 'r') as f:
            for line in f:
                text = line.strip()
                print(find_mismatch(text))
    elif choice == "I":
        text = input("Enter the brackets: ")
        print(find_mismatch(text))
