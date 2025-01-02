import time

print("Countdown Timer")

userinput = int(input("Enter the number of seconds you want to countdown: "))

while userinput > 0:
    print(userinput)
    time.sleep(1)
    userinput -= 1

if userinput == 0:
    print(userinput)
    print("Time's up!")
