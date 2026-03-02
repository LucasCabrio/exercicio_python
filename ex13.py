def calculador (a,b,operacao):
    if operacao == "+":
        return a+b
    elif operacao == "-":
        return a-b
    elif operacao == "*":
        return a*b
    else:
        if b == 0:
            return "Idiota"
        else:
            return a/b
        
print (calculador (10, 2, "/"))