name = "Denver"
count = 1

def another():
    color = "blue"
    global count
    count +=1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

        greeting("Denver")


# The local scope in Python is created whenever you define a variable inside a function. Variables declared within this scope can only be accessed and used within that specific function. Once the function ends, the local variables are no longer accessible—they are essentially “forgotten” by the program.