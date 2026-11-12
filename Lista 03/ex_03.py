import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = np.array([-1.0, 2.0, 4.0])
y = np.array([-32.0, 1.0, 3.0])

def E(a, b):
    """Soma dos quadrados dos resíduos."""
    return np.sum((y - a*np.exp(b*x))**2)

try:
    with np.errstate(invalid="raise"):
        np.log(y)
except FloatingPointError:
    print("Método 1: inviável, pois ln(-32) não é real")

def gauss_newton(a, b, itmax=200, tol=1e-12):
    hist = [(a, b, E(a, b))]
    for _ in range(itmax):
        g = np.exp(b*x)
        r = y - a*g                                   
        J = np.column_stack([g, a*x*g])              
        try:
            d = np.linalg.solve(J.T @ J, J.T @ r)     
        except np.linalg.LinAlgError:
            break
        t = 1.0                                       
        while E(a + t*d[0], b + t*d[1]) > E(a, b) and t > 1e-10:
            t /= 2
        a, b = a + t*d[0], b + t*d[1]
        hist.append((a, b, E(a, b)))
        if np.linalg.norm(t*d) < tol:
            break
    return a, b, hist

res = {}
for a0, b0 in [(1.0, 0.5), (-1.0, -1.0), (-30.0, -0.5)]:
    a, b, h = gauss_newton(a0, b0)
    res[(a0, b0)] = (a, b)
    print(f"Gauss-Newton ({a0},{b0}) -> a={a:.6g} b={b:.6g} E={E(a,b):.6f} it={len(h)-1}")

for b in (-3, -6, -10):
    print(f"a=-32e^b, b={b}: E={E(-32*np.exp(b), b):.8f}")

xx = np.linspace(-1.6, 4.6, 800)
aP, bP = res[(1.0, 0.5)]
aN, bN = res[(-1.0, -1.0)]
fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
for k in (0, 1):
    ax[k].scatter(x, y, c="red", s=70, zorder=5, label="Dados: (-1,-32), (2,1), (4,3)")
    ax[k].plot(xx, -2*xx**2+13*xx-17, color="green", lw=1.6, alpha=.7, label=r"Lagrange $p_2(x)=-2x^2+13x-17$")
    ax[k].plot(xx, aN*np.exp(bN*xx), "b--", lw=2, label=rf"Gauss-Newton, início $(-1;-1)$: $a\approx{aN:.2f},\ b\approx{bN:.2f}$ ($E\approx10{{,}}07$)".replace(".", ",", 0))
    ax[k].plot(xx, aP*np.exp(bP*xx), color="orange", lw=2, label=rf"Gauss-Newton, início $(1;0{{,}}5)$: $a\approx{aP:.4f},\ b\approx{bP:.2f}$ ($E\approx1024{{,}}8$)")
    ax[k].axhline(0, c="k", lw=.8); ax[k].axvline(0, c="k", lw=.8)
    ax[k].grid(ls=":", alpha=.6); ax[k].set_xlabel("x"); ax[k].set_ylabel("y")
ax[0].set_ylim(-36, 8); ax[0].set_title("(a) Visão geral (escala linear)")
ax[0].legend(fontsize=7, loc="lower right")
ax[1].set_xlim(1.2, 4.6); ax[1].set_ylim(-1, 8); ax[1].set_title("(b) Zoom em x ≥ 1,2: comportamento nos pontos positivos")
plt.tight_layout(); plt.savefig("fig1.png", dpi=170); plt.close()