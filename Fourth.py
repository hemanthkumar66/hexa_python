no = int(input('Enter the no in range 10 to 20 '))
while no<10 or no>20:
    print("not proper range ")
    no = int(input('Enter the no between 10,20'))
else:
    print(no)
