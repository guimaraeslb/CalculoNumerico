import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

valores_n = [10, 100, 1000, 10000, 100000, 1000000]

pi_aproximado = []
erros = []

rng = np.random.default_rng()

for n in valores_n:

    x = rng.random(n)
    y = rng.random(n)

    dentro = (x**2 + y**2 <= 1)

    m = np.sum(dentro)

    pi_n = 4 * m / n

    erro = abs(pi_n - pi)

    pi_aproximado.append(pi_n)
    erros.append(erro)

    print(f"n = {n:>8}  m = {m:>8}  "
        f"pi_n = {pi_n:.10f}  erro = {erro:.10f}")

plt.figure(figsize=(8, 5))

plt.loglog(valores_n, erros, 'o-')

plt.xlabel('Número de pontos (n)')
plt.ylabel('Erro absoluto |πₙ - π|')
plt.title('Erro da aproximação de π - Método de Monte Carlo')
plt.grid(True, which="both")

plt.show()