# Agente reativo com percepção simples modularizado

def agente(percepcao):
    return decidir(percepcao)

def main():
    while True:
        percepcao = input("Ambiente: ")
        if percepcao == "sair":
            print("Encerrando agente...")
            break
        acao = agente(percepcao)
        print(f"Agente vai: {acao}")

def decidir(percepcao):
    if "sujo" in percepcao:
        return "limpar"
    elif "fome" in percepcao:
        return "comer"
    elif "nadar" in percepcao:
        return "descansar"
    else:
        return "esperar"

if __name__ == "__main__":
    main()
