#Aluno: Ricardo Augusto de Araújo Machado. - T03 - 10:40 às 12:30.
def resolver_triangular_superior(A,b):
    """
    Entradas:
        A : matriz dos coeficientes.
        b : vetor das constantes.

    Retorna:
        x : vetor solução do sistema.
    """
    #Verificar se as dimensões de A e b são compatíveis.
    if len(A) != len(b):
        return "Dimensões incompatíveis"
    n = len(A) - 1
    x = [0 for i in range(len(A))]
    #Resolver a última linha.
    x[n] = b[n]/A[n][n]
    #Resolver o sistema triangular superior.
    for k in range(n-1,-1,-1):
        soma = 0
        for j in range(k+1,n+1):
            soma += A[k][j]*x[j]
        x[k] = (b[k] - soma)/A[k][k]
    return x
def main():
    #Exemplos de uso da função.
    A1 = [[2,1,2,1],[0,1,0,-1],[0,0,-1,-4],[0,0,0,13]]
    b1 = [6,-2,-11,39]
    x1 = resolver_triangular_superior(A1,b1)
    print("Solução do sistema 1:")
    print(x1)
    A2 = [[2, 1, -1],[0, 3, 2],[0, 0, 1]]
    b2 = [2, 12, 3]
    x2 = resolver_triangular_superior(A2,b2)
    print("Solução do sistema 2:")
    print(x2)
if __name__ == "__main__":
    main()
    