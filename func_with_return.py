#a
def avg_my(num1, num2):
    return (num1 + num2) / 2.0

_avg = avg_my(90, 99)
print(_avg)

#b
def headline_my(title):
    return title.capitalize() + "!"

head1 = headline_my("python has concurred the world")

print(head1)
print(head1)

#c
def list_concat(list1, list2, list3):
    """
    Concatenates three lists into one long list.
    """
    return list1 + list2 + list3

con_res = list_concat([9, 8, 7], [6, 5, 4, 3], [2, 1])

print(con_res)
print(len(con_res))

help(list_concat)