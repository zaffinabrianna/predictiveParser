# Brianna Zaffina
# CPSC 323
# Professor Venkatesh
# 21 April 2025

# Creating Predictive Parsing Table:
parseTable = {
    'E':{
        'a':['T', "E'"],
        '(':['T', "E'"]
        },
    "E'":{
        '+':['+', 'T', "E'"],
        '-':['-', 'T', "E'"],
        ')':['ε'],
        '$':['ε']
        },
    'T':{
        '(':['F', "T'"],
        'a':['F', "T'"]
        },
    "T'":{
        '*':['*', 'F', "T'"],
        '/':['/', 'F', "T'"],
        '+':['ε'],
        '-':['ε'],
        '(':['ε'],
        '$':['ε']
        },
    'F':{
        '(':['(', 'E', ')'],
        'a':['a']
        }
}

states = ['a', '+', '-', '*', '/', '(', ')', '$']
terms = ['E', 'T', "E'", "T'", 'F', 'ε']

def parse(inputs):
    inputs = inputs.replace(" ", "").strip()
    
    for char in inputs:
        if char not in states and char not in terms:
            print("String is Invalid.\n")
            return
        
    stack = ['$', 'E']
    index = 0

    print(f"{'Stack':<30} {'Input':<30} Action")
    while len(stack) > 0:
        top = stack[-1]
        currentInput = inputs[index]

        print(f"{''.join(stack):<30} {inputs[index:]:<30}", end=' ')

        if top == currentInput:
            print(f"Match '{top}'")
            stack.pop()
            index += 1
        elif top in states:
            print(f"Error: Unexpected Terminal '{top}'")
            return
        elif top in parseTable and currentInput in parseTable[top]:
            rule = parseTable[top][currentInput]

            print(f"Apply {top} -> {' '.join(rule)}")

            stack.pop()

            if rule[0] != 'ε':
                for symbol in reversed(rule):
                    stack.append(symbol)
        else:
                print(f"Error: No Rule For {top} with input {currentInput}")
                print(f"Output: String is Invalid.\n")
                return
            
    if index == len(inputs):
        print("String is Valid\n")
    else:
        print("String is Invalid\n")

def main():
    test = [
        "(a +a)*a$",
        "a*(a/a) $",
        "a(a+a) $:"
    ]

    for i, s in enumerate(test, 1):
        print(f"\nTest Case {i}: {s} ---")
        parse(s)

if __name__ == "__main__":
    main()