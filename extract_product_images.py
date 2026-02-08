"""
Extract product images from PDF with specification text included.
Each product has 3 pages: main, square, wide
"""

import fitz  # PyMuPDF
import json
import os
from pathlib import Path

# Configuration
PDF_PATH = r"C:\Users\Juyong\Inbiomat\VIEW-Rev00-EXTERNAL-Specs-Tradeshow-Interactive-COMPRESSED.pdf"
OUTPUT_DIR = r"C:\Users\Juyong\Inbiomat\product_images"
METADATA_PATH = r"C:\Users\Juyong\Inbiomat\extracted_images\image_metadata.json"
PRODUCTS_INDEX_PATH = r"C:\Users\Juyong\Inbiomat\data\products-index.json"

# Product list in order (15 products)
PRODUCTS = [
    "mcd",       # MCD Apatitic Abrasive
    "mcha",      # Hydroxyapatite (MC-Type)
    "swha",      # Hydroxyapatite (HA) SWHA
    "uwha",      # Hydroxyapatite (HA) UWHA
    "hawhisk-s", # HA Whiskers
    "cad",       # Calcium Deficient HA Discs
    "had",       # Dense HA Discs
    "hadel",     # Enamel-like HA Discs
    "atcp",      # Alpha-TCP
    "ssbtcp",    # Beta-TCP (Solid-State)
    "swbtcp",    # Beta-TCP (Precipitated)
    "utcp",      # TCP (Unsintered)
    "ttcp",      # Tetracalcium Phosphate
    "s1bcp",     # BCP (Sintered)
    "u1bcp",     # BCP (Unsintered)
]

def create_output_dir():
    """Create output directory if it doesn't exist."""
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

def load_metadata():
    """Load existing image metadata to understand page structure."""
    with open(METADATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_page_as_image(doc, page_num, output_path, dpi=150):
    """
    Extract a full page as an image at specified DPI.
    Higher DPI = better quality but larger file size.
    """
    page = doc[page_num]

    # Calculate zoom to achieve desired DPI
    # Default PDF is 72 DPI, so zoom = desired_dpi / 72
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)

    # Render page to pixmap
    pix = page.get_pixmap(matrix=mat)

    # Save as PNG
    pix.save(output_path)
    print(f"  Saved: {os.path.basename(output_path)} ({pix.width}x{pix.height}px)")

def extract_product_images():
    """
    Extract images for all 15 products.
    Each product has 3 pages starting from page 2 (0-indexed: page 1).
    """
    # Create output directory
    create_output_dir()

    # Open PDF
    doc = fitz.open(PDF_PATH)
    print(f"PDF opened: {doc.page_count} pages total\n")

    # Track extraction summary
    summary = []

    # PDF structure: Page 1 is cover, products start at page 2 (0-indexed: 1)
    # Each product has 3 pages: main intro, square photo+specs, wide photo+specs
    start_page = 1  # 0-indexed (page 2 in PDF viewer)

    for idx, product_id in enumerate(PRODUCTS):
        # Calculate page numbers for this product
        base_page = start_page + (idx * 3)
        page_main = base_page
        page_square = base_page + 1
        page_wide = base_page + 2

        # Verify we're not out of bounds
        if page_wide >= doc.page_count:
            print(f"Warning: Product {product_id} pages exceed PDF bounds")
            break

        print(f"Product {idx+1}/15: {product_id.upper()}")
        print(f"  Pages: {page_main+1}, {page_square+1}, {page_wide+1} (PDF page numbers)")

        # Extract main page
        main_path = os.path.join(OUTPUT_DIR, f"{product_id}_main.png")
        extract_page_as_image(doc, page_main, main_path, dpi=150)

        # Extract square page (with specs text at bottom)
        square_path = os.path.join(OUTPUT_DIR, f"{product_id}_square.png")
        extract_page_as_image(doc, page_square, square_path, dpi=150)

        # Extract wide page (with specs text at bottom)
        wide_path = os.path.join(OUTPUT_DIR, f"{product_id}_wide.png")
        extract_page_as_image(doc, page_wide, wide_path, dpi=150)

        # Add to summary
        summary.append({
            "product_id": product_id,
            "pdf_pages": [page_main+1, page_square+1, page_wide+1],
            "files": [
                f"{product_id}_main.png",
                f"{product_id}_square.png",
                f"{product_id}_wide.png"
            ]
        })

        print()

    doc.close()

    # Save summary report
    summary_path = os.path.join(OUTPUT_DIR, "extraction_summary.json")
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({
            "total_products": len(summary),
            "total_images": len(summary) * 3,
            "extraction_date": "2026-02-08",
            "pdf_source": PDF_PATH,
            "dpi": 150,
            "products": summary
        }, f, indent=2)

    print(f"Extraction complete!")
    print(f"Total products: {len(summary)}")
    print(f"Total images: {len(summary) * 3}")
    print(f"Summary saved to: {summary_path}")

    return summary

def verify_extraction():
    """Verify all expected files were created."""
    print("\n" + "="*60)
    print("VERIFICATION")
    print("="*60)

    missing = []
    for product_id in PRODUCTS:
        for suffix in ["_main.png", "_square.png", "_wide.png"]:
            filepath = os.path.join(OUTPUT_DIR, f"{product_id}{suffix}")
            if not os.path.exists(filepath):
                missing.append(f"{product_id}{suffix}")

    if missing:
        print(f"Missing {len(missing)} files:")
        for f in missing:
            print(f"  - {f}")
    else:
        print(f"All {len(PRODUCTS) * 3} images extracted successfully!")

if __name__ == "__main__":
    print("="*60)
    print("PRODUCT IMAGE EXTRACTION")
    print("="*60)
    print(f"PDF: {PDF_PATH}")
    print(f"Products: {len(PRODUCTS)}")
    print(f"Expected images: {len(PRODUCTS) * 3}")
    print("="*60 + "\n")

    summary = extract_product_images()
    verify_extraction()
