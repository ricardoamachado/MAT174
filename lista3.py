# Aluno: Ricardo Augusto de Araújo Machado. - T03 - 10:40 às 12:30.
import math


def metodo_bissecao(a, b, precisao, f):
    """a : limite inferior do intervalo.
    b : limite superior do intervalo.
    precisao : precisão.
    f : função a ser avaliada.

    Retorna:
        x : raiz da função f"""
    if (b - a) < precisao:
        return (a + b) / 2
    else:
        M = f(a)
        x = (a + b) / 2
        if M * f(x) > 0:
            # Recursão com a = x, caso f(a)*f(x) > 0.
            return metodo_bissecao(x, b, precisao, f)
        else:
            # Recursão com b = x, caso contrário.
            return metodo_bissecao(a, x, precisao, f)


def f1(x):
    # Exemplo 4 do livro.
    return x**3 - 9 * x + 3


def f2(x):
    return x**3 + 4 * x**2 - 10


def f3(x):
    return 3 * x - math.exp(x)


def main():
    raiz_f1 = metodo_bissecao(0, 1, 1e-3, f1)
    raiz_f2 = metodo_bissecao(1, 2, 1e-4, f2)
    raiz_f3 = metodo_bissecao(1, 2, 1e-5, f3)
    print(f"Raiz da função f1: {raiz_f1:.9f}")
    print(f"Raiz da função f2: {raiz_f2:.9f}")
    print(f"Raiz da função f3: {raiz_f3:.9f}")


if __name__ == "__main__":
    main()
