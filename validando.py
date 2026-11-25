idade = int(input())

# quer verificar se a pessoa pode tirar cnh ou nao
# se a pessoa tem idade igual ou maior a 18 anos, ela pode tirar
# se a pessoa tem idade igual ou maior a 17 anos, ela pode iniciar o processo mas não realizar a prova
# se a pessoa tem menos do que 17 anos, ela não pode tirar a cnh

if idade >= 18:
    print("CNH liberada!")
# se senão -> porque já verificamos o primeiro se
elif idade >= 17:
    print("Pode iniciar o processo mas não fazer a prova.")
else:
    print("Não tem idade o suficiente para tirar a CNH.")