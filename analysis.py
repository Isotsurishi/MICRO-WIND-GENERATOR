import numpy as np
import matplotlib.pyplot as plt

# 抵抗値と各データセットの電圧データ
R_load = np.array([10000, 6800, 4700, 2100, 1000, 470, 270, 200], dtype=float)

datasets = {
    "NdFeB6_360":      {"rpm": 360, "V": np.array([3.8, 3.6, 3.2, 2.8, 2.1, 1.3, 0.85, 0.65])},
    "NdFeB6_720":      {"rpm": 720, "V": np.array([8.8, 8.3, 7.9, 5.7, 3.5, 1.9, 1.1, 0.8])},
    "NdFeB10_360":     {"rpm": 360, "V": np.array([20.0, 19.3, 18.4, 16.2, 11.8, 6.7, 4.1, 3.1])},
    "NdFeB10_720":     {"rpm": 720, "V": np.array([41.5, 37.6, 36.4, 25.5, 14.8, 7.7, 4.8, 3.3])},
    "NdFeB16ep_360":   {"rpm": 360, "V": np.array([18.4, 16.9, 16.4, 13.9, 9.9, 5.7, 3.5, 2.6])},
    "NdFeB16ep_720":   {"rpm": 720, "V": np.array([35.0, 33.7, 31.5, 22.3, 12.7, 6.5, 3.8, 2.8])},
    "NdFeB16no_360":   {"rpm": 360, "V": np.array([12.9, 12.8, 12.2, 10.8, 7.4, 4.4, 2.7, 2.0])},
    "NdFeB16no_720":   {"rpm": 720, "V": np.array([27.6, 26.4, 24.2, 17.6, 9.9, 5.1, 2.9, 2.2])},
    "Ferrite_360":     {"rpm": 360, "V": np.array([8.8, 8.4, 8.0, 6.8, 4.8, 2.9, 1.8, 1.3])},
    "Ferrite_720":     {"rpm": 720, "V": np.array([18.5, 18.0, 15.6, 11.6, 6.5, 3.4, 1.9, 1.4])},
}

# ---------- グラフ生成 ----------

def plot_all():
    plt.figure(figsize=(8, 6))
    for name, d in datasets.items():
        plt.plot(R_load, d["V"], marker="o", label=name)
    plt.xscale("log")
    plt.xlabel("Load resistance [Ω]")
    plt.ylabel("Voltage [V]")
    plt.title("All datasets (360 & 720 rpm)")
    plt.grid(True, which="both", ls="--", alpha=0.4)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig("all_datasets.png", dpi=200)

def plot_by_rpm(target_rpm, filename):
    plt.figure(figsize=(8, 6))
    for name, d in datasets.items():
        if d["rpm"] == target_rpm:
            plt.plot(R_load, d["V"], marker="o", label=name)
    plt.xscale("log")
    plt.xlabel("Load resistance [Ω]")
    plt.ylabel("Voltage [V]")
    plt.title(f"Datasets at {target_rpm} rpm")
    plt.grid(True, which="both", ls="--", alpha=0.4)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(filename, dpi=200)

def plot_pairs():
    pairs = [
        ("NdFeB6_360",    "NdFeB6_720"),
        ("NdFeB10_360",   "NdFeB10_720"),
        ("NdFeB16ep_360", "NdFeB16ep_720"),
        ("NdFeB16no_360", "NdFeB16no_720"),
        ("Ferrite_360",   "Ferrite_720"),
    ]
    for a, b in pairs:
        plt.figure(figsize=(8, 6))
        for name in (a, b):
            d = datasets[name]
            plt.plot(R_load, d["V"], marker="o", label=f"{name} ({d['rpm']} rpm)")
        plt.xscale("log")
        plt.xlabel("Load resistance [Ω]")
        plt.ylabel("Voltage [V]")
        plt.title(f"{a} vs {b}")
        plt.grid(True, which="both", ls="--", alpha=0.4)
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(f"{a}_vs_{b}.png", dpi=200)

# ---------- メイン処理 ----------

if __name__ == "__main__":
    plot_all()
    plot_by_rpm(360, "rpm_360.png")
    plot_by_rpm(720, "rpm_720.png")
    plot_pairs()
    print("PNG グラフを生成しました。")
