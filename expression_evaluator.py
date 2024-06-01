from LLStack import LLStack
#Darryl Eason U00885025 
def token_class(token): #Identify token 
     if token.upper().isupper() == True: #Sets all letters (if applicable) in token to uppercase and checks to see if they are uppercase, if yes, then there is a letter in the token and is therefore invalid.
        raise ValueError("Invalid Token")
     elif token == "^":
        return "Exponent"
     elif token == "(":
        return "Open"
     elif token == ")":
        return "Closed"
     elif token == "+":
        return "Addition"
     elif token == "-":
        return "Subtraction"
     elif token == "*":
        return "Multiplication"
     elif token == "/":
        return "Division"
     elif token.isnumeric() == True: #If token is all numbers, it is an integer
        return "Integer"
     elif token.find("-") != -1 and token.find(".") == -1: #if there is a - and no . , then remove the - sign. If it is all numbers, then it is an integer (negative)
        if (token.replace("-","",1)).isnumeric() == True:
           return "Integer"
     elif token.find(".") != -1: #If there is a . , then it is a float
        return "Float"
     elif token.find(".") != -1 and token.find("-") != -1: #If there is a . and a -, it is a negative float
        return "Float"
     else:
        return ValueError("Invalid Token")
     
def precedence(token): #Set precedence according to operator.
   if token == "(":
    return 1
   elif token == "+":
    return 2
   elif token == "-":
     return 2
   elif token == "*":
     return 3
   elif token == "/":
     return 3
   elif token == "^":
      return 4

def exponential(base, n): #Find base raised to n power recursively
   if n == 0:
      return 1
   else:
      if n > 0:
         n = n - 1
         v = base * exponential(base, n)
      elif n < 0:
         n = n + 1
         v = exponential(base, n) / base
      return v

   
 

def infix_to_postfix(infix):
    infixstack = LLStack() #Create stack
    #Algorithm 1: Check for Well-formed Expression
    for x in range(len(infix)): #Iterate over expression
        if infix[x] == "(": # If there is an op. parenthesis push onto stack
            infixstack.push(x)
        elif infix[x] == ")": #If there is a cl. parenthesis attempt to pop; if unable to pop, catch error 
            try:
                infixstack.pop()
            except IndexError as error:
                return(f"{error} (Opening Parenthesis Missing.)")
    if infixstack.is_empty() != True: #If the stack isn't empty then return error
        return ValueError("Expression is not well-formed (Unclosed Parenthesis)")
    #Algorithm 2: Convert to postfix
    postfix = "" #create postfix variable to return
    infix = infix.split() # Split infix into seperate tokens
    for x in range(len(infix)):
        if token_class(infix[x]) == "Integer" or token_class(infix[x]) == "Float":  #If token is int/float, add to postfix variable
            postfix += infix[x] + " "
        elif infix[x] == "+" or infix[x] == "-" or infix[x] == "/" or infix[x] == "*" or infix[x] == "^": #if x is operator
           while infixstack.is_empty() != True and precedence(infix[x]) <=  precedence(infixstack.head.value): #while stack isn't empty and token precedence is greater than the head
              postfix += infixstack.head.value + " " #add to postfix and then pop
              infixstack.pop()
           infixstack.push(infix[x]) #push once conditions have been met
        elif infix[x] == "(": #if token is op parenthesis push onto stack
           infixstack.push(infix[x])
        elif infix[x] == ")": #if token is closed parenthesis
         try:
           while infixstack.head.value != "(": #add to postfix and pop head while head isn't op parenthesis
              postfix += infixstack.head.value + " "
              infixstack.pop()
         except:
           if infixstack.is_empty == True: #if stack is empty, raise error
              raise ValueError("Parenthesis balancing error")
         infixstack.pop() #Once ( is found, pop it
        else:
           raise ValueError("Invalid Token") #Catch invalid token
    for x in range(infixstack.depth()): #Empty out stack and add to postfix
       if infixstack.head.value == "(":
          raise ValueError("Parenthesis balancing error")
       postfix += infixstack.head.value + " " 
       infixstack.pop()
    return postfix

       

def evaluate(postfix):
   postfix = postfix.split() #split into tokens
   op1 = '' #operand 1
   op2 = '' #operand 2
   postfixstack = LLStack()
   for x in range(len(postfix)):
      if token_class(postfix[x]) == "Integer": #if token is int, push onto stack as int
         postfixstack.push(int(postfix[x]))
      elif token_class(postfix[x]) == "Float": #same as above but for float
         postfixstack.push(float(postfix[x]))
      elif token_class(postfix[x]) == "Addition" or token_class(postfix[x]) == "Subtraction" or token_class(postfix[x]) == "Multiplication" or token_class(postfix[x]) == "Division" or token_class(postfix[x]) == "Exponent":
        #^ if above is operator
        try:
         op2 = postfixstack.head.value #set operands and pop them from stack
         postfixstack.pop()
         op1 = postfixstack.head.value
         postfixstack.pop()
         #do math on them
         if token_class(postfix[x]) == "Addition":
            postfixstack.push(op1 + op2)
         elif token_class(postfix[x]) == "Subtraction":
            postfixstack.push(op1 - op2)
         elif token_class(postfix[x]) == "Multiplication":
            postfixstack.push(op1 * op2)
         elif token_class(postfix[x]) == "Division":
            postfixstack.push(op1 / op2)
         elif token_class(postfix[x]) == "Exponent":
            postfixstack.push(op1 ** op2)
        except:
           raise IndexError("Too few operands") #catch errors
      else:
         raise ValueError("Invalid Token")
   return postfixstack.head.value


infix = input("Enter an expression to evaluate (X to exit):")
while infix != "X":
   try:
      result = evaluate(infix_to_postfix(infix))
      print(f"Result = {result}")
      infix = input("Enter another expression to evaluate (X to exit):")
   except:
      print("There seems to be a formatting error in your expression, try again!")
      infix = input("Enter an expression to evaluate (X to exit):")
      