# calculator
def add_numbers(a,b):
    return a + b

def get_user_inputs():
    a=float(input("first number"))
    b=float(input("second number"))
    return a , b

if __name__== "__main__":
    num1 , num2 = get_user_inputs()
    result = add_numbers(num1 , num2)
    print("result sum of {} and {} is equal {}".format(num1,num2,result))
    
    