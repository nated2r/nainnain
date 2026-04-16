import sys
import os

def extract_pdf_to_images(pdf_path, output_dir):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("缺少 PyMuPDF 套件，正在嘗試安裝...")
        os.system(f"{sys.executable} -m pip install PyMuPDF")
        import fitz

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"正在開啟 PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # 提高解析度 (zoom_x, zoom_y)
        zoom_x = 2.0  
        zoom_y = 2.0  
        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        output_file = os.path.join(output_dir, f"page_{page_num + 1:02d}.jpg")
        pix.save(output_file)
        print(f"已儲存: {output_file}")
        
    print("PDF 轉換完成！")

if __name__ == "__main__":
    pdf_path = "/Users/chad/Desktop/一頁網站/藍藻菌一頁式.pdf"
    output_dir = "/Users/chad/Desktop/一頁網站/assets"
    extract_pdf_to_images(pdf_path, output_dir)
