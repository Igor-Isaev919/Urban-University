def test_function():
    def inner_function():
        print('Я в области видимости функции test function')
    inner_function()
test_function()
#inner_function() ###при попытке вызова функции возникает ошибка, т.к. она находится в
                 ###локальной области видимости функции test_function