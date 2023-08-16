from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_to_pdf(images, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    for img in images:
        c.drawImage(img, 0, 0, width, height)
        c.showPage()
    c.save()

def convert_folder_to_pdf(folder_path, pdf_filename):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    image_paths = [os.path.join(folder_path, img) for img in image_files]
    convert_to_pdf(image_paths, pdf_filename)

def main():
    root_folder = str(input("Insira o caminho para o diretorio root: "))
    pdf_output_folder = str(input("Insira o caminho para o diretorio destinho: "))

    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            pdf_filename = os.path.join(pdf_output_folder, f"{folder_name}.pdf")
            convert_folder_to_pdf(folder_path, pdf_filename)
            print(f"Converted {folder_name} to {pdf_filename}")

if __name__ == "__main__":
    main()
