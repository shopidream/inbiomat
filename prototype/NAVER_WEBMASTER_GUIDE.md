# 네이버 웹마스터 도구 설정 가이드

## 1. 네이버 서치어드바이저 등록

### 1.1 사이트 등록
1. [네이버 서치어드바이저](https://searchadvisor.naver.com) 접속
2. 네이버 계정으로 로그인
3. 상단 메뉴에서 **"웹마스터 도구"** 클릭
4. **"사이트 등록"** 버튼 클릭
5. 사이트 URL 입력: `https://www.inbiomat.co.kr`

### 1.2 사이트 소유 확인
✅ **이미 완료**: HTML 메타 태그 방식으로 인증 완료
- 인증 코드: `aefbeaffa8f2f1e2eadfdc54195ec23b0f59b2a0`
- 모든 HTML 페이지에 메타 태그 추가됨

## 2. robots.txt 제출

### 2.1 robots.txt 확인
- 파일 위치: `/prototype/robots.txt`
- 웹 URL: `https://www.inbiomat.co.kr/robots.txt`

### 2.2 제출 방법
1. 서치어드바이저 > **"요청"** > **"robots.txt"** 클릭
2. robots.txt 내용 확인
3. 수집 요청

### 2.3 robots.txt 내용
```
# 네이버 검색로봇 (Yeti) 허용
User-agent: Yeti
Allow: /

# 모든 검색로봇 허용
User-agent: *
Allow: /

# Sitemap 위치
Sitemap: http://www.inbiomat.co.kr/sitemap.xml
```

## 3. sitemap.xml 제출

### 3.1 Sitemap 확인
- 파일 위치: `/prototype/sitemap.xml`
- 웹 URL: `https://www.inbiomat.co.kr/sitemap.xml`

### 3.2 제출 방법
1. 서치어드바이저 > **"요청"** > **"사이트맵 제출"** 클릭
2. Sitemap URL 입력: `https://www.inbiomat.co.kr/sitemap.xml`
3. **"확인"** 버튼 클릭

### 3.3 포함된 페이지
- `index.html` (우선순위: 1.0)
- `products.html` (우선순위: 0.8)
- `product-detail.html` (우선순위: 0.8)
- `quote.html` (우선순위: 0.7)

## 4. 검색 최적화 확인

### 4.1 검색 노출 확인
서치어드바이저에서 다음 항목들을 확인:

1. **수집 현황**
   - 경로: 서치어드바이저 > "통계" > "수집 현황"
   - 확인 사항: 크롤링된 페이지 수, 오류 페이지

2. **검색 반영 현황**
   - 경로: 서치어드바이저 > "통계" > "검색 반영 현황"
   - 확인 사항: 색인된 페이지 수

3. **사이트 간단 체크**
   - 경로: 서치어드바이저 > "최적화" > "사이트 간단 체크"
   - 확인 사항: SEO 점수, 개선 사항

### 4.2 구조화된 데이터 확인
1. 서치어드바이저 > **"검증"** > **"구조화된 데이터"**
2. 페이지 URL 입력하여 JSON-LD 스키마 확인
3. 오류 없이 인식되는지 확인

### 4.3 모바일 친화성 확인
1. 서치어드바이저 > **"검증"** > **"모바일 친화성"**
2. 페이지별로 모바일 최적화 확인

## 5. 검색어 등록 및 관리

### 5.1 검색어 설정
서치어드바이저 > **"최적화"** > **"검색어 관리"**

권장 검색어:
- 칼슘포스페이트
- 바이오머티리얼
- 하이드록시아파타이트
- 의료용 바이오머티리얼
- calcium phosphate
- biomaterials
- hydroxyapatite
- TCP
- BCP

### 5.2 콘텐츠 최적화
- 각 페이지에 한글/영어 키워드 모두 포함
- meta keywords 태그에 주요 검색어 등록됨
- 구조화된 데이터(JSON-LD)로 검색 노출 개선

## 6. 성능 모니터링

### 6.1 주기적 확인 항목
- **주 1회**: 수집 현황, 검색 반영 현황
- **월 1회**: 사이트 간단 체크, 검색어 통계
- **필요시**: 수집 요청 (새 페이지 추가 시)

### 6.2 오류 대응
1. **수집 오류 발생 시**
   - 서치어드바이저 > "통계" > "수집 현황" > 오류 페이지 확인
   - robots.txt, sitemap.xml 재확인
   - 수집 재요청

2. **색인 누락 시**
   - 페이지 접근성 확인
   - meta robots 태그 확인 (noindex 설정 여부)
   - 수동 색인 요청

## 7. 적용된 SEO 최적화 목록

### 7.1 HTML 최적화
✅ 모든 페이지에 적용됨:
- `<meta name="robots" content="index, follow">`
- `<meta name="naver-site-verification">`
- `<meta name="keywords">` (한/영 키워드)
- `<link rel="canonical">` (표준 URL)
- `lang="ko"` 속성

### 7.2 구조화된 데이터 (JSON-LD)
✅ 페이지별 스키마 적용:
- **index.html**: Organization, WebSite, BreadcrumbList
- **products.html**: CollectionPage, ItemList, BreadcrumbList
- **product-detail.html**: Product, BreadcrumbList
- **quote.html**: ContactPage, BreadcrumbList

### 7.3 이미지 최적화
✅ 모든 이미지:
- alt 태그 추가
- loading="lazy" 적용 (첫 화면 제외)

### 7.4 성능 최적화
✅ 모든 페이지:
- JavaScript defer 로딩
- 리소스 힌트 (preconnect, dns-prefetch)

## 8. 다음 단계

### 8.1 추가 권장 사항
1. **Google Search Console 등록**
   - 구글 검색 노출을 위해 등록 권장
   - sitemap.xml, robots.txt 동일하게 사용 가능

2. **네이버 블로그/카페 활용**
   - 공식 블로그 개설하여 제품 정보 공유
   - 백링크 생성으로 검색 순위 개선

3. **정기적인 콘텐츠 업데이트**
   - 신제품 정보 추가
   - 기술 문서, 사용 사례 업데이트

4. **페이지 속도 개선**
   - 이미지 WebP 변환
   - CSS/JS 압축 (minify)
   - CDN 사용 고려

### 8.2 문의
- 네이버 서치어드바이저 헬프센터: https://searchadvisor.naver.com/guide
- 네이버 웹마스터 공식 블로그: https://blog.naver.com/naver_search

---

**작성일**: 2026-02-14
**최종 업데이트**: 2026-02-14
**담당자**: I&H Global
