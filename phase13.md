프로젝트 경로: C:\Users\Juyong\Inbiomat
PDF 원본: C:\Users\Juyong\Inbiomat\VIEW-Rev00-EXTERNAL-Specs-Tradeshow-Interactive-COMPRESSED.pdf
이 PDF에서 제품 이미지를 재추출하고, 웹사이트에 적용해줘.
PDF 구조 설명
각 제품은 PDF에서 2~3페이지로 구성되어 있음:

1페이지: 제품 메인 소개 페이지 (전체 레이아웃 이미지)
2페이지: 정사각형에 가까운 제품 사진 + 하단에 수치/스펙 텍스트
3페이지: 좌우로 넓은(가로형) 제품 사진 + 하단에 수치/스펙 텍스트

이미지 재추출 요구사항

각 제품마다 3종류 이미지를 추출할 것:

{product_id}_main.png: 1페이지의 메인 이미지 (기존처럼)
{product_id}_square.png: 2페이지의 정사각형 이미지 — 하단 수치 텍스트를 포함해서 잘라야 함 (텍스트 잘라내지 말 것)
{product_id}_wide.png: 3페이지의 가로형 이미지 — 하단 수치 텍스트를 포함해서 잘라야 함 (텍스트 잘라내지 말 것)


기존 prototype/product_images/와 prototype/images/products/의 이미지를 새로 추출한 이미지로 교체

웹사이트 적용 요구사항

제품 리스트 페이지 (products.html, products.js):

제품 카드 썸네일에 {product_id}_square.png (2페이지 정사각형 이미지) 사용
제품 카드의 이미지 프레임을 정사각형에 가까운 비율로 수정 (현재 가로로 넓은 비율임)
CSS에서 .product-card-image 스타일 수정 필요


제품 상세 페이지 (product-detail.html, product-detail.js):

3개 이미지 모두 표시: main, square, wide
이미지 갤러리 또는 슬라이드 형태로 3장 모두 볼 수 있게 구성
각 이미지 하단의 수치 텍스트가 보여야 하므로 이미지 자체에 포함되어 있는 텍스트를 자르지 않은 상태로 표시


데이터 파일 업데이트:

prototype/data/products-index.json과 각 제품별 JSON 파일에서 이미지 경로를 새 파일명 체계로 업데이트
image 필드를 images 객체로 변경:



json     "images": {
       "main": "{product_id}_main.png",
       "square": "{product_id}_square.png",
       "wide": "{product_id}_wide.png"
     }

참고: 기존 추출된 이미지는 extracted_images/ 폴더와 product_images/ 폴더에 있음. extracted_images/image_metadata.json에 페이지별 이미지 매핑 정보가 있으니 참고해서 어떤 페이지가 어떤 제품인지 파악할 것.

수정 완료 후:
powershellgit add .
git commit -m "Re-extract product images with spec text, update thumbnails and detail page"
git push