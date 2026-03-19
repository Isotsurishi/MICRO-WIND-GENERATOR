import matplotlib.pyplot as plt

# 抵抗値 [Ω]
R = [10000, 6800, 4700, 2100, 1000, 470, 270, 200]

# 電圧データ（360 rpm）
V360 = {
    "NdFeB6":    [3.8, 3.6, 3.2, 2.8, 2.1, 1.3, 0.85, 0.65],
    "NdFeB10":   [20.0, 19.3, 18.4, 16.2, 11.8, 6.7, 4.1, 3.1],
    "NdFeB16ep": [18.4, 16.9, 16.4, 13.9, 9.9, 5.7, 3.5, 2.6],
    "NdFeB16no": [12.9, 12.8, 12.2, 10.8, 7.4, 4.4, 2.7, 2.0],
    "Ferrite":   [8.8, 8.4, 8.0, 6.8, 4.8, 2.9, 1.8, 1.3],
}

# 電圧データ（720 rpm）
V720 = {
    "NdFeB6":    [8.8, 8.3, 7.9, 5.7, 3.5, 1.9, 1.1, 0.8],
    "NdFeB10":   [41.5, 37.6, 36.4, 25.5, 14.8, 7.7, 4.8, 3.3],
    "NdFeB16ep": [35.0, 33.7, 31.5, 22.3, 12.7, 6.5, 3.8, 2.8],
    "NdFeB16no": [27.6, 26.4, 24.2, 17.6, 9.9, 5.1, 2.9, 2.2],
    "Ferrite":   [18.5, 18.0, 15.6, 11.6, 6.5, 3.4, 1.9, 1.4],
}

def calc_power(V_dict):
    P_dict = {}
    for name, vs in V_dict.items():
        P = []
        for v, r in zip(vs, R):
            P.append((v ** 2) / r)
        P_dict[name] = P
    return P_dict

P360 = calc_power(V360)
P720 = calc_power(V720)

colors = {
    "NdFeB6": "C0",
    "NdFeB10": "C1",
    "NdFeB16ep": "C2",
    "NdFeB16no": "C3",
    "Ferrite": "C4",
}

# 360 rpm
plt.figure(figsize=(6, 4))
for name, P in P360.items():
    plt.plot(R, P, marker="o", label=name, color=colors[name])
plt.xlabel("Resistance [Ω]")
plt.ylabel("Power [W]")
plt.title("Resistance vs Power (360 rpm)")
plt.grid(True)
plt.legend()
plt.xscale("log")  # 昨日のグラフが対数ならそのまま、違えば消してOK
plt.tight_layout()
plt.savefig("R_vs_P_360rpm.png", dpi=200)

# 720 rpm
plt.figure(figsize=(6, 4))
for name, P in P720.items():
    plt.plot(R, P, marker="o", label=name, color=colors[name])
plt.xlabel("Resistance [Ω]")
plt.ylabel("Power [W]")
plt.title("Resistance vs Power (720 rpm)")
plt.grid(True)
plt.legend()
plt.xscale("log")  # 同上
plt.tight_layout()
plt.savefig("R_vs_P_720rpm.png", dpi=200)

plt.show()
