"""
Decalring dictionary for one's place and ten's place
"""
one_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
ten_dict = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty",
            40: "Fourty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
            80: "Eighty", 90: "Ninty"}


""" 
Method to return values from the one's dictionary
"""


def one(n):
    if n != 0:
        return one_dict[n]
    return ''


""" 
Method to return values from the ten's dictionary
"""


def ten(n1, n2):
    if n1 > 1 and n2 >= 1:
        return ten_dict[int(str(n1) + '0')] + " " + one(n2)
    n = int(str(n1) + str(n2))
    return ten_dict[n]



"""
Main method which is responsible for converting integers to text
"""


def cheque_statement(number):
    global cheque_text

    digit = [int(i) for i in str(number)] #spliting the given number
    length = len(str(number)) # length of the input number

    if length == 1:
        """If length is one and it ends with CROre, LAkh, NEel, PADma, SANkh etc
         append and to it"""
        if cheque_text.endswith(('re', 'kh', 'el', 'd', 'b', 'ma')) and number \
                != 0:
            cheque_text += " and"
        cheque_text += " " + one(number)
        return cheque_text

    """Fetching the maximum value in the dictionary and checking for the 
    length of the given input is within the range of the config file value"""

    max_allow = config_dict.keys()[-1]

    if max_allow <= length >= max_allow+1:
        return "Please configure the config file accordingly"
    else:
        """If the value lies in the range
        for ex: in config file we have 8 digits for crore
        if user inputs a 10crore value (123456789) length is 9
        will get key error as we have 8 for crore in the config file
        in the exception part we will minus 1 from the length to identify 
        which number name it belongs to.
        
        if length is matched in config file:
            will get the text from the config file and  remove the first 
            integer from the input
            
        if length is not matched in config file:
            (in case of 10 lakh, 10 crore..etc)
            will minus 1 from the length and match the number name and 
            removes 2 digits
        """
        try:
            text = config_dict[length]
            if length == 2:
                if cheque_text != '':
                    cheque_text += " and"
                if number >= 20:
                    cheque_text += " " + ten(digit[0], 0)
                else:
                    cheque_text += " " + ten(digit[0], digit[1])
                    return cheque_text

            else:
                cheque_text += " " + one(digit[0]) + " " + text
            digit.pop(0)

        except KeyError:
            text = config_dict[length - 1]
            cheque_text += " " + ten(digit[0], digit[1]) + " " + text
            digit.pop(0)
            digit.pop(0)

    """
    After removing the digits will left with few more digits, will call the 
    cheque_statement function recurvisely until it shrinks to length 1 and 
    :returns cheque_text 
    """

    cheque_text = cheque_statement(int("".join(map(str, digit))))
    return cheque_text



config_dict = {}

"""Reads the config file which is holding the number names and the digit 
length
3  Hundreds
4  Thousands...etc
"""
with open("config.txt") as f:
    for line in f:
        (key, val) = line.split()
        config_dict[int(key)] = val

"""
Reads the Test cases from the test_cases.txt file where the inputs are given 
in a new line

"""
with open("test_cases.txt") as f1:
    for int_value in f1:
        cheque_text = ''
        int_val = int_value.strip()
        if int_val != '0':
            output = cheque_statement(int(int_val))
            print "User Input:", int_val
            print "Output:", output
            print "======================"
        else:
            print "User Input:", int_val
            print "Zero is not a valid input"
            print "======================"
