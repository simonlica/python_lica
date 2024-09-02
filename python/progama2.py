def ordenacao_total(lista):
    return sorted(lista, key=lambda x: (isinstance(x, str), x))

# Exemplo de uso
if __name__ == "__main__":
    itens = ["Ferrari", "Lamborghini", "Porsche", "McLaren", "Bugatti", 10, 3, 50, 7, 1]
    
    ordenado = ordenacao_total(itens)
    print("Lista ordenada (números primeiro, depois strings):")
    print(ordenado)
