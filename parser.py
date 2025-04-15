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
        '+':['T', '+', "E'"],
        '-':['T', '-', "E'"],
        ')':['ε'],
        '$':['ε']
        },
    'T':{
        '(':['F', "T'"],
        'a':['F', "T'"]
        },
    "T'":{
        '*':['F', '*', "T'"],
        '/':['F', '/', "T'"],
        '+':['ε'],
        '-':['ε'],
        '(':['ε'],
        '$':['ε']
        },
    'F':{
        '(':['(', 'E', ')'],
        'a':['F']
        }
}

states = ['a', '+', '-', '*', '/', '(', ')', '$']

def main():
    print("bruh")
    


if __name__ == "__main__":
    main()