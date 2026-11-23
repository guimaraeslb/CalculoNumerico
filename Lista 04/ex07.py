import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
  """EDO: dy/dt = -15 * y(t)"""
  return -15.0 * y


def solucao_exata(t):
  """Solução analítica: y(t) = exp(-15 * t)"""
  return np.exp(-15.0 * t)


def malha_tempo(t0, tf, h):
  """Gera os instantes de t0 até tf com passo h (incluindo tf)."""
  n_passos = int(round((tf - t0) / h))
  return np.linspace(t0, tf, n_passos + 1)


def euler(t0, tf, y0, h):
  t = malha_tempo(t0, tf, h)
  y = np.empty_like(t, dtype=float)
  y[0] = float(y0)
  for i in range(len(t) - 1):
    y[i + 1] = y[i] + h * f(t[i], y[i])
  return t, y


def heun(t0, tf, y0, h):
  """Método de Heun (Euler aprimorado / Runge-Kutta explícito de 2.ª ordem)."""
  t = malha_tempo(t0, tf, h)
  y = np.empty_like(t, dtype=float)
  y[0] = float(y0)
  for i in range(len(t) - 1):
    k1 = f(t[i], y[i])
    k2 = f(t[i + 1], y[i] + h * k1)
    y[i + 1] = y[i] + 0.5 * h * (k1 + k2)
  return t, y


def ponto_medio(t0, tf, y0, h):
  """Método do Ponto Médio (Runge-Kutta explícito de 2.ª ordem)."""
  t = malha_tempo(t0, tf, h)
  y = np.empty_like(t, dtype=float)
  y[0] = float(y0)
  for i in range(len(t) - 1):
    k1 = f(t[i], y[i])
    y_mid = y[i] + 0.5 * h * k1
    k2 = f(t[i] + 0.5 * h, y_mid)
    y[i + 1] = y[i] + h * k2
  return t, y


def rk4(t0, tf, y0, h):
  """Método de Runge-Kutta de 4.ª ordem clássico."""
  t = malha_tempo(t0, tf, h)
  y = np.empty_like(t, dtype=float)
  y[0] = float(y0)
  for i in range(len(t) - 1):
    ti, yi = t[i], y[i]
    k1 = f(ti, yi)
    k2 = f(ti + 0.5 * h, yi + 0.5 * h * k1)
    k3 = f(ti + 0.5 * h, yi + 0.5 * h * k2)
    k4 = f(ti + h, yi + h * k3)
    y[i + 1] = yi + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
  return t, y


def main():
  t0, tf, y0 = 0.0, 2.0, 1.0
  passos = [0.2, 0.1, 0.05, 0.025]

  metodos = {
      "Euler": euler,
      "Heun": heun,
      "Ponto Médio": ponto_medio,
      "RK4": rk4,
  }

  t_fino = np.linspace(t0, tf, 500)
  y_fino = solucao_exata(t_fino)

  # Impressão de valores finais em t = 2.0 para apoio aos itens 4 e 5
  for h in passos:
    y_ex_fim = solucao_exata(tf)
    print(f"=== Passo h = {h} (Exata em t=2: {y_ex_fim:.3e}) ===")
    for nome, func in metodos.items():
      _, y_num = func(t0, tf, y0, h)
      tem_sinal_negativo = np.any(y_num < 0.0)
      print(
          f"  {nome:12s} -> y(2) = {y_num[-1]: .4e} | max|y| ="
          f" {np.max(np.abs(y_num)): .4e} | oscila/negativo: {tem_sinal_negativo}"
      )
    print()

  # Gráfico 2x2 comparando todos os métodos para cada passo h
  fig, axes = plt.subplots(2, 2, figsize=(13, 9), sharex=True)
  axes = axes.ravel()

  for ax, h in zip(axes, passos):
    ax.plot(t_fino, y_fino, "k-", linewidth=2.0, label="Exata")
    for nome, func in metodos.items():
      t_num, y_num = func(t0, tf, y0, h)
      ax.plot(t_num, y_num, marker="o", markersize=4, linewidth=1.3, label=nome)

    ax.axhline(0.0, color="gray", linewidth=0.8, alpha=0.6)
    ax.set_title(f"Passo h = {h}")
    ax.set_ylabel("y(t)")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(fontsize=8)

  for ax in axes[2:]:
    ax.set_xlabel("t")

  plt.suptitle(
      r"PVI: $y'(t) = -15y(t)$, $y(0) = 1$ em $[0, 2]$", fontsize=13
  )
  plt.tight_layout()
  plt.show()

  # Gráfico específico para o item 5: Euler vs. RK4 com h = 0.2
  t_eu, y_eu = euler(t0, tf, y0, 0.2)
  t_rk, y_rk = rk4(t0, tf, y0, 0.2)

  plt.figure(figsize=(8, 5))
  plt.plot(t_fino, y_fino, "k-", linewidth=2.0, label="Exata")
  plt.plot(t_rk, y_rk, "d-", markersize=5, label="RK4 (h = 0.2)")
  plt.plot(t_eu, y_eu, "o--", markersize=5, label="Euler (h = 0.2)")
  plt.axhline(0.0, color="gray", linewidth=0.8, alpha=0.6)
  plt.title("Comparação: Euler vs. RK4 para h = 0.2")
  plt.xlabel("t")
  plt.ylabel("y(t)")
  plt.grid(True, linestyle="--", alpha=0.4)
  plt.legend()
  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  main()