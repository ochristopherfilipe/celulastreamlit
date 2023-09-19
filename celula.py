import streamlit as st
import random
import re

# Função para embaralhar os nomes
def shuffle_list(lst):
    random.shuffle(lst)

# Função que faz as designações
@st.cache_resource
def fazer_designacoes(pessoas, lideres_edificacao):

    # Lista de tarefas a serem designadas
    tarefas = ["Quebra-gelo", "Louvores", "Edificação", "Cadeira da benção", "Compartilhando a Visão"]

    # Dicionário para armazenar as designações
    designacoes = {}

    for tarefa in tarefas:
        if pessoas:
            if tarefa == "Edificação":
                if lideres_edificacao:
                    designacoes[tarefa] = lideres_edificacao.pop(0)
                else:
                    designacoes[tarefa] = pessoas.pop(0)
            else:
                designacoes[tarefa] = pessoas.pop(0)
        else:
            designacoes[tarefa] = lideres_edificacao.pop(0)

    return designacoes

# Título do streamlit
st.title("Designação de Tarefas")

# Entrada dos nomes dos membros
pessoas_input = st.text_area("Nomes dos membros")

# Entrada dos nomes dos Líderes e pessoas que podem fazer edificação
lideres_edificacao_input = st.text_area("Nomes dos Líderes e pessoas que podem fazer a Edificação")

# Botão para designar tarefas
if st.button("Designar Tarefas"):
    # Dividir nomes usando vírgula, vírgula seguida por espaço ou 'e' como separadores
    pessoas = [p.strip() for p in re.split(r', |,| e |,', pessoas_input) if p.strip()]
    lideres_edificacao = [l.strip() for l in re.split(r', |,| e |,', lideres_edificacao_input) if l.strip()]

    # Embaralhar as listas de pessoas e líderes de edificação antes de fazer as designações
    shuffle_list(pessoas)
    shuffle_list(lideres_edificacao)

    # Chama função de shuffle
    designacoes = fazer_designacoes(pessoas, lideres_edificacao)

    st.header("Designações de Tarefas:")
    for tarefa, pessoa in designacoes.items():
        st.write(f"{tarefa}: {pessoa}")
