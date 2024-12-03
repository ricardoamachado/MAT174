#Aluno: Ricardo Augusto de Araújo Machado. - T03 - 10:40 às 12:30.
import numpy as np
def gauss_seidel(A,b,x0,precisao):
    """
    Entradas:
        A : matriz dos coeficientes.
        b : vetor das constantes.
        x0 : vetor inicial.
        precisao : precisão.

    Retorna:
        x : vetor solução do sistema.
    """
    # Verifica se as dimensões de A e b são compatíveis.
    if len(A) != len(b):
        return "Dimensões incompatíveis"
    n = len(A)
    x = x0.copy()
    erro_relativo = precisao + 1
    # Define o número máximo de iterações.
    max_iteracoes = 100
    num_iteracoes = 0
    # Realiza as iterações do método de Gauss-Seidel.
    while erro_relativo > precisao and num_iteracoes <= max_iteracoes:
        x_anterior = x.copy()
        for i in range(n):
            soma = b[i]/A[i][i]
            for j in range(n):
                if j != i:
                    soma -= A[i][j]*x[j]/A[i][i]
            x[i] = soma
        num_iteracoes += 1
        dist_erro = max(abs(x[i] - x_anterior[i]) for i in range(n))
        erro_relativo = dist_erro / max(abs(xi) for xi in x)
  
    return x
def main():
    #Exemplo de uso da função.
    A = [[4, -1, 0, 0],[-1, 4, -1, 0],[0, -1, 4, -1],[0, 0, -1, 4]]
    b = [1, 1, 1, 1]
    x0 = [0, 0, 0, 0]
    precisao = 1e-6
    x1 = gauss_seidel(A,b,x0,precisao)
    print("Solução do sistema: ")
    print(x1)
if __name__ == "__main__":
    main()