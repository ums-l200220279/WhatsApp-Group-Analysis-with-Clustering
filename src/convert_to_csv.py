import csv

def convert_to_csv(input_path, output_path):
    """Konversi file teks WhatsApp ke CSV dengan debugging untuk melihat data yang tidak sesuai format."""
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Sender", "Message"])  # Header CSV
        
        for line in lines:
            # Ekstraksi timestamp dan pesan
            parts = line.split(" - ", 1)
            if len(parts) == 2:
                timestamp, message = parts
                sender_message = message.split(": ", 1)
                
                if len(sender_message) == 2:
                    sender, msg = sender_message
                    writer.writerow([timestamp, sender, msg])
                else:
                    print(f"Skipping line (no sender): {line}")  # Debugging line without sender
                    writer.writerow([timestamp, "System", message])  # Jika tidak ada pengirim
            else:
                print(f"Skipping invalid line: {line}")  # Debugging invalid format

    print(f"CSV file created at {output_path}")

# Contoh penggunaan
if __name__ == "__main__":
    input_path = "D:/IPSD/WhatsApp-Group-Analysis-with-Clustering/data/clean_data_group.txt"
    output_path = "D:/IPSD/WhatsApp-Group-Analysis-with-Clustering/data/data_group.csv"
    convert_to_csv(input_path, output_path)
