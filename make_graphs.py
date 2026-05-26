import numpy as np
import matplotlib.pyplot as plt

# 1200rpm 実測データ
R = np.array([9910, 6740, 4745, 2128, 990, 473.4, 267.7, 197.3, 102.4, 46.4, 22.8, 10.6])

neo6 = np.array([7.48, 7.08, 6.98, 6.05, 4.548, 2.634, 1.603, 1.203, 0.634, 0.2878, 0.1390, 0.0630])
neo10 = np.array([39.30, 36.18, 35.87, 31.58, 21.98, 12.83, 7.70, 5.798, 3.047, 1.385, 0.677, 0.3047])
neo16_no = np.array([27.84, 27.06, 25.36, 21.69, 15.12, 8.66, 5.160, 3.875, 2.037, 0.924, 0.4449, 0.2035])
neo16_ss = np.array([39.36, 37.56, 36.29, 33.38, 22.49, 12.79, 7.68, 5.776, 3.041, 1.380, 0.665, 0.3024])
ferrite = np.array([22.84, 23.65, 22.87, 19.18, 13.54, 7.59, 4.534, 3.391, 1.786, 0.813, 0.3915, 0.1794])

plt.figure(figsize=(10,6))

plt.plot(np.log10(R), neo6, label="Neo6 SandIron")
plt.plot(np.log10(R), neo10, label="Neo10 SS400")
plt.plot(np.log10(R), neo16_no, label="Neo16 No Yoke")
plt.plot(np.log10(R), neo16_ss, label="Neo16 SS400")
plt.plot(np.log10(R), ferrite, label="Ferrite19 SS400")

plt.xlabel("log10(Resistance [Ω])")
plt.ylabel("Voltage [V]")
plt.title("Voltage vs log10(Resistance) - 1200rpm")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("1200rpm.png", dpi=300)
plt.close()


import numpy as np
import matplotlib.pyplot as plt

# 1800rpm 実測データ
R = np.array([9910, 6740, 4745, 2128, 990, 473.4, 267.7, 197.3, 102.4, 46.4, 22.8, 10.6])

neo6 = np.array([11.24, 10.47, 9.98, 8.57, 5.386, 2.865, 1.672, 1.242, 0.646, 0.2953, 0.1406, 0.0641])
neo10 = np.array([57.64, 53.82, 50.75, 41.20, 25.24, 13.52, 7.90, 5.884, 3.072, 1.391, 0.669, 0.3056])
neo16_no = np.array([39.40, 38.47, 37.09, 28.09, 17.14, 9.08, 5.310, 3.946, 2.057, 0.930, 0.4471, 0.2043])
neo16_ss = np.array([59.06, 56.61, 53.74, 41.76, 25.04, 13.45, 7.86, 5.858, 3.062, 1.387, 0.668, 0.3051])
ferrite = np.array([35.94, 33.52, 33.52, 24.40, 15.12, 7.96, 4.652, 3.462, 1.805, 0.817, 0.3931, 0.1802])

plt.figure(figsize=(10,6))

plt.plot(np.log10(R), neo6, label="Neo6 SandIron")
plt.plot(np.log10(R), neo10, label="Neo10 SS400")
plt.plot(np.log10(R), neo16_no, label="Neo16 No Yoke")
plt.plot(np.log10(R), neo16_ss, label="Neo16 SS400")
plt.plot(np.log10(R), ferrite, label="Ferrite19 SS400")

plt.xlabel("log10(Resistance [Ω])")
plt.ylabel("Voltage [V]")
plt.title("Voltage vs log10(Resistance) - 1800rpm")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("1800rpm.png", dpi=300)
plt.close()


import numpy as np
import matplotlib.pyplot as plt

# 共通の抵抗値
R = np.array([9910, 6740, 4745, 2128, 990, 473.4, 267.7, 197.3, 102.4, 46.4, 22.8, 10.6])
logR = np.log10(R)

# ---------------------------------------------------------
# 360 rpm（コア長 23mm）
# ---------------------------------------------------------
neo6_360_23 = np.array([0.2017, 0.1964, 0.1723, 0.1314, 0.1251, 0.1053, 0.0937, 0.0723, 0.0635, 0.0324, 0.0201, 0.0097])
neo10_360_23 = np.array([2.386, 2.327, 2.278, 2.263, 2.115, 2.084, 2.051, 1.923, 1.667, 1.324, 0.995, 0.5102])
neo16_no_360_23 = np.array([1.656, 1.612, 1.592, 1.486, 1.394, 1.279, 1.202, 1.194, 1.082, 0.802, 0.5657, 0.3072])
neo16_ss_360_23 = np.array([2.598, 2.498, 2.476, 2.428, 2.362, 2.236, 2.138, 2.057, 1.823, 1.406, 1.001, 0.5376])
ferrite18_360_23 = np.array([1.645, 1.551, 1.486, 1.398, 1.318, 1.277, 1.234, 1.158, 1.030, 0.789, 0.5397, 0.2987])

# ---------------------------------------------------------
# 720 rpm（コア長 23mm）
# ---------------------------------------------------------
neo6_720_23 = np.array([0.831, 0.806, 0.752, 0.713, 0.652, 0.632, 0.5483, 0.5236, 0.4476, 0.2943, 0.1875, 0.0996])
neo10_720_23 = np.array([5.692, 5.664, 5.484, 5.423, 5.173, 5.139, 4.871, 4.712, 3.998, 2.912, 1.772, 0.904])
neo16_no_720_23 = np.array([4.186, 4.083, 4.050, 3.986, 3.845, 3.716, 3.498, 3.394, 2.852, 2.016, 1.212, 0.627])
neo16_ss_720_23 = np.array([6.110, 6.098, 5.986, 5.602, 5.598, 5.386, 5.182, 5.046, 4.546, 3.080, 1.853, 0.948])
ferrite18_720_23 = np.array([3.960, 3.912, 3.874, 3.798, 3.602, 3.442, 3.332, 3.104, 2.723, 1.901, 1.153, 0.5876])

# ---------------------------------------------------------
# 360 rpm（コア長 60mm）
# ---------------------------------------------------------
neo6_360_60 = np.array([1.621, 1.560, 1.468, 1.334, 1.302, 1.078, 0.794, 0.691, 0.3984, 0.2046, 0.1023, 0.0472])
neo10_360_60 = np.array([11.23, 10.85, 10.52, 10.39, 9.62, 7.65, 5.934, 4.722, 2.734, 1.326, 0.651, 0.2997])
neo16_no_360_60 = np.array([7.52, 7.32, 7.28, 7.03, 6.03, 5.067, 3.645, 3.017, 1.742, 0.910, 0.4406, 0.2015])
neo16_ss_360_60 = np.array([10.58, 10.53, 10.13, 10.05, 9.14, 7.40, 5.497, 4.456, 2.615, 1.241, 0.6096, 0.2812])
ferrite18_360_60 = np.array([6.28, 6.010, 5.770, 5.550, 5.081, 4.073, 3.058, 2.486, 1.437, 0.694, 0.3434, 0.1581])

# ---------------------------------------------------------
# 720 rpm（コア長 60mm）
# ---------------------------------------------------------
neo6_720_60 = np.array([4.086, 3.945, 3.836, 3.364, 2.953, 2.009, 1.365, 1.061, 0.5873, 0.2726, 0.1326, 0.0612])
neo10_720_60 = np.array([22.90, 22.53, 22.02, 21.46, 17.12, 11.52, 7.46, 5.694, 3.080, 1.419, 0.686, 0.3142])
neo16_no_720_60 = np.array([15.44, 15.02, 14.67, 13.92, 11.67, 7.53, 4.812, 3.698, 1.988, 0.841, 0.4162, 0.1904])
neo16_ss_720_60 = np.array([22.50, 21.23, 21.98, 20.66, 16.72, 10.97, 7.00, 5.378, 2.880, 1.324, 0.640, 0.2929])
ferrite18_720_60 = np.array([13.26, 13.01, 12.48, 11.60, 9.62, 6.21, 4.023, 3.073, 1.656, 0.759, 0.368, 0.1684])

# ---------------------------------------------------------
# 1200 rpm（コア長 60mm）
# ---------------------------------------------------------
neo6_1200_60 = np.array([7.48, 7.08, 6.98, 6.05, 4.548, 2.634, 1.603, 1.203, 0.634, 0.2878, 0.1390, 0.0630])
neo10_1200_60 = np.array([39.30, 36.18, 35.87, 31.58, 21.98, 12.83, 7.70, 5.798, 3.047, 1.385, 0.677, 0.3047])
neo16_no_1200_60 = np.array([27.84, 27.06, 25.36, 21.69, 15.12, 8.66, 5.160, 3.875, 2.037, 0.924, 0.4449, 0.2035])
neo16_ss_1200_60 = np.array([39.36, 37.56, 36.29, 33.38, 22.49, 12.79, 7.68, 5.776, 3.041, 1.380, 0.665, 0.3024])
ferrite18_1200_60 = np.array([22.84, 23.65, 22.87, 19.18, 13.54, 7.59, 4.534, 3.391, 1.786, 0.813, 0.3915, 0.1794])

# ---------------------------------------------------------
# 1800 rpm（コア長 60mm）
# ---------------------------------------------------------
neo6_1800_60 = np.array([11.24, 10.47, 9.98, 8.57, 5.386, 2.865, 1.672, 1.242, 0.646, 0.2953, 0.1406, 0.0641])
neo10_1800_60 = np.array([57.64, 53.82, 50.75, 41.2, 25.24, 13.52, 7.90, 5.884, 3.072, 1.391, 0.669, 0.3056])
neo16_no_1800_60 = np.array([39.40, 38.47, 37.09, 28.09, 17.14, 9.08, 5.310, 3.946, 2.057, 0.930, 0.4471, 0.2043])
neo16_ss_1800_60 = np.array([59.06, 56.61, 53.74, 41.76, 25.04, 13.45, 7.86, 5.858, 3.062, 1.387, 0.668, 0.3051])
ferrite18_1800_60 = np.array([35.94, 33.52, 33.52, 24.40, 15.12, 7.96, 4.652, 3.462, 1.805, 0.817, 0.3931, 0.1802])

# ---------------------------------------------------------
# 抵抗–電圧グラフ（4枚）
# 360 / 720 rpm は 23mm と 60mm の両方を重ねて表示
# ---------------------------------------------------------

def plot_voltage_360():
    plt.figure(figsize=(10, 6))
    # 23mm（実験1）
    plt.plot(logR, neo6_360_23,  color="blue",   linestyle="--", linewidth=2, label="Neo6 SandIron 23mm")
    plt.plot(logR, neo10_360_23, color="red",    linestyle="--", linewidth=2, label="Neo10 SS400 23mm")
    plt.plot(logR, neo16_no_360_23, color="green", linestyle="--", linewidth=2, label="Neo16 NoYoke 23mm")
    plt.plot(logR, neo16_ss_360_23, color="orange", linestyle="--", linewidth=2, label="Neo16 SS400 23mm")
    plt.plot(logR, ferrite18_360_23, color="purple", linestyle="--", linewidth=2, label="Ferrite18 SS400 23mm")
    # 60mm（実験2）
    plt.plot(logR, neo6_360_60,  color="blue",   linewidth=2, label="Neo6 SandIron 60mm")
    plt.plot(logR, neo10_360_60, color="red",    linewidth=2, label="Neo10 SS400 60mm")
    plt.plot(logR, neo16_no_360_60, color="green", linewidth=2, label="Neo16 NoYoke 60mm")
    plt.plot(logR, neo16_ss_360_60, color="orange", linewidth=2, label="Neo16 SS400 60mm")
    plt.plot(logR, ferrite18_360_60, color="purple", linewidth=2, label="Ferrite18 SS400 60mm")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Voltage [V]")
    plt.title("Voltage vs log10(Resistance) - 360rpm")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("voltage_360rpm.png", dpi=300)
    plt.close()

def plot_voltage_720():
    plt.figure(figsize=(10, 6))
    # 23mm
    plt.plot(logR, neo6_720_23,  color="blue",   linestyle="--", linewidth=2, label="Neo6 SandIron 23mm")
    plt.plot(logR, neo10_720_23, color="red",    linestyle="--", linewidth=2, label="Neo10 SS400 23mm")
    plt.plot(logR, neo16_no_720_23, color="green", linestyle="--", linewidth=2, label="Neo16 NoYoke 23mm")
    plt.plot(logR, neo16_ss_720_23, color="orange", linestyle="--", linewidth=2, label="Neo16 SS400 23mm")
    plt.plot(logR, ferrite18_720_23, color="purple", linestyle="--", linewidth=2, label="Ferrite18 SS400 23mm")
    # 60mm
    plt.plot(logR, neo6_720_60,  color="blue",   linewidth=2, label="Neo6 SandIron 60mm")
    plt.plot(logR, neo10_720_60, color="red",    linewidth=2, label="Neo10 SS400 60mm")
    plt.plot(logR, neo16_no_720_60, color="green", linewidth=2, label="Neo16 NoYoke 60mm")
    plt.plot(logR, neo16_ss_720_60, color="orange", linewidth=2, label="Neo16 SS400 60mm")
    plt.plot(logR, ferrite18_720_60, color="purple", linewidth=2, label="Ferrite18 SS400 60mm")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Voltage [V]")
    plt.title("Voltage vs log10(Resistance) - 720rpm")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("voltage_720rpm.png", dpi=300)
    plt.close()

def plot_voltage_1200():
    plt.figure(figsize=(10, 6))
    plt.plot(logR, neo6_1200_60,  color="blue",   linewidth=2, label="Neo6 SandIron")
    plt.plot(logR, neo10_1200_60, color="red",    linewidth=2, label="Neo10 SS400")
    plt.plot(logR, neo16_no_1200_60, color="green", linewidth=2, label="Neo16 NoYoke")
    plt.plot(logR, neo16_ss_1200_60, color="orange", linewidth=2, label="Neo16 SS400")
    plt.plot(logR, ferrite18_1200_60, color="purple", linewidth=2, label="Ferrite18 SS400")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Voltage [V]")
    plt.title("Voltage vs log10(Resistance) - 1200rpm")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("voltage_1200rpm.png", dpi=300)
    plt.close()

def plot_voltage_1800():
    plt.figure(figsize=(10, 6))
    plt.plot(logR, neo6_1800_60,  color="blue",   linewidth=2, label="Neo6 SandIron")
    plt.plot(logR, neo10_1800_60, color="red",    linewidth=2, label="Neo10 SS400")
    plt.plot(logR, neo16_no_1800_60, color="green", linewidth=2, label="Neo16 NoYoke")
    plt.plot(logR, neo16_ss_1800_60, color="orange", linewidth=2, label="Neo16 SS400")
    plt.plot(logR, ferrite18_1800_60, color="purple", linewidth=2, label="Ferrite18 SS400")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Voltage [V]")
    plt.title("Voltage vs log10(Resistance) - 1800rpm")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("voltage_1800rpm.png", dpi=300)
    plt.close()

# ---------------------------------------------------------
# 抵抗–電力グラフ（5枚）
# 60mm コアのデータを使用し、各磁石ごとに 4 rpm を重ねる
# P = V^2 / R
# ---------------------------------------------------------

def power_from_voltage(V):
    return (V ** 2) / R

def plot_power_neo6():
    plt.figure(figsize=(10, 6))
    plt.plot(logR, power_from_voltage(neo6_360_60),  color="blue",   linewidth=2, label="360rpm")
    plt.plot(logR, power_from_voltage(neo6_720_60),  color="red",    linewidth=2, label="720rpm")
    plt.plot(logR, power_from_voltage(neo6_1200_60), color="green",  linewidth=2, label="1200rpm")
    plt.plot(logR, power_from_voltage(neo6_1800_60), color="orange", linewidth=2, label="1800rpm")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Power [W]")
    plt.title("Power vs log10(Resistance) - Neo6 SandIron")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("power_neo6.png", dpi=300)
    plt.close()

def plot_power_neo10():
    plt.figure(figsize=(10, 6))
    plt.plot(logR, power_from_voltage(neo10_360_60),  color="blue",   linewidth=2, label="360rpm")
    plt.plot(logR, power_from_voltage(neo10_720_60),  color="red",    linewidth=2, label="720rpm")
    plt.plot(logR, power_from_voltage(neo10_1200_60), color="green",  linewidth=2, label="1200rpm")
    plt.plot(logR, power_from_voltage(neo10_1800_60), color="orange", linewidth=2, label="1800rpm")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Power [W]")
    plt.title("Power vs log10(Resistance) - Neo10 SS400")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("power_neo10.png", dpi=300)
    plt.close()

def plot_power_neo16_no():
    plt.figure(figsize=(10, 6))
    plt.plot(logR, power_from_voltage(neo16_no_360_60),  color="blue",   linewidth=2, label="360rpm")
    plt.plot(logR, power_from_voltage(neo16_no_720_60),  color="red",    linewidth=2, label="720rpm")
    plt.plot(logR, power_from_voltage(neo16_no_1200_60), color="green",  linewidth=2, label="1200rpm")
    plt.plot(logR, power_from_voltage(neo16_no_1800_60), color="orange", linewidth=2, label="1800rpm")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Power [W]")
    plt.title("Power vs log10(Resistance) - Neo16 NoYoke")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("power_neo16_no.png", dpi=300)
    plt.close()

def plot_power_neo16_ss():
    plt.figure(figsize=(10, 6))
    plt.plot(logR, power_from_voltage(neo16_ss_360_60),  color="blue",   linewidth=2, label="360rpm")
    plt.plot(logR, power_from_voltage(neo16_ss_720_60),  color="red",    linewidth=2, label="720rpm")
    plt.plot(logR, power_from_voltage(neo16_ss_1200_60), color="green",  linewidth=2, label="1200rpm")
    plt.plot(logR, power_from_voltage(neo16_ss_1800_60), color="orange", linewidth=2, label="1800rpm")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Power [W]")
    plt.title("Power vs log10(Resistance) - Neo16 SS400")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("power_neo16_ss.png", dpi=300)
    plt.close()

def plot_power_ferrite18():
    plt.figure(figsize=(10, 6))
    plt.plot(logR, power_from_voltage(ferrite18_360_60),  color="blue",   linewidth=2, label="360rpm")
    plt.plot(logR, power_from_voltage(ferrite18_720_60),  color="red",    linewidth=2, label="720rpm")
    plt.plot(logR, power_from_voltage(ferrite18_1200_60), color="green",  linewidth=2, label="1200rpm")
    plt.plot(logR, power_from_voltage(ferrite18_1800_60), color="orange", linewidth=2, label="1800rpm")

    plt.xlabel("log10(Resistance [Ω])")
    plt.ylabel("Power [W]")
    plt.title("Power vs log10(Resistance) - Ferrite18 SS400")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("power_ferrite18.png", dpi=300)
    plt.close()

# ---------------------------------------------------------
# すべてのグラフを生成
# ---------------------------------------------------------

def main():
    plot_voltage_360()
    plot_voltage_720()
    plot_voltage_1200()
    plot_voltage_1800()

    plot_power_neo6()
    plot_power_neo10()
    plot_power_neo16_no()
    plot_power_neo16_ss()
    plot_power_ferrite18()

    # HTML 用 <img> タグをテキストファイルに出力
    html_lines = [
        '<img src="img/voltage_360rpm.png" width="600">',
        '<img src="img/voltage_720rpm.png" width="600">',
        '<img src="img/voltage_1200rpm.png" width="600">',
        '<img src="img/voltage_1800rpm.png" width="600">',
        '',
        '<img src="img/power_neo6.png" width="600">',
        '<img src="img/power_neo10.png" width="600">',
        '<img src="img/power_neo16_no.png" width="600">',
        '<img src="img/power_neo16_ss.png" width="600">',
        '<img src="img/power_ferrite18.png" width="600">',
        ''
    ]
    with open("img_tags.html.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))

if __name__ == "__main__":
    main()
