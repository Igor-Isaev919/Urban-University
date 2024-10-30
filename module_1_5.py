immutable_var = 7, [6*1+3], 'Freedom', True
print(immutable_var)
print(immutable_var[-1])
#immutable_var[0] = 1 #Кортежи — это неизменяемый тип данных в Python, который используется для хранения упорядоченной последовательности элементов.
mutable_list = [8, 'London', False, [8/2*3]]
print(mutable_list)
mutable_list[0] = 14
mutable_list[-1] = [6/2+4]
mutable_list.append('another one')
print(mutable_list)