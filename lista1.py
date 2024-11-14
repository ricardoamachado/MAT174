def bin_para_dec(binario):
    """ Converte um número binário inteiro para decimal."""
    #Converte o numero binario para string de modo que seja possivel acessar cada dígito.
    binario = str(binario)
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2 ** (len(binario) - 1 - i)
    return decimal

def dec_para_bin(decimal):
    """ Converte um número decimal inteiro para binário. Retorna binário como string."""
    decimal = int(decimal)
    binario = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        resto = decimal % 2
        #Concatena o dígito obtio na iteração atual com os dígitos já encontrados.
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario

def bin_frac_para_dec(binario):
    binario = str(binario)
    #Separa a string do binário em parte inteira e parte fracionária.
    indice_separador = binario.index(".")
    bin_parte_inteira = binario[:indice_separador]
    bin_parte_decimal = binario[indice_separador:]
    #Utiliza a função já existente para converter a parte inteira do binário para decimal.
    decimal_parte_inteira = bin_para_dec(bin_parte_inteira)
    decimal_parte_fracional = 0
    #Converte a parte fracionária do binário para decimal.
    #Começa do indice 1 para ignorar o ponto.
    for i, digito in enumerate(bin_parte_decimal[1:]):
        decimal_parte_fracional += int(digito) * 2 ** (-(i + 1))
    decimal = decimal_parte_inteira + decimal_parte_fracional
    return decimal

def main():
    print(bin_para_dec(1011))
    print(dec_para_bin(12))
    bin_frac_para_dec(1010.110110)


if __name__ == '__main__':
    main()