def solution(num1, num2):
    if len(num2) > len(num1):
        num1, num2 = num2, num1

    diff = len(num1) - len(num2)
    val, carry, res = 0, 0, ''
    for i in range(len(num1) - 1, -1, -1):
        if i >= diff:
            val = int(num1[i]) + int(num2[i - diff]) + carry
        else:
            val = int(num1[i]) + carry
        res = str(val % 10) + res
        carry = val // 10

    if carry > 0:
        res = '1' + res

    return res

'''
Finally Test !!!!!
    c4)
    num1    : 1
    num2    : 99
    res     : 100


            i
              01
    num1    : 99
    num2    : 1
    ------------
    res     : '100'

    diff    : 1
    val     : 10
    carry   : 1




    fter for loop
        => if carry > 0
        res = '1' + res


    for i in range(len(num1)-1, ~~~):
        if i >= diff:
                int(num1[i]) + int(num2[i-diff]) + carry
        else:
            int(num1[i]) + carry
        res = str(val) + res
        carry = val / 10


1. Problem
    - Given two non-negative
    - num1, num2 => string
    - return the sum of num1 + num2

    My question
    - non negative
    - positive?? 0 ???
    - int(num1) ??
    - 

2. TCs
    tc1)
    num1    : 1
    num2    : 2
    res     : 3

    tc2)
    num1    : 1
    num2    : 9
    res     : 10

    tc3)
    num1    : 99
    num2    : 1
    res     : 100

    tc4)
    num1    : 1
    num2    : 99
    res     : 100

    num1    : 11
    num2    : 99
    res     : 110


3. Brain Storming

              i
    num1    : 11
    num2    : 32
    --------------------
    res     : 43


    for i in range(len(num1)-1, ~~~):
        val = int(num1[i]) + int(num2[i])
        res = str(val) + res
              i
    num1    : 11
    num2    : 32
    --------------------
    res     : '43'                        <= ''
    val     : 4


              i
    num1    : 1
    num2    : 9
    --------------------
    res     : 10
    val     : 10



               i
               01
    num1    :  19
    num2    :  21
    res     :  '40'       <= res = str(val % 10) + res
    carry   :  0        <= val / 10
    val     :  4       <= int(num1[i]) + int(num2[i]) + carry



              i
              01
    num1    : 99
    num2    : 1
    res     :  '00'          <= res = str(val % 10) + res
    carry   : 1         <= val / 10
    val     : 10              

                            if i >= diff:
                                int(num1[i]) + int(num2[i-diff]) + carry
                            else:
                                int(num1[i]) + carry



    after for loop
        => if carry > 0
        res = '1' + res



4. Summarize

    for i in range(len(num1)-1, ~~~):
        if i >= diff:
                int(num1[i]) + int(num2[i-diff]) + carry
        else:
            int(num1[i]) + carry
        res = str(val) + res
        carry = val / 10



    a) ljust, rjust => 0 append ?
        =>

          0123
    s:    4232

'''
