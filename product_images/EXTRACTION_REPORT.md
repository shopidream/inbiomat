# Product Image Extraction Report

**Date:** February 8, 2026
**Source PDF:** VIEW-Rev00-EXTERNAL-Specs-Tradeshow-Interactive-COMPRESSED.pdf
**Output Directory:** C:\Users\Juyong\Inbiomat\product_images

---

## Summary

- **Total Products Extracted:** 15
- **Total Images Extracted:** 45 (3 per product)
- **Image Resolution:** 1650x1275 pixels at 150 DPI
- **Format:** PNG
- **Specification Text:** INCLUDED (square and wide images contain full specs)

---

## Extraction Details

### Image Types per Product

1. **{product_id}_main.png** - Full introduction page with product description and main image
2. **{product_id}_square.png** - Square product photo + chemical/physical specifications
3. **{product_id}_wide.png** - Wide/horizontal product photo + detailed specifications (particle sizes, etc.)

---

## Products Extracted

| # | Product ID | Product Name | PDF Pages | Images |
|---|------------|--------------|-----------|--------|
| 1 | mcd | MCD Apatitic Abrasive | 2, 3, 4 | mcd_main.png, mcd_square.png, mcd_wide.png |
| 2 | mcha | Hydroxyapatite (MC-Type) | 5, 6, 7 | mcha_main.png, mcha_square.png, mcha_wide.png |
| 3 | swha | Hydroxyapatite (HA) SWHA | 8, 9, 10 | swha_main.png, swha_square.png, swha_wide.png |
| 4 | uwha | Hydroxyapatite (HA) UWHA | 11, 12, 13 | uwha_main.png, uwha_square.png, uwha_wide.png |
| 5 | hawhisk-s | HA Whiskers | 14, 15, 16 | hawhisk-s_main.png, hawhisk-s_square.png, hawhisk-s_wide.png |
| 6 | cad | Calcium Deficient HA Discs | 17, 18, 19 | cad_main.png, cad_square.png, cad_wide.png |
| 7 | had | Dense HA Discs | 20, 21, 22 | had_main.png, had_square.png, had_wide.png |
| 8 | hadel | Enamel-like HA Discs | 23, 24, 25 | hadel_main.png, hadel_square.png, hadel_wide.png |
| 9 | atcp | Alpha-TCP | 26, 27, 28 | atcp_main.png, atcp_square.png, atcp_wide.png |
| 10 | ssbtcp | Beta-TCP (Solid-State) | 29, 30, 31 | ssbtcp_main.png, ssbtcp_square.png, ssbtcp_wide.png |
| 11 | swbtcp | Beta-TCP (Precipitated) | 32, 33, 34 | swbtcp_main.png, swbtcp_square.png, swbtcp_wide.png |
| 12 | utcp | TCP (Unsintered) | 35, 36, 37 | utcp_main.png, utcp_square.png, utcp_wide.png |
| 13 | ttcp | Tetracalcium Phosphate | 38, 39, 40 | ttcp_main.png, ttcp_square.png, ttcp_wide.png |
| 14 | s1bcp | BCP (Sintered) | 41, 42, 43 | s1bcp_main.png, s1bcp_square.png, s1bcp_wide.png |
| 15 | u1bcp | BCP (Unsintered) | 44, 45, 46 | u1bcp_main.png, u1bcp_square.png, u1bcp_wide.png |

---

## File Naming Convention

All images follow this naming pattern:
- **Main page:** `{product_id}_main.png`
- **Square photo:** `{product_id}_square.png`
- **Wide photo:** `{product_id}_wide.png`

Where `{product_id}` matches the ID in `data/products-index.json`.

---

## Quality Verification

- All 45 images extracted successfully
- All images are 1650x1275 pixels (150 DPI)
- Square and wide images include complete specification text at bottom
- Main images include full product introduction and description
- No cropping of specification text occurred

---

## Technical Details

**Extraction Method:** PyMuPDF (fitz)
**DPI:** 150 (zoom factor: 2.083)
**Color Space:** RGB
**Compression:** PNG (lossless)

**Script Location:** C:\Users\Juyong\Inbiomat\extract_product_images.py

---

## Next Steps

The images are ready for website integration. The user will handle:
- Updating JSON files with new image references
- Web component updates
- Deployment

---

## Files Generated

1. **45 product images** (mcd_main.png through u1bcp_wide.png)
2. **extraction_summary.json** - JSON summary of extraction
3. **EXTRACTION_REPORT.md** - This report

---

**Status:** COMPLETE ✓
All 45 product images successfully extracted with specification text included.
