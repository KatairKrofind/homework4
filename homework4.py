immutable_var = 1, 2, 'a', 'b'
print('Immutable tuple: ', immutable_var)
#immutable_var[1] = 'm' - данная переменная относится к типу данных кортеж,
# свойства которой заключаются в неизменяемости и хранении разных типов данных
mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified')
print('Mutable list: ', mutable_list)
