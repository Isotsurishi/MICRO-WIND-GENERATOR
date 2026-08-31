import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# ============================
# 1. データ入力（英信さんのデータ）
# ============================

data_420 = pd.DataFrame({
    "R":[9910,6740,4745,2128,990,473.4,267.7,197.3,102.4,46.4,22.8,10.6],
    "Neo10":[8.30,8.12,8.23,7.72,6.96,6.28,6.11,5.612,3.912,2.166,1.108,0.5123],
    "Neo12":[9.31,9.41,9.13,8.68,8.39,7.98,6.66,6.29,4.489,2.483,1.280,0.6000],
    "Neo13":[9.12,8.97,9.22,8.97,8.58,8.35,7.17,6.34,4.698,2.546,1.297,0.6112]
})

data_840 = pd.DataFrame({
    "R":[9910,6740,4745,2128,990,473.4,267.7,197.3,102.4,46.4,22.8,10.6],
    "Neo10":[16.96,16.75,17.04,15.84,15.52,13.17,10.26,8.35,4.993,2.436,1.194,0.549],
    "Neo12":[18.91,18.27,18.67,18.01,17.41,14.78,11.65,9.54,5.784,2.790,1.378,0.633],
    "Neo13":[19.35,19.69,19.57,18.92,18.31,15.79,11.93,9.78,5.854,2.836,1.398,0.644]
})

data_1260 = pd.DataFrame({
    "R":[9910,6740,4745,2128,990,473.4,267.7,197.3,102.4,46.4,22.8,10.6],
    "Neo10":[25.03,25.52,26.11,25.06,22.34,17.17,11.94,9.51,5.336,2.496,1.212,0.555],
    "Neo12":[28.77,28.75,28.37,28.31,24.87,19.55,13.58,10.86,6.110,2.862,1.396,0.641],
    "Neo13":[30.08,29.87,30.12,28.35,26.33,20.26,13.74,11.08,6.201,2.909,1.418,0.650]
})

datasets = {
    "420rpm": data_420,
    "840rpm": data_840,
    "1260rpm": data_1260
}

# ============================
# 2. グラフをPDFにバラバラ出力
# ============================

def save_voltage_pdf(label, df):
    df["logR"] = np.log10(df["R"])
    filename = f"voltage_{label}.pdf"

    with PdfPages(filename) as pdf:
        plt.figure(figsize=(8,6))
        plt.plot(df["logR"], df["Neo10"], marker="o", label="Neo10")
        plt.plot(df["logR"], df["Neo12"], marker="o", label="Neo12")
        plt.plot(df["logR"], df["Neo13"], marker="o", label="Neo13")
        plt.xlabel("log10(Resistance [Ω])")
        plt.ylabel("Voltage [V]")
        plt.title(f"Voltage vs log10(Resistance) - {label}")
        plt.grid(True)
        plt.legend()
        pdf.savefig()
        plt.close()

    print(f"Voltage PDF 出力完了：{filename}")

def save_power_pdf(label, df):
    df["logR"] = np.log10(df["R"])
    df["P_Neo10"] = df["Neo10"]**2 / df["R"]
    df["P_Neo12"] = df["Neo12"]**2 / df["R"]
    df["P_Neo13"] = df["Neo13"]**2 / df["R"]

    filename = f"power_{label}.pdf"

    with PdfPages(filename) as pdf:
        plt.figure(figsize=(8,6))
        plt.plot(df["logR"], df["P_Neo10"], marker="o", label="Neo10")
        plt.plot(df["logR"], df["P_Neo12"], marker="o", label="Neo12")
        plt.plot(df["logR"], df["P_Neo13"], marker="o", label="Neo13")
        plt.xlabel("log10(Resistance [Ω])")
        plt.ylabel("Power [W]")
        plt.title(f"Power vs log10(Resistance) - {label}")
        plt.grid(True)
        plt.legend()
        pdf.savefig()
        plt.close()

    print(f"Power PDF 出力完了：{filename}")

# ============================
# 3. 実行
# ============================

for label, df in datasets.items():
    save_voltage_pdf(label, df)
    save_power_pdf(label, df)

print("すべてのPDF出力が完了しました。")
