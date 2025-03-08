STEP BY STEP COMMANDS to convert JPG to PDF

- mkdir JPGToPDFConverter

- mkdir JPEGImages

- mv /Users/UserNamer/Downloads/file.jpg   /Users/UserNamer/Downloads/JPEGImages/

- cd JPGToPDFConverter

- python3 -m venv venv

- source venv/bin/activate

- pip3 install Pillow reportlab

- mkdir src

- touch src/__init__.py

- touch src/jpg_to_pdf.py

- nano src/jpg_to_pdf.py

- python3 src/jpg_to_pdf.py

In the file pdf_to_jpeg.py change the UserName and replace the name of the files. 
