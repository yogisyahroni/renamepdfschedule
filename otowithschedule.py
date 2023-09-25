import fitz
import os
import schedule
import time

# Global flag to track renaming progress
all_files_renamed = False

def rename_pdfs():
    global all_files_renamed
    
    directory = 'C:/Users/yogis/Documents/DATA RAR/ALL PDF SEPT 2023'
    os.chdir(directory)
    pdf_list = [file for file in os.listdir() if file.endswith(".pdf")]

    # Track the number of successfully renamed files
    renamed_count = 0

    for pdf in pdf_list:
        with fitz.open(pdf) as pdf_obj:
            text = pdf_obj[0].get_text()
            lines = text.split("\n")
            no_surat = None

        for line in lines:
            if "No." in line:
                parts = line.split(".")
                if len(parts) > 1:
                    no_surat = parts[1].strip().replace("/", "-")
                break

        if no_surat:
            new_file_name = f"NO.{no_surat}.pdf"
            
            # Check if the file name already exists in the directory
            if not os.path.exists(new_file_name):
                # Rename the file
                os.rename(pdf, new_file_name)
                renamed_count += 1
            else:
                print(f"File {new_file_name} already exists. Rename operation canceled.")
        else:
            print(f"No document number found in the file {pdf}.")

    # Check if all files have been renamed
    if renamed_count == len(pdf_list):
        all_files_renamed = True
        print("All files have been renamed.")   

# Schedule the task to run every second
schedule.every(3).seconds.do(rename_pdfs)

while not all_files_renamed:
    schedule.run_pending()
    time.sleep(1)
