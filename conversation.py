# Fun little program just playing around with inputs
# Dog names must be kayce, scout and zero...all lowercase
# There is no "try except" function(?), if you screw up the name its over
# Try your dogs name for fun!




# dogs

kayce = 'kayce'
scout = 'scout'
zero = 'zero'


# Favorite dog

fav_dog = input('Which is your favorite dog? ')

# responding to dog choice

if fav_dog == kayce:
    print('The old so and so')
elif fav_dog == zero:
    print('Of Course')
elif fav_dog == scout:
    print('WOW, bold choice!')
else:
    print("We're not getting a fourth!")
    exit()

# responding to dog choice

second_fav_dog = input('Which is your second favorite dog? ')

if second_fav_dog == kayce:
    print('Second is Better then last, she says')
if second_fav_dog == zero:
    print('I would have thought otherwise')
elif second_fav_dog == scout:
    print('Oh no! Poor Zero!!')

# Assigns least favorite

if fav_dog != scout and second_fav_dog != scout:
    third_fav_dog = scout
    print('That leaves Scout as the least favorite!')

elif fav_dog != kayce and second_fav_dog != kayce:
    third_fav_dog = kayce
    print('That leaves Kayce as the least favorite!')

else:
    third_fav_dog = zero
    print('That leaves Zero as the least favorite!')
    print('WOW')

# List favorite dogs in order

first = "Your love for {} is limitless".format(fav_dog)
second = "{} is a great choice when {} isn't around".format(second_fav_dog, fav_dog)
last = "{}, you could take 'em or leave 'em".format(third_fav_dog)
print(first)
print(second)
print(last)
