import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_data(input_csv, output_csv):
    """Melakukan normalisasi data."""
    data = pd.read_csv(input_csv)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.iloc[:, 1:])  # Kolom fitur
    scaled_df = pd.DataFrame(scaled_data, columns=data.columns[1:])
    scaled_df.insert(0, 'Label', data.iloc[:, 0])  # Tambahkan kembali label
    scaled_df.to_csv(output_csv, index=False)
    print(f"Scaled data saved to {output_csv}")

# Contoh penggunaan
if __name__ == "__main__":
    input_csv = "D:/IPSD/WhatsApp-Group-Analysis-with-Clustering/data/data_group.csv"
    output_csv = "D:/IPSD/WhatsApp-Group-Analysis-with-Clustering/data/scaled_data_group.csv"
    scale_data(input_csv, output_csv)
