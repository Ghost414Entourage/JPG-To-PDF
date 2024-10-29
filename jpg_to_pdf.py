from PIL import Image
import os
from reportlab.pdfgen import canvas

def jpg_to_pdf(image_folder, output_pdf):
    # Get all JPEG files from the folder
    images = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg'))]
    images.sort()  # Sort files if needed

    # Create a PDF
    c = canvas.Canvas(output_pdf)

    for image_file in images:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        
        # Convert the image to RGB if it's not in that mode
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Get the dimensions
        width, height = image.size

        # Add the image to the PDF
        c.drawImage(image_path, 0, 0, width, height)
        c.showPage()  # Go to the next page

    c.save()  # Save the PDF

if __name__ == "__main__":
    image_folder = '/Users/UserName/Downloads/JPEGImages'  # Folder containing JPEG files
    output_pdf = '/Users/UserName/Downloads/ConvertedImages.pdf'  # Output PDF file
    jpg_to_pdf(image_folder, output_pdf)
    print(f"Converted images from {image_folder} to {output_pdf}")
