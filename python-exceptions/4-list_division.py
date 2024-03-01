#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    fin_list = []
    for i in range(list_length):
        try:
            a = my_list1[i]
            b = my_list2[i]

            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                res = a/b
                fin_list.append(res)
            else:
                print("wrong type")
                fin_list.append(0)
        except IndexError:
            print('out of range')
            fin_list.append(0)
        except ZeroDivisionError:
            print('division by 0')
            fin_list.append(0)
        finally:
            pass
    return fin_list
