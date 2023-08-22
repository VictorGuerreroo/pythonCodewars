""" The Story:
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

Task Overview:
You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus excluding the driver.
wait is the number of people waiting to get on to the bus excluding the driver.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

Usage Examples:
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting """

def enough(cap, on, wait):
    return max(0, wait - (cap - on))

def enough(cap, on, wait):
    return wait + on - cap if wait + on > cap else 0

def enough(cap, on, wait):
    rem=cap-on
    if wait<=rem:
        return 0
    else :
        return wait-rem
a=enough(5,3,2)
if a==0:
    print("Yes.Bob can take all passengers with him")
else :
    print("Woops.Bob can't able to take ",a," passengers into the bus")



""" TESTS """

import codewars_test as test
from solution import enough

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(enough(10, 5, 5), 0)
        test.assert_equals(enough(100, 60, 50), 10)
        test.assert_equals(enough(20, 5, 5), 0)


@test.describe("Random Tests")
def random_tests():

    import random
    
    random.seed = None
    
    def control(cap, on, wait):
        if on+wait <= cap:
            return 0
        else:
            return on+wait-cap

    for TEST in range(0, 20):
        a = random.randint(50, 100)
        b = min(random.randint(0, 80), a)
        c = random.randint(0, 80)
        @test.it(f"testing for enough({a}, {b}, {c})")
        def test_case():
            test.assert_equals(enough(a,b,c), control(a,b,c))