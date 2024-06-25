remove_pw_from_pdf.py

Explanation
Import the PyPDF2 library: This library is used to work with PDF files.
Open the encrypted PDF file: The with open(input_pdf_path, 'rb') as input_file statement opens the encrypted PDF file in read-binary mode.
Check if the PDF is encrypted: reader.is_encrypted checks if the PDF file is encrypted.
Decrypt the PDF file: reader.decrypt(password) attempts to decrypt the PDF file using the provided password.
Create a PdfWriter object: This object is used to write the decrypted content to a new PDF file.
Add all pages to the writer: The for loop adds all pages from the reader to the writer.
Write the decrypted PDF to a new file: The with open(output_pdf_path, 'wb') as output_file statement writes the decrypted PDF content to a new file.
Replace 'path/to/encrypted.pdf', 'path/to/decrypted.pdf', and 'your_password' with your actual file paths and password.

This script will remove the password protection from the PDF and save a new decrypted copy. If you have any issues or further questions, feel free to ask!