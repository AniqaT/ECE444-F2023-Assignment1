class utils:
    def reversed (number):
        if (type(number) != int):
            return "Input must be an int"
        
        number = list(str(number))
        l, r = 0, len(number) - 1

        while (l < r):
            temp = number[l]
            number[l] = number[r]
            number[r] = temp
            l += 1
            r -= 1
        
        number = int("".join(number))
        return number
        
    def formatter (number):
        if (type(number) != int):
            return "Input must be an int"
        
        base_2_num = bin(number)
        base_8_num = oct(number)

        return [base_2_num, base_8_num]