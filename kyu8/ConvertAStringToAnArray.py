""" Write a function to split a string and convert it into an array of words. """

""" "Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"] """

def string_to_array(s):
    if s == "":
        return [s] 
    else:
        return s.split()
    

def string_to_array(string):
    return string.split(" ")


def string_to_array(string=''):
    return string.split() if string else ['']





""" TESTS """

import codewars_test as test
from solution import string_to_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
        test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
        test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
        test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
        test.assert_equals(string_to_array(""), [""])
        
@test.describe("Random Tests")
def random_tests():
    
    from random import randint
    
    sol=lambda s: s.split(" ")
    
    base="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    for _ in range(40):
        s=" ".join(["".join([base[randint(0,len(base)-1)] for q in range(randint(1,20))]) for k in range(randint(1,15))])
        @test.it(f"Testing for string_to_array({repr(s)})")
        def test_case():
            test.assert_equals(string_to_array(s),sol(s))