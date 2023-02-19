# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    mismatch_pos = None
    for i, next in enumerate(text):
        # enumerate nodod gan kārtas numur, gan simbolu
        if next in "([{":
            # Process opening bracket, write your code here
            #jāpievieno struktūras
            

            opening_brackets_stack.append(Bracket(next,i+1))
            

        if next in ")]}":
            # Process closing bracket, write your code here
            #empty != (empty nebūs)
            #Matchc are matching
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
        if opening_brackets_stack:
            return opening_brackets_stack[0].position
        return "Success"
            
        


def main():
    text = input()
    if text[0] == "I":
        text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    input("I")
    main()
    main()
