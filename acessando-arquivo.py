import json #estamos trazendo algo de fora para dentro

ARQUIVO = "gastos.json"

def carregar(): 
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)