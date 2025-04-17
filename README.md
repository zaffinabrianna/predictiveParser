# predictiveParser

## Setup Instructions
1. Download the parser.py file and put it into your IDE, ensuring you have a Python debugger installed. 
2. The main() has all of the test strings, so all you have to do is run the code in your IDE, and it will provide the given output.
3. If you would like to add different tests, edit the test list in main().
   
             After "(aa)" add:
   
             "(aa)",
   
             "YOUR TEST CASE"
   
             ]

## Code Explanation
My code uses a map/dictionary to create a parsing table using the table provided in the assignment. 

It uses a function parse(inputs) to take the inputs of a list of strings and parse through them. It determines the rules to use on a specific terminal based on the previously added parsing table. Using a stack, we pop through to get each char in a string using an index. Through each step, we are given the state of the stack, the state of the input, and the actions used while parsing.


##  Dependencies and Version Used
I used the most up-to-date version of python. No extra modules or libraries were added.

## Reflection
Inherently, figuring out how to logically put a parsing table and make a parser into code was difficult. 
