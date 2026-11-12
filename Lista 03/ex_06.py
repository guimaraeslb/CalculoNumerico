import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, simpson, trapezoid

def f(x):
    return (x - 2) ** 2 / (x + 3) ** 3

x_tab = np.array([0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75])
y_tab = np.array([1.4815e-1, 8.9213e-2, 5.2478e-2, 2.9630e-2,
                  1.5625e-2, 8.2150e-3, 4.0100e-3, 2.1000e-3])
h = 0.25

def trapezios(y, h):
    return h / 2 * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson_1_3(y, h):
    n = len(y) - 1
    assert n % 2 == 0, "Simpson 1/3 precisa de n par"
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])

def simpson_3_8(y, h):
    assert len(y) == 4, "Simpson 3/8 simples usa 4 pontos"
    return 3 * h / 8 * (y[0] + 3 * y[1] + 3 * y[2] + y[3])

def simpson_hibrido(y, h):
    return simpson_1_3(y[:5], h) + simpson_3_8(y[4:], h)

def simpson_13_mais_trapezio(y, h):
    return simpson_1_3(y[:7], h) + h / 2 * (y[6] + y[7])

y_exato_nos = f(x_tab)
I_ref, _ = quad(f, 0, 1.75)

resultados = {
    "Trapézios (tabela)":                trapezios(y_tab, h),
    "Simpson 1/3 + 3/8 (tabela)":        simpson_hibrido(y_tab, h),
    "Simpson 1/3 + trapézio (tabela)":   simpson_13_mais_trapezio(y_tab, h),
    "scipy.trapezoid (tabela)":          trapezoid(y_tab, x=x_tab),
    "scipy.simpson (tabela)":            simpson(y_tab, x=x_tab),
    "Trapézios (f exata nos nós)":       trapezios(y_exato_nos, h),
    "Simpson 1/3 + 3/8 (f exata nos nós)": simpson_hibrido(y_exato_nos, h),
}

print(f"Referência (scipy.integrate.quad): {I_ref:.6f}\n")
print(f"{'Método':<38}{'Resultado':>11}{'Erro abs.':>13}{'Erro rel.':>11}")
for nome, valor in resultados.items():
    erro = abs(valor - I_ref)
    print(f"{nome:<38}{valor:>11.6f}{erro:>13.2e}{100 * erro / I_ref:>10.2f}%")

print("\nDiferença tabela - f(x) em cada nó:")
for xi, yt, ye in zip(x_tab, y_tab, y_exato_nos):
    print(f"  x = {xi:4.2f}   tabela = {yt:.6f}   f(x) = {ye:.6f}   dif. = {yt - ye:+.2e}")

x_fino = np.linspace(0, 1.75, 400)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(x_fino, f(x_fino), "b-", lw=2, label=r"$f(x)=(x-2)^2/(x+3)^3$")
ax.fill_between(x_tab, y_tab, color="orange", alpha=0.25,
                label="Área dos trapézios (dados da tabela)")
ax.plot(x_tab, y_tab, "r-", lw=0.8)
ax.scatter(x_tab, y_tab, color="red", zorder=5, label="Pontos tabelados")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Questão 6: f(x) e área aproximada em [0; 1,75]")
ax.set_xlim(-0.03, 1.78)
ax.set_ylim(0, 0.16)
ax.set_xticks(x_tab)
ax.grid(True, ls="--", alpha=0.5)
ax.legend()
fig.tight_layout()
fig.savefig("fig1_funcao_trapezios.png", dpi=200)

fig, ax = plt.subplots(figsize=(8, 3.8))
ax.bar(x_tab, (y_tab - y_exato_nos) * 1e3, width=0.15, color="crimson")
ax.axhline(0, color="k", lw=0.8)
ax.set_xlabel("x")
ax.set_ylabel(r"tabela $-$ f(x)  ($\times 10^{-3}$)")
ax.set_title("Discrepância entre os valores tabelados e a função")
ax.set_xticks(x_tab)
ax.grid(True, axis="y", ls="--", alpha=0.5)
fig.tight_layout()
fig.savefig("fig2_discrepancia.png", dpi=200)
plt.show()
plt.show()
