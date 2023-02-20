# python3

class Bracket:
    def _init_(self, char, position):
        self.char = char
        self.position = position


def are_matching(left, right):
    matching_pairs = {"(": ")", "[": "]", "{": "}"}
    return left in matching_pairs and right == matching_pairs[left]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i))
        elif next_char in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack[-1]
            if not are_matching(top.char, next_char):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"


def main():
    text = input()
    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)


if _name_ == "_main_":
    main()
    
