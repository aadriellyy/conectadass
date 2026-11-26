def cadastrar_gastos(gastos, descricao, valor, tipo):
    gastos.append({
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo
    })
    return gastos

gastos = []
novos_gastos = cadastrar_gastos(gastos, "Mercado", 152.30, "Alimentação")
print(novos_gastos)

def calcular_gastos(novos_gastos):
    total = 0
    for dicionario in novos_gastos:
        total = total + dicionario["valor"]
    return total

print(calcular_gastos(novos_gastos))

