def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(a = 5, b = 'str', c = [1, 3, 9])
print_params(b = 25)
print_params(c = [1,2,3])
#
values_list = [5, 'string', 21.7]
values_dict = {'a': 9, 'b': 'apple', 'c': 32.1}
print_params(*values_list)
print_params(**values_dict)
#
values_list_2 = [(1, 3, 5), 'home']
print_params(*values_list_2, 42)