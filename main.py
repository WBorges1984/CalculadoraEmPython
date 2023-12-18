def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        # Verificar divisão por zero
        return num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"
    else:
        # Caso seja inserido um número de operação inválido
        return 0

# Exemplos de uso:
resultado_soma = calculadora(5, 3, 1)
resultado_subtracao = calculadora(5, 3, 2)
resultado_multiplicacao = calculadora(5, 3, 3)
resultado_divisao = calculadora(5, 0, 4)  # Divisão por zero

# Exibir resultados
print("Soma:", resultado_soma)
print("Subtração:", resultado_subtracao)
print("Multiplicação:", resultado_multiplicacao)
print("Divisão:", resultado_divisao)
