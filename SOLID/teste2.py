a = 10
b = 20
c = a

print("Endereço de a :", hex(id(a)))
print("Endereço de b :", hex(id(b)))
print("Endereço de c :", hex(id(c)))
print()
print("Esperado de c:", hex(id(a)))
print("obtido   de c:", hex(id(c)))
print('***********************************************')
print()
# Com Objetos:
lista = ['a', 'b', 'c', 'd', 'e']
lista2 = [x for x in range(1, 5)]
dict1 = {s: i for i, s in enumerate(lista)}
dict2 = {value: key for key, value in dict1.items()}
print(dict2)
print(dict1)
dict3 = dict2

dict4 = {k: v for (k, v) in dict3.items()}

print(f'Endereço de memoria de dict1 = {hex(id(dict1))}')

print(f'Endereço de memoria de dict2 = {hex(id(dict2))}')
print(f'Endereço de memoria de dict3 = {hex(id(dict3))}')

print(f'Endereço de memoria de dict4 = {hex(id(dict4))}')
