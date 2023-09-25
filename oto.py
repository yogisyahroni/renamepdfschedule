import fitz
import os

# Direktori yang berisi file PDF
directory = 'C:/Users/yogis/Documents/DATA RAR/04 SEPTEMBER 2023'

# Pindah ke direktori PDF
os.chdir(directory)

pdf_list = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[0].get_text()
        lines = text.split("\n")
        no_surat = None

        # Cari baris yang mengandung "Nomor Surat"
        for line in lines:
            if "No." in line:
                parts = line.split(".")
                if len(parts) > 1:
                    no_surat = parts[1].strip().replace("/", "-")
                break

        # Jika nomor dokumen ditemukan, gunakan sebagai nama file baru
        if no_surat:
            new_file_name = f"No.{no_surat}.pdf"
            
            # Cek apakah nama file sudah ada di direktori
            if not os.path.exists(new_file_name):
                pdf_obj.close()
                # Ubah nama file
                os.rename(pdf, new_file_name)
            else:
                print(f"File {new_file_name} sudah ada. Pengubahan nama dibatalkan.")
        else:
            print(f"Tidak ada nomor dokumen yang ditemukan dalam file {pdf}.")

print("Pengubahan nama selesai.")