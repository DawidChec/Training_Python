def fibo(inp):
    num = [1, 1]
    if inp <=2:
        if inp < 1:
            num = 'None'
        elif inp == 2:
            num = [1, 1]
        else:
            num = [1]
    else:
        for i in range(inp - 2):
            num.append(num[-1] + num[-2])
    return num

print(fibo(int(input('How many fibonnaci numbers would you like? \n'))))