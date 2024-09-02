def ordenacao_natural(lista):
    return sorted(lista)

def ordenacao_customizada(lista, criterio):
    return sorted(lista, key=criterio)

# Exemplo de uso
if __name__ == "__main__":
    # Lista de carros esportivos
    carros_esportivos = ["Ferrari", "Lamborghini", "Porsche", "McLaren", "Bugatti", "Aston Martin", "Koenigsegg"]

    # Ordenação Natural
    print("Ordenação Natural:")
    print(ordenacao_natural(carros_esportivos))

    # Ordenação Customizada - Critério: Ordenar pelo tamanho do nome do carro
    print("\nOrdenação Customizada (tamanho do nome):")
    print(ordenacao_customizada(carros_esportivos, len))

    # Ordenação Customizada - Critério: Ordem alfabética inversa
    print("\nOrdenação Customizada (ordem alfabética inversa):")
    print(ordenacao_customizada(carros_esportivos, lambda x: x[::-1]))
