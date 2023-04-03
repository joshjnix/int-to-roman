class Solution:
    def intToRoman(self, num: int) -> str:
        mystr = ""

        if num >= 1000:
            mystr += "M" * (num // 1000)
            num -= 1000 * (num // 1000) 

        if num >= 500:
            if num >= 900:
                mystr += "CM"
                num -= 900 
            else:
                mystr += "D" * (num // 500)
                num -= 500 * (num // 500)

        if num >= 100:
            if num >= 400:
                mystr += "CD"
                num -= 400
            else:
                mystr += "C" * (num // 100)
                num -= 100 * (num // 100)

        if num >= 50:
            if num >= 90:
                mystr += "XC"
                num -= 90
            else:
                mystr += "L" * (num // 50)
                num -= 50 * (num // 50)

        if num >= 10:
            if num >= 40:
                mystr += "XL"
                num -= 40
            else:
                mystr += "X" * (num // 10)
                num -= 10 * (num // 10)

        if num >= 5:
            if num >= 9:
                mystr += "IX" 
                num -= 9
            else:
                mystr += "V" * (num // 5)
                num -= 5 * (num // 5)

        if num >= 1:
            if (num // 1) == 4:
                mystr += "IV"
            else: 
                mystr += "I" * (num // 1)
        
        return mystr
