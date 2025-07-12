import streamlit as st

# --- BASE DE DADOS DE ALIMENTOS ---
# simulando um banco de dados, pois não seria necessário tê-lo agora
# As equivalencias: 'weight' = Calorias, 'value' = Proteínas (em gramas)

FOOD_DATABASE = {
    'Frango Grelhado (100g)': {'weight': 165, 'value': 31},
    'Salmão Assado (100g)': {'weight': 208, 'value': 22},
    'Ovo Cozido (1 unidade)': {'weight': 78, 'value': 6},
    'Carne Moída (100g)': {'weight': 250, 'value': 26},
    'Arroz Branco (100g)': {'weight': 130, 'value': 2.7},
    'Feijão Preto (100g)': {'weight': 131, 'value': 8.9},
    'Brócolis Cozido (100g)': {'weight': 35, 'value': 2.4},
    'Batata Doce (100g)': {'weight': 86, 'value': 1.6},
    'Abacate (50g)': {'weight': 80, 'value': 1},
    'Azeite de Oliva (1 colher)': {'weight': 119, 'value': 0},
    'Queijo Minas (30g)': {'weight': 72, 'value': 5},
    'Iogurte Grego (100g)': {'weight': 59, 'value': 10},
    'Lentilhas (100g)': {'weight': 116, 'value': 9},
}

# inicio da interface

st.set_page_config(page_title="Otimizador de Dieta", page_icon="🥗")

st.title("🥗 Otimizador de Dieta Inteligente")
st.write(
    "Esta ferramenta usa o algoritmo do **Problema da Mochila (Knapsack)** "
    "para montar um cardápio que **maximiza a quantidade de proteína** "
    "sem ultrapassar seu limite de calorias diário."
)
