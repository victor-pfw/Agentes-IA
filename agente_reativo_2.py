#Agente reativo percepção simples
# Este código simula um agente reativo que toma decisões com base em percepções simples do ambiente.

def perceber():
    return input("Ambiente: ")

def decidir(percepcao):
    if "sujo" in percepcao:
        return "Limpar"
    elif "fome" in percepcao:
        return "comer"
    elif "nadar" in percepcao:
        return "descançar"
    else:
        return "esperar"

def agir(acao):
    print(f"Agenter vai:  {acao}")

while True:
    percepcao = perceber()
    if percepcao == "sair":
        print("Encerrando agente...")
        break
    acao = decidir(percepcao)
    agir(acao)