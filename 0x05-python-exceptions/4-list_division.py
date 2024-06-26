#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    product = 0
    for i in range(list_length):
        try:
            product = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            product = 0
        except TypeError:
            print("wrong type")
            product = 0
        except ZeroDivisionError:
            print("division by 0")
            product = 0
        finally:
            new_list.append(product)

    return new_list
