#def check_alive(health):
#    return health > 0

#def fixed_tests():
    #def basic_test_cases():
        #test.assert_equals(check_alive(5), True)
        #test.assert_equals(check_alive(0), False)
        #test.assert_equals(check_alive(-5), False)

#def repeat_str(n, s):
    #return s * n
#def basic_tests():
    
    #def basic_test_cases():
        #test.assert_equals(repeat_str(4, 'a'), 'aaaa')
        #test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
        #test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
        #test.assert_equals(repeat_str(0, ''), '')
        #test.assert_equals(repeat_str(0, 'I'), '')
        #test.assert_equals(repeat_str(5, ''), '')
        #test.assert_equals(repeat_str(6, 'I'), 'IIIIII')
        #test.assert_equals(repeat_str(5, 'Hello'), 'HelloHelloHelloHelloHello')

#def cookie(x):
    #if isinstance(x, str):
        #return "Who ate the last cookie? It was Zach!"
    #elif isinstance(x, (int, float)):
        #return "Who ate the last cookie? It was Monica!"
    #else:
        #return "Who ate the last cookie? It was the dog!"

#def basic_tests():

    #def examples():   
        #test.assert_equals(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
        #test.assert_equals(cookie(2.3), "Who ate the last cookie? It was Monica!")
        #test.assert_equals(cookie(26), "Who ate the last cookie? It was Monica!")
        #test.assert_equals(cookie(True), "Who ate the last cookie? It was the dog!")

#def century(year):
    #if year % 100 == 0:
        #return year // 100
    #else:
        #return (year // 100) + 1

#def find_average(nums):
    #return sum(nums) / len(nums) if nums else 0 