# Este código simula um agente reativo que executa uma lista de tarefas de forma sequencial.

import time

tarefas = [
    "Lavar a louça",
    "Limpar o chão",
    "Arrumar a cama",
    "Fazer compras",
    "Estudar para a prova",
]

total_tarefas = len(tarefas)

for i, tarefa in enumerate(tarefas, 1):
    print(f"Tarefa {i}/{total_tarefas}: {tarefa}")
    time.sleep(1)   # Simula um agente reativo que executa tarefas de forma sequencial
print("Todas as tarefas foram concluídas!")
