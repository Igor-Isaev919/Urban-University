### словари
my_dict  = {'Viktor': 1996, 'Igor': 1993, 'Max': 2000, 'Stepan': 1999}
print(my_dict)
print(my_dict['Stepan'])
print(my_dict.get('Oleg'))
my_dict.update({'Leonid': 1987, 'Nikita': 2003})
key_to_delete = 'Max'
value_deleted = my_dict.pop(key_to_delete)
print(value_deleted)
print(my_dict)
### множества
my_set = {5, 'Kursk', 4, True, 5, 'Kursk', 4, 'Igor', 4, True}
print(my_set)
my_set.update({12.76, 'London', 12.76})
my_set.discard(True)
print(my_set)





