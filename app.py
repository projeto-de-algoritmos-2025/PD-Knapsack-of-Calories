import streamlit as st
from knapsack_solver import solve_knapsack

# BASE DE DADOS DE ALIMENTOS
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

st.header("1. Configure seus Parâmetros")

calorie_limit = st.number_input(
    'Qual seu limite máximo de calorias (kcal)?',
    min_value=100,
    max_value=4000,
    value=800,
    step=50
)

# selecionando os alimentos a considerar
st.write("Quais alimentos você quer incluir na otimização?")
available_foods = list(FOOD_DATABASE.keys())
selected_food_names = st.multiselect(
    'Escolha os alimentos:',
    options=available_foods,
    default=available_foods[:7] # ja deixa pré-selecionado os 7 primeiros
)

st.info("A otimização considerará apenas os alimentos selecionados acima.")

# logica acontece no click no botao
if st.button('💪 Otimizar meu Cardápio!', use_container_width=True):
    if not selected_food_names:
        st.warning("Por favor, selecione pelo menos um alimento para otimizar.")
    else:
        # Prepara os dados para o algoritmo no formato esperado
        items_for_solver = []
        for name in selected_food_names:
            items_for_solver.append({
                'name': name,
                'weight': FOOD_DATABASE[name]['weight'],
                'value': FOOD_DATABASE[name]['value']
            })

        # Chama o algoritmo aqui
        max_protein, selected_foods = solve_knapsack(items_for_solver, calorie_limit)

        st.header("🎉 Resultado da Otimização")

        if not selected_foods:
            st.error("Nenhum cardápio pôde ser formado com as opções e o limite de calorias informado.")
        else:
            # Calcula o total de calorias do cardapio otimizado
            total_calories = sum(food['weight'] for food in selected_foods)

            col1, col2 = st.columns(2)
            col1.metric("Proteína Total", f"{max_protein:.1f} g")
            col2.metric("Calorias Totais", f"{total_calories} kcal")
            
            st.subheader("Cardápio Sugerido:")
            for food in selected_foods:
                st.markdown(
                    f"- **{food['name']}**: {food['weight']} kcal, **{food['value']}g de proteína**"
                )
            
            st.success("Este é o cardápio que oferece o máximo de proteína dentro do seu limite de calorias!")

#  exibe a base de dados para comparar
with st.expander("Ver a base de dados de alimentos completa"):
    st.dataframe(FOOD_DATABASE)
