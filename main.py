# python3
BRACKETS_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
}

def are_matching(left, right):
    return BRACKETS_MAP.get(left) == right

def find_mismatch(text):
    stack = []
    for i, char in enumerate(text, start=1):
        if char in BRACKETS_MAP:
            stack.append((char, i))
        elif char in BRACKETS_MAP.values():
            if not stack:
                return i
            last_bracket, _ = stack.pop()
            if not are_matching(last_bracket, char):
                return i
    if stack:
        return stack[0][1]
    return 'Success'

def main():
    text = input()
    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

if _name_ == "_main_":
    main()
