import art


#add
def add(n1,n2):
    return n1+n2
#sub
def subtract(n1,n2):
    return n1-n2
#multiply
def multiply(n1,n2):
    return n1*n2
#divide
def divide(n1,n2):
    return n1/n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/" :divide,
}



def calculator():
    print(art.logo)
    num1=float(input("What is the first number: "))
    should_continue=True
    while should_continue:
        for symbol in operation:
            print(symbol)
        operator=input("pick a symbol: ")

        num2=float(input("What is the secund number: "))

        answer=operation[operator](num1,num2)
        print(f"{num1}{operator}{num2}={answer}")

        choice=input("type y to continue with {answer}, or type n to discontinue")
        if choice=="y":
            num1=answer

        else:
            should_continue=False
            print("\n"*100)
            calculator()

calculator()