class InfixToPostfixConverter:
  
    def __init__(self):
      
 
       
        self.operators = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3
        }
 
        
        self.stack = []
 
       
        self.postfix_expression = ""
 
    def convert_to_postfix(self, infix_expression: str) -> str:
     
 
      
        if not infix_expression:
            raise ValueError("Infix expression cannot be empty.")
 
      
        self.stack = []
        self.postfix_expression = ""
 
       
        for char in infix_expression:
            
            if char.isalnum():
                self.postfix_expression += char
           
            elif char == "(":
                self.stack.append(char)
           
            elif char == ")":
                while self.stack and self.stack[-1] != "(":
                    self.postfix_expression += self.stack.pop()
               
                if self.stack and self.stack[-1] == "(":
                    self.stack.pop()
            
            elif char in self.operators:
                while self.stack and self.stack[-1] != "(" and self.operators[char] <= self.operators.get(self.stack[-1], 0):
                    self.postfix_expression += self.stack.pop()
                self.stack.append(char)
 
        
        while self.stack:
            self.postfix_expression += self.stack.pop()
 
        return self.postfix_expression
 
 

 

converter = InfixToPostfixConverter()
 

infix_expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"
postfix_expression = converter.convert_to_postfix(infix_expression)
print(f"The postfix expression for '{infix_expression}' is '{postfix_expression}'.")