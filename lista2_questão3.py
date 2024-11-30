import numpy as np
def resolver_triangular_superior(A,b):
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
    A = [[2,1,2,1],[0,1,0,-1],[0,0,-1,-4],[0,0,0,13]]
    b = [6,-2,-11,39]
    x1 = resolver_triangular_superior(A,b)
    print(f"A:{len(A)} e |b|:{len(b)}")
    print(x1)
    x2 = np.linalg.solve(A,b)
    print(x2)
if __name__ == "__main__":
    main()
    