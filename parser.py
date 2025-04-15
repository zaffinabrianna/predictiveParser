# Brianna Zaffina
# CPSC 323
# Professor Venkatesh
# 21 April 2025

# Creating Predictive Parsing Table:
parseTable = {
    'E':{
        'a':['T', "E'"], # FIRST of E (for E->TE')
        '(':['T', "E'"]  
        },
    "E'":{
        '+':['+', 'T', "E'"], # FIRST of E' (for E' -> T+E')
        '-':['-', 'T', "E'"], # FIRST of E' (for E' -> T-E')
        ')':['ε'],            # FIRST OF E' (for E' -> ε)
        '$':['ε']             # FIRST OF E' (for E' -> ε)
        },
    'T':{
        '(':['F', "T'"],      # FIRST of T (for T -> FT')
        'a':['F', "T'"]       # FIRST of T (for T -> FT')
        },
    "T'":{
        '*':['*', 'F', "T'"], # FIRST of T' (for T' -> F*T')
        '/':['/', 'F', "T'"], # FIRST of T' (for T' -> F/T')
        '+':['ε'],            # FIRST of T' (for T' -> ε)
        '-':['ε'],            # FIRST of T' (for T' -> ε)
        ')':['ε'],            # FIRST of T' (for T' -> ε)
        '$':['ε']             # FIRST of T' (for T' -> ε)
        },
    'F':{
        '(':['(', 'E', ')'],  # FIRST of F (for F -> (E))
        'a':['a']             # FIRST of F (for F -> a)
        }
}

# All the possible non-terminals (states) and terms in the parser
terms = ['a', '+', '-', '*', '/', '(', ')', '$']
states = ['E', 'T', "E'", "T'", 'F', 'ε']

# Function to take input string and translate it onto 
def parse(inputs):
    inputs = inputs.replace(" ", "").strip() # Gets rid of any whitespace in the code
    
    # Checking to see if all characeters in the string have valid terms and states
    for char in inputs:  
        if char not in terms and char not in states:
            print("---------------------------------RESULT------------------------------------------")
            print("String is not Accepted/Invalid as there is/are Invalid char(s).\n")  # If it doesn't, returns invalid message since it does not belong to the parser
            return
    
    # Starts Parsing Stack: Stack is FILO so $ will mark the end of the stack and E starts it 
    stack = ['$', 'E']
    index = 0 # Index to start at the first character of the string and go through it one by one

    print(f"{'Stack':<20} {'Input':<20} Action") # Header for output

    # While the stack still has items within it
    while len(stack) > 0:
        top = stack[-1] # Negative indexing for the LAST item in stack which is the top
        currentInput = inputs[index] # Set current index to the current character we are at (in index) in the while loop

        print(f"{''.join(stack):<20} {inputs[index:]:<20}", end=' ') # Output the Current Stack and the Current state of the Index

        if top == currentInput: # If the top is the same as the current index
            print(f"Match '{top}'") 
            stack.pop() # Pop the item in the stack
            index += 1 # Move index by one
        elif top in terms: # Checks to see if top item is a term and not a non-term item
            print("\n---------------------------------RESULT------------------------------------------")
            print(f"String is not Accepted/Invalid. The Term '{top}' is Unexpected.")
            return
        elif top in parseTable and currentInput in parseTable[top]: 
            rule = parseTable[top][currentInput] # Checks to see if theres a rule for top and the current input

            print(f"Apply {top} -> {' '.join(rule)}") # Apply (top -> rule)

            stack.pop() # Pop the item that we just applied the rule to

            if rule[0] != 'ε': # If the item isnt epsilon
                for symbol in reversed(rule): 
                    stack.append(symbol) # Put the items reversed into the stack since stack is LIFO
        else:
                print("\n---------------------------------RESULT------------------------------------------")
                print(f"String is not Accepted/Invalid as There is no Rule for '{top}' with input '{currentInput}'.\n")
                return
    print("---------------------------------RESULT------------------------------------------")
    if index == len(inputs): # Once the index is the same length of our original string, inputs, then we have gone through it all and can determine if its valid or not
        print("String is Accepted/Valid.\n") 
    else:
        print("String is not Accepted/Invalid.\n")

def main():
    #Test cases to test parser
    test = [
        "(a +a)*a$",
        "a*(a/a) $",
        "a(a+a) $",
        "(a+a) e $"
    ]

    for testNum, stringTests in enumerate(test, 1): # Increase the test number and go to the next string
        print(f"\nTest Case {testNum}: {stringTests}") # Output these test variables
        print("---------------------------------------------------------------------------------")
        parse(stringTests) # Parse the current string test were on


if __name__ == "__main__":
    main()