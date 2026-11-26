notas = []

#percorre até n-1, nesse caso vai percorrer entre 0 e 3 pois nosso n = 4
for i in range(4):
    nota = float(input())
    notas.append(nota)

# sum = soma todos os valores de uma lista
soma_media = sum(notas)
media_final = soma_media/4

print("Sua média final é: ", media_final)

if media_final >= 5:
    print("Parabéns, você passou de ano!")
elif media_final >= 4:
    print("Você está de recuperação")
else: 
    print("Que pena! Você reprovou de ano")
