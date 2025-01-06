import re

def clean_whatsapp_chat(input_path, output_path):
    """Bersihkan data chat WhatsApp."""
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        # Hapus baris otomatis atau tidak relevan
        if any(keyword in line for keyword in ["Pesan ini dihapus", "<Media tidak disertakan>", "end-to-end"]):
            continue
        # Hapus metadata tambahan (opsional)
        line = re.sub(r'\d{2}/\d{2}/\d{2,4} \d{2}\.\d{2} - ', '', line)
        cleaned_lines.append(line.strip())

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_lines))
    print(f"Cleaned data saved to {output_path}")

# Contoh penggunaan
if __name__ == "__main__":
    input_path = "D:/IPSD/WhatsApp-Group-Analysis-with-Clustering/data/data_group.txt"
    output_path = "D:/IPSD/WhatsApp-Group-Analysis-with-Clustering/data/clean_data_group.txt"
    clean_whatsapp_chat(input_path, output_path)