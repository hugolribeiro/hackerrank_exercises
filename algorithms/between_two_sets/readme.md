1 - First we need to calculate the lcm (least common multiple) of all number in a

    So, we need to pick all numbers in a and try to divide them to numbers begin to 2 at same time. 
    If none number can divided by the divisor or at leat one number is different to 1, we raise the divisor.
    
    Example:
    60, 80
    
    60 / 2 - ok, it is possible  |  80 / 2 - ok, it is possbile
    
    Now we have 30 and 40 ... in divisor we have 2
    
    So we'll try to do again this division.
    
    30 / 2 - ok, it is possible  | 40 / 2 - ok, it is possible
    
    Now we have 15 and 20 ... in divisor we have [2, 2]
    
    So we'll try to do the division by 2 again
    
    15 / 2 - ow no, it is not possible | 20 / 2 - ok, it is possible
    
    Now we have 15 and 10 ... in divisor we have [2, 2, 2]
    
    15 / 2 - not ok     | 10 / 2  - ok
    
    We got 15 and 5 ... in divisor we have [2, 2, 2, 2]
    
    15 / 2 - not ok   | 5 / 2 - not ok
    
    Lets raise the divisor. So now we got 3 like divisor
    
    15 / 3 - ok     | 5 / 3 - not ok
    
    We got 5 and 5 ... in divisors we have [2, 2, 2, 2, 3]
    
    5 / 3 - not ok    | 5 / 3 - not ok
    
    We need to raise the divisor to the next prime number (5)
    
    5 / 5 - ok       | 5 / 5 - ok
    
    We got 1 and 1 ... in divisors we have [2, 2, 2, 2, 3, 5]
    
    All numbers is equal to 1, so we finish it.
    
    Lets multiply all numbers in divisors
    
    2 * 2 * 2 * 2 * 3 * 5 = 240
    
    So, the LCM between 60 and 80 is equal to 240

2 - We need to calculate the GCD (Greatest common divisor) of the numbers in b
    
    We can use the library Math with the method gcd to do this
   
3 - Now we need to find all multiples of the lcm we have and divide them to the gcd

4 - Finally, we have to divide the gcd with all multiples wich we found at step 3