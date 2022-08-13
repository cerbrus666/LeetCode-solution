Approach name: Stack

1. Initialise a stack
2. Initialise a mapping, with closing parantheses ("]", "}", ")") as key and opening parantheses as values
3. Loop through the char in inputted string, s
4. If char is opening bracket (values), then append them in stack
5. If char is closing bracket (keys) and also stack is not empty, then pop up the stack (assigned to top_element)
6. If char is closing bracket (keys) but the stack is empty, then assign dummy variable ('#') to top_element
7. Then check if the pop up parantheses is equal to the current char mapping (closing bracket of current char being looped)
8. If not equal, return False, the whole string inputted is invalid
9. Otherwise keep looping, if at the end of loop the stack is empty, then returning 'not stack' will result in True // valid parantheses

Notes:

- Stacks are Last In First Out
