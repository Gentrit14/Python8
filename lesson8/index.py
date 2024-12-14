text = "This is not a number"


try:
    text_to_int = int(text)

except Exception as e :
    print("An error accured whie parsing the data: " , e)


try:
    result = 10/2

except ZeroDivisionError:
    print("this Devisiion is acured bla bla bla")

else:
    print("Bla Bla Bla comsi comsa", result)


try:
    result = 10/2

except ZeroDivisionError:
    print("this Devisiion is acured bla bla bla")

finally:
    print("Finally this exept okey")



