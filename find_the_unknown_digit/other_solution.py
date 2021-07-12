def to_chinese_numeral(n):
    numerals = {
        "-":"负",
        ".":"点",
        0:"零",
        1:"一",
        2:"二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
        10:"十",
        100:"百",
        1000:"千",
        10000:"万"
    }

    #find out if number is negative
    neg = True if n < 0 else False
    n = n *-1 if neg else n

    #split input number by decimal sepeartor
    nums = str(n).split(".")

    #make a list such that 1245 -> 1*1000 + 2*100 + 4*10 + 5*1 -> ["一千", "二百", "四十", "五一"]
    nums[0] = [numerals[int(j)] + numerals[10**i] for i,j in enumerate(nums[0][::-1])][::-1] 
    
    #since chinese notation dictates that several zeroes in the middle of a number are concatinated,
    #we loop through the list of numbers and concatinate all adjeacent zeroes to the left of the decimal seperator
    prev = False
    for i,j in enumerate(nums[0]):
        if j[0] == "零" and not prev:
            nums[0][i] = "零"
            prev = True
            
        elif j[0] == "零" and prev:
            nums[0][i] = ""
        
        else:
            prev = False

    #remove leftover zeroes from the right side of the number and join the list of characters
    nums[0] = "".join(nums[0]).rstrip('零')

    #i already forgot why i did this, but it works :)
    nums[0] = "零" if nums[0] == '' else nums[0]
    nums[0] = nums[0][:-1] if nums[0][-1] == '一' else nums[0]
    nums[0] = nums[0][1:] if nums[0][0] == '一' and 10 <= n < 20 else nums[0]

    #this section handles the right side of the number, which is the decimal seperator
    if len(nums) > 1:
        nums[1] = ["点"] + [numerals[int(i)] for i in nums[1]]
        nums[1] = "".join(nums[1])

    #join the two sides of the number and return the result
    return "".join(nums) if not neg else "负" + "".join(nums)

print(to_chinese_numeral(9) + "         should equal: '九' ")     
print(to_chinese_numeral(-5) + "        should equal: '负五' ")     
print(to_chinese_numeral(0.5) + "       should equal: '零点五' ")     
print(to_chinese_numeral(1.5) + "       should equal: '一点五' ")     
print(to_chinese_numeral(10) + "        should equal: '十' ")
print(to_chinese_numeral(15) + "        should equal: '十五' ")       
print(to_chinese_numeral(110) + "       should equal: '一百一十' ")     
print(to_chinese_numeral(111) + "       should equal: '一百一十一' ")     
print(to_chinese_numeral(1000) + "      should equal: '一千' ")     
print(to_chinese_numeral(10000) + "     should equal: '一万' ")     
print(to_chinese_numeral(10006) + "     should equal: '一万零六' ")     
print(to_chinese_numeral(10306.005) + " should equal: '一万零三百零六点零零五' ")