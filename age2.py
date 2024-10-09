def within_range(num: int, min: int, max: int) -> bool:
    return (min < number and number <= max)
# if 0 < number and number <= 99:
#    return True
#  elif:
#    return False


while (True):
    answer: str = input("How old are you?")
# 1. Check if valid number
    try:
        number = int(answer)
    except ValueError as error:
        print("Give a valid number!")
        continue
# 2. Check if input is between 0 and 99
    valid: bool = within_range(number, 0, 99)
    if not valid:
        print("You gave the wrong number!")
        continue
    elif valid:
        break

state: str = ""


if 0 < number and number <= 99:
    # OK
    if number <= 25:
        state = "young"

    elif number <= 50:
        state = "adult"

    elif number <= 75:
        state = "elderly"

    elif number <= 99:
        state = "ghost"

match state:
    case "young":
        print("Lucky")
    case "adult":
        print("Not so lucky")
    case "elderly":
        print("Even less lucky")
    case "ghost":
        print("Unlucky")
    case _:
        pass
