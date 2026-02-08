프로젝트 경로: C:\Users\Juyong\Inbiomat
목표: prototype 폴더를 유일한 웹사이트 소스로 통합하고, 데이터 이중화 문제를 완전히 제거한다.
현재 문제:

Inbiomat/data/(루트)와 Inbiomat/prototype/data/에 같은 JSON 파일이 따로 존재
Inbiomat/product_images/와 Inbiomat/prototype/product_images/에 같은 이미지가 따로 존재
수정할 때 한쪽만 업데이트되어 Cloudflare 배포 시 이미지/데이터가 안 보이는 문제 반복 발생
Cloudflare는 wrangler.jsonc의 assets.directory: "./prototype"에 따라 prototype 폴더만 배포함

작업 순서:
1단계: 루트 데이터를 prototype으로 동기화

루트 data/products-index.json이 최신이면 prototype/data/products-index.json에 덮어쓰기
루트 data/categories.json → prototype/data/categories.json에 덮어쓰기
루트 data/products/*.json → prototype/data/products/에 덮어쓰기
루트 product_images/pages/*.png → prototype/product_images/pages/에 덮어쓰기
동기화 후 prototype/data/products-index.json에 "pages" 필드가 정상적으로 있는지 확인

2단계: prototype 내 불필요한 이미지 정리

prototype/product_images/ 안에 pages 폴더 외의 옛날 크롭 이미지(*_1.png, *_2.png, *_main.png, *_square.png, *_wide.png 등)가 있으면 삭제
prototype/images/products/ 폴더가 있으면 삭제
prototype/product_images/pages/page_02.png ~ page_46.png만 남기기

3단계: JS/HTML 경로 전체 검증

prototype/ 안의 모든 HTML, JS, CSS 파일에서 ../data/, ../product_images/ 등 prototype 바깥을 참조하는 경로가 없는지 확인
모든 경로는 ./data/, ./product_images/ (prototype 내부 상대경로)여야 함
특히 prototype/js/products.js, prototype/js/product-detail.js, prototype/index.html의 fetch 경로와 img src 경로 확인
JSON에서 이미지를 참조하는 필드(pages.main, pages.detail1, pages.detail2)의 값이 실제 prototype/product_images/pages/에 존재하는 파일명과 일치하는지 확인

4단계: 루트 원본 폴더 정리

루트의 data/ 폴더 삭제 (prototype/data/가 유일한 소스)
루트의 product_images/ 폴더 삭제 (prototype/product_images/가 유일한 소스)
루트의 extracted_images/ 폴더 삭제 (더 이상 사용 안 함)
루트의 prototype/images/ 폴더가 있으면 삭제
루트의 이미지 추출 관련 Python 스크립트들(extract_product_images.py, extract_images_with_text.py, cleanup_product_images.py, update_product_images.py, verify_extraction.py, copy_to_prototype.py) 삭제
루트의 pdf_content.json, image_mapping.csv, image_mapping.json, EXTRACTION_SUMMARY.txt 등 추출 관련 파일 삭제
phase*.md, product-analysis.md, PHASE2-*.md 등 작업 기록 파일은 유지해도 무방 (선택사항)

5단계: 최종 구조 확인
정리 후 구조가 이렇게 되어야 함:
Inbiomat/
├── prototype/              ← Cloudflare 배포 대상 (유일한 웹사이트 소스)
│   ├── index.html
│   ├── products.html
│   ├── product-detail.html
│   ├── quote.html
│   ├── assets/
│   ├── css/style.css
│   ├── js/
│   │   ├── i18n.js
│   │   ├── products.js
│   │   ├── product-detail.js
│   │   └── quote.js
│   ├── lang/
│   │   ├── en.json
│   │   └── ko.json
│   ├── data/
│   │   ├── products-index.json
│   │   ├── categories.json
│   │   └── products/*.json
│   └── product_images/
│       └── pages/
│           ├── page_02.png ~ page_46.png
├── wrangler.jsonc
├── VIEW-Rev00-EXTERNAL-Specs-Tradeshow-Interactive-COMPRESSED.pdf
└── (작업 기록 md 파일들)
6단계: 배포 테스트

wrangler.jsonc의 assets.directory가 "./prototype" 또는 "prototype"인지 확인
로컬에서 브라우저로 prototype/index.html 열어서 이미지가 보이는지 확인
prototype/products.html 열어서 제품 카드에 이미지가 보이는지 확인

중요 원칙: 앞으로 이 프로젝트에서 데이터나 이미지를 수정할 때는 반드시 prototype/ 안의 파일만 수정할 것. 루트에 별도 data나 product_images 폴더를 만들지 말 것.
수정 완료 후:
powershellgit add .
git commit -m "Consolidate all data and images into prototype folder, remove duplicates"
git push