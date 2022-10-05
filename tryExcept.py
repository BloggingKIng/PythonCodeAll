    
from typing import Type


def divide(number1, number2):
    try:
        number1/number2
    except ZeroDivisionError as e:
        print("You can't divide a number by zero man!")
    except TypeError as error:
        print(error)
        print("You can't divide two strings!")
    
    except:
        print("An Error has occurred")


divide('3','50')