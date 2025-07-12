def solve_knapsack(items, capacity):
    """
    Resolve o problema da mochila (Knapsack Problem) usando programação dinâmica.
    
    """
    n = len(items)
    # Cria uma matriz para armazenar os resultados
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Preenche a matriz de forma iterativa (bottom-up)
    for i in range(1, n + 1):
        item = items[i-1]
        item_weight = item['weight']
        item_value = item['value']

        for w in range(1, capacity + 1):
            # Caso 1: O item atual é pesado demais
            if item_weight > w:
                dp_table[i][w] = dp_table[i-1][w]
            else:
                # Caso 2: O item pode ser incluído ou não, se este exitir
                value_without_item = dp_table[i-1][w]

                value_with_item = item_value + dp_table[i-1][w - item_weight]

                # A solução ótima para dp_table[i][w]
                dp_table[i][w] = max(value_without_item, value_with_item)

    total_value = dp_table[n][capacity]
    selected_items = []
    
    # Inicia o "backtracking" para descobrir quais itens foram escolhidos
    w = capacity
    for i in range(n, 0, -1):
        # Se o valor na tabela é diferente do valor acima, significa que o item foi incluído
        if dp_table[i][w] != dp_table[i-1][w]:
            item = items[i-1]
            selected_items.append(item)
            w -= item['weight']

    return total_value, selected_items