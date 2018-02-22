one_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
ten_dict = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty",
            40: "Fourty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
            80: "Eighty", 90: "Ninty"}


def one(n):
    if n != 0:
        return one_dict[n]
    return ''


def ten(n1, n2):
    if n1 != 0:
        n = int(str(n1) + str(n2))
        return ten_dict[n]
    return " and"


def cheque_statement(number):
    print ("number", number)
    if number == 0:
        return "Zero"

    global cheque_text

    digit = [int(i) for i in str(number)]
    length = len(str(number))
    if length == 1:
        if cheque_text != '':
            cheque_text += " and"
        cheque_text += " " + one(number)
        return cheque_text

    if length not in config_dict and length + 1 not in config_dict:
        return "Please configure the config file accordingly"
    else:
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

    cheque_text = cheque_statement(int("".join(map(str, digit))))
    return cheque_text


config_dict = {}
cheque_text = ''

with open("config.txt") as f:
    for line in f:
        (key, val) = line.split()
        k = int(key)
        if k <=3:
            config_dict[k] = val
        else:
            config_dict[k+1]  = val

output = cheque_statement(int('1121'))
print(output)
# print(cheque(100000000234))
