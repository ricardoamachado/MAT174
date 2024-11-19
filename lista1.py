#Aluno: Ricardo Augusto de Araújo Machado. - 10:40 às 12:30.
def bin_para_dec(binario):
    """Converte um número binário inteiro para decimal."""
    # Converte o numero binario para string de modo que seja possivel acessar cada dígito.
    binario = str(binario)
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2 ** (len(binario) - 1 - i)
    return decimal


def dec_para_bin(decimal):
    """Converte um número decimal inteiro para binário. Retorna binário como string."""
    decimal = int(decimal)
    binario = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        resto = decimal % 2
        # Concatena o dígito obtido na iteração atual com os dígitos já encontrados.
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario


def bin_frac_para_dec(binario):
    binario = str(binario)
    # Separa a string do binário em parte inteira e parte fracionária.
    indice_separador = binario.index(".")
    bin_parte_inteira = binario[:indice_separador]
    bin_parte_decimal = binario[indice_separador:]
    # Utiliza a função já existente para converter a parte inteira do binário para decimal.
    decimal_parte_inteira = bin_para_dec(bin_parte_inteira)
    decimal_parte_fracional = 0
    # Converte a parte fracionária do binário para decimal.
    # Começa do indice 1 para ignorar o ponto.
    for i, digito in enumerate(bin_parte_decimal[1:]):
        decimal_parte_fracional += int(digito) * 2 ** (-(i + 1))
    decimal = decimal_parte_inteira + decimal_parte_fracional
    return decimal

def dec_frac_para_bin(decimal):
    decimal = str(decimal)
    # Separa a string do decimal em parte inteira e parte fracionária.
    indice_separador = decimal.index(".")
    dec_parte_inteira = decimal[:indice_separador]
    dec_parte_decimal = decimal[indice_separador:]
    # Utiliza a função já existente para converter a parte inteira do decimal.
    bin_parte_inteira = dec_para_bin(dec_parte_inteira)
    bin_parte_decimal = ""
    decimal_parte_fracional = float(dec_parte_decimal)
    iteracao = 0
    #Define maximo de iterações para evitar loop infinito.
    nmax_iteracoes = 20
    while decimal_parte_fracional > 0 and iteracao < nmax_iteracoes:
        decimal_parte_fracional *= 2
        if decimal_parte_fracional >= 1:
            bin_parte_decimal += "1"
            decimal_parte_fracional -= 1
        else:
            bin_parte_decimal += "0"
        iteracao += 1
    return bin_parte_inteira + '.' + bin_parte_decimal

def main():
    entrada = input("Digite um número\n")
    while True:
        try:
            tipo_numero = input(
                "Escolha a opção:\n"
                " 0 - Binário para decimal\n"
                " 1 - Decimal para binário\n"
                " 2 - Binário fracionário para decimal\n"
                " 3 - Decimal fracionário para binário\n"
            )
            tipo_numero = int(tipo_numero)
            if tipo_numero == 0:
                resultado = bin_para_dec(entrada)
                print(resultado)
                break
            elif tipo_numero == 1:
                resultado = dec_para_bin(entrada)
                print(resultado)
                break
            elif tipo_numero == 2:
                resultado = bin_frac_para_dec(entrada)
                print(resultado)
                break
            elif tipo_numero == 3:
                resultado = dec_frac_para_bin(entrada)
                print(resultado)
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Entrada inválida")
            break


if __name__ == "__main__":
    main()
