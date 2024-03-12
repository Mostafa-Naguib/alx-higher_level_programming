def fizzbuzz():
    for i in range(101):
        if i % 5:
            print("Fizz")
        elif i % 3:
            print("Buzz")
        elif i % 15:
            print("FizzBuzz")
        else:
            print(i)
