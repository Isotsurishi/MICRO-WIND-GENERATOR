import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'MS Gothic'

R = np.array([10000, 6800, 4700, 2100, 1000, 470, 270, 200])

V = {
    "NdFeB6":     [19.633333333333336, 18.483333333333338, 18.083333333333332,
                   11.983333333333334, 6.533333333333333, 3.2, 1.641666666666667, 1.125],
    "NdFeB10":    [88.08333333333333, 77.25, 75.4,
                   45.65, 21.3, 9.866666666666667, 6.316666666666666, 3.7333333333333325],
    "NdFeB16ep":  [70.96666666666667, 70.1, 64.21666666666667,
                   40.5, 18.766666666666666, 8.233333333333333, 4.45, 3.2333333333333325],
    "NdFeB16no":  [59.45, 55.86666666666666, 50.2,
                   32.333333333333336, 15.316666666666666, 6.616666666666665, 3.3333333333333326, 2.6333333333333337],
    "Ferrite":    [39.516666666666666, 38.8, 32.06666666666666,
                   22.0, 10.183333333333334, 4.483333333333333, 2.1166666666666663, 1.6166666666666663]
}

colors = ["blue", "orange", "green", "red", "purple"]

plt.figure(figsize=(6,4))
for (label, values), color in zip(V.items(), colors):
    plt.plot(R, values, label=label, color=color, linewidth=1.5)

plt.xscale("log")
plt.xlabel("抵抗値 [Ω]")
plt.ylabel("電圧 [V]")
plt.title("1500 rpm 電圧 vs 抵抗値")
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("1500rpm_voltage.png", dpi=200)
