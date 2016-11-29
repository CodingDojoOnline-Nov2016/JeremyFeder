# initial solution
def odd_even():
    for number in range(1, 2000+1):
        if number % 2 != 0:
            print "Number is", number, ".", "This is an odd number."
        elif number % 2 == 0:
            print "Number is", number, ".", "This is an even number."
odd_even()

# a better solution
def odd_even(start, end):
    for num in range(start, end+1):
        if num % 2 != 0:
            odev = "odd"
        elif num % 2 == 0:
            odev = "even"
        print "Number is {}. This is an {} number.".format(num, odev)
odd_even(1, 2000)
