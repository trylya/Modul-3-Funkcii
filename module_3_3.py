
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5,'text', False]
values_dict = {'a':67, 'b':True, 'c':'bukva'}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [257, 'cat']
print_params(*values_list2,42)