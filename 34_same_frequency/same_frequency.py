def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_dic = {}
    num2_dic = {}
    num1 = str(num1)
    num2 = str(num2)
    for num in num1:
        if num in num1_dic.keys():
            num1_dic[num] += 1
        else:
            num1_dic[num] = 1
    for num in num2:
        if num in num2_dic.keys():
            num2_dic[num] += 1
        else:
            num2_dic[num] = 1
    if num1_dic == num2_dic:
        return True
    return False
        