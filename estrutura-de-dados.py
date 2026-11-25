compras = ["arroz", "feijão", "açucar", "batata"]

print(compras)

# pop = comando usado para remover o ultimo elemento de uma lista
print(compras.pop())

# append = adiciona um item ao final da lista
compras.append("banana")
print(compras)

for item in compras:
    print(item)

print(len(compras))

for i in range(len(compras)): 
    print(compras[i])
    print(i)