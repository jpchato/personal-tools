import PyPDF2

def remove_pdf_password(input_pdf_path, output_pdf_path, password):
    try:
        # Open the encrypted PDF file
        with open(input_pdf_path, 'rb') as input_file:
            reader = PyPDF2.PdfReader(input_file)

            # Check if the PDF file is encrypted
            if reader.is_encrypted:
                # Decrypt the PDF file with the provided password
                reader.decrypt(password)

                # Create a PdfWriter object
                writer = PyPDF2.PdfWriter()

                # Add all pages from the reader to the writer
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])

                # Write the decrypted PDF to the output file
                with open(output_pdf_path, 'wb') as output_file:
                    writer.write(output_file)

                print(f"Password removed successfully. Decrypted PDF saved as '{output_pdf_path}'.")

            else:
                print("The PDF file is not encrypted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_pdf_path = 'path/to/encrypted.pdf'
output_pdf_path = 'path/to/decrypted.pdf'
password = 'your_password'

remove_pdf_password(input_pdf_path="veterans_letter.pdf", output_pdf_path="veterans_letter_pena.pdf", password="2-29672625665")
