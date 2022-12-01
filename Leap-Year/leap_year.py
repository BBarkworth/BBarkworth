from datetime import date

def leap_year_check(num):
    num = float(num)
    first = num % 4
    second = num / 100
    third = num / 400
    if first % 4 == 0:
        if second % 1 == 0:
            if third % 1 != 0:
                return "No"
        return "Yes"
    else:
        return "No"

user_input = input("Please insert a number: ")
while user_input.isnumeric() == False:
    user_input = input("Please insert a number: ")
if len(user_input) < 1:
    today = date.today()
    year = today.strftime("%Y")
    year = float(year)
else:
    year = user_input
answer = leap_year_check(year)
print(answer)