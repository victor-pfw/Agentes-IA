# Estudos de Agentes de IA - Semana 1

Este repositório contém os primeiros exercícios e exemplos de implementação de agentes de IA, focando em agentes reativos simples.

## Conteúdo

### 1. Agente Reativo Sequencial (`agente_reativo_1.py`)
- Implementação de um agente que executa tarefas de forma sequencial
- Demonstra o conceito básico de um agente que segue uma lista predefinida de ações
- Simula a execução de tarefas domésticas com um intervalo de tempo entre cada uma

### 2. Agente Reativo com Percepção Simples (`agente_reativo_2.py`)
- Implementação de um agente que toma decisões baseadas em percepções do ambiente
- Utiliza um modelo de estímulo-resposta simples
- O agente reage a palavras-chave como "sujo", "fome" e "nadar" com ações apropriadas

### 3. Agente Reativo Modularizado (`agente_reativo_3.py`)
- Versão modularizada do agente reativo com percepção simples
- Implementa uma arquitetura mais organizada com funções separadas para percepção, decisão e ação
- Demonstra boas práticas de programação com estrutura principal (`main`) e funções específicas

## Como Executar

Para executar qualquer um dos agentes, use o interpretador Python:

```bash
python agente_reativo_1.py
python agente_reativo_2.py
python agente_reativo_3.py
```

## Conceitos Abordados

- **Agentes Reativos**: Agentes que respondem diretamente a estímulos sem manter estado interno ou planejar ações futuras
- **Percepção e Ação**: Mecanismos básicos de interação com o ambiente
- **Modularização**: Organização de código para melhor manutenção e compreensão

## Próximos Passos

Nas próximas semanas, serão explorados conceitos mais avançados como:
- Agentes com estado interno
- Agentes baseados em objetivos
- Agentes baseados em utilidade
- Agentes de aprendizado