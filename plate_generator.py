from random import randint

def lower():
    x = ord('a')
    y = ord('z')
    temp = randint(x, y)
    return chr(temp)
#--------------------------------------------
def upper():
    x = ord('A')
    y = ord('Z')
    temp = randint(x, y)
    return chr(temp)
#--------------------------------------------
def two_digit_number():
    return randint(10,99)
#--------------------------------------------
def two_digit_number_even():
    x = randint(10,99)
    if x % 2 != 0:
        x -= 1
    return x
#--------------------------------------------
def three_digit_number():
    return randint(100,999)
#--------------------------------------------
q = int(input('How many do you want: '))
while q <= 0:
    int(input('Try again, How many do you want: '))
    
w = int(input('How many do you lower: '))
while w < 0:
    int(input('Try again, How many do you lower: '))
    
e = int(input('How many do you upper: '))
while e < 0:
    int(input('Try again, How many do you lower: '))
    
r = int(input('How many do you number_2: '))
while r < 0:
    int(input('Try again, How many do you number_2: '))
    
t = int(input('How many do you number_2_even: '))
while t < 0:
    int(input('Try again, How many do you number_2_even: '))
    
u = int(input('How many do you number_3: '))
while u < 0:
    int(input('Try again, How many do you number_3: '))
#--------------------------------------------

for k in range(q):
    plate = ''
    
    for i in range(w):
        plate += lower()
        
    for i in range(e):
        plate += upper()

    for i in range(r):
        plate += str(two_digit_number())

    for i in range(t):
        plate += str(two_digit_number_even())

    for i in range(u):
        plate += str(three_digit_number())

    print(f'plate {k + 1}: ', plate)    
