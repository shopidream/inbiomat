# 네이버 검색로봇 접근 불가 문제 해결 가이드

## 문제 증상
```
네이버 검색로봇이 웹페이지에 접근할 수 없습니다.
```

## 주요 원인 및 해결 방법

### ⚠️ 1. 웹사이트가 온라인 상태가 아님 (가장 가능성 높음)

#### 확인 방법:
1. 웹 브라우저에서 `http://www.inbiomat.co.kr` 접속 시도
2. 명령 프롬프트에서 다음 명령어 실행:
```bash
curl -I http://www.inbiomat.co.kr
```
또는
```bash
ping www.inbiomat.co.kr
```

#### 예상 결과:
- ❌ **접속 불가**: "사이트에 연결할 수 없음" → 웹 서버 미실행 또는 도메인 미설정
- ✅ **접속 가능**: HTTP 200 응답 → 다른 원인 확인 필요

#### 해결 방법:
**A. 웹 호스팅 서비스 이용 시:**
- FTP/SFTP로 `prototype` 폴더 내의 모든 파일을 웹 서버 루트에 업로드
- 파일 위치:
  - `/index.html`
  - `/products.html`
  - `/product-detail.html`
  - `/quote.html`
  - `/robots.txt` ⭐ (루트에 위치 필수)
  - `/sitemap.xml` ⭐ (루트에 위치 필수)
  - `/css/`, `/js/`, `/assets/`, `/data/`, `/product_images/` 폴더

**B. 자체 서버 운영 시:**
- 웹 서버(Apache, Nginx 등) 실행 확인
- 방화벽 포트 80(HTTP), 443(HTTPS) 오픈
- 도메인 DNS A 레코드가 서버 IP를 올바르게 가리키는지 확인

---

### 2. robots.txt 접근 불가

#### 확인 방법:
브라우저에서 직접 접속:
```
http://www.inbiomat.co.kr/robots.txt
```

#### 예상 결과:
- ❌ **404 Not Found**: robots.txt 파일이 루트에 없음
- ✅ **200 OK**: 파일 내용이 보임

#### 해결 방법:
- **robots.txt 파일을 반드시 웹사이트 루트 디렉토리에 배치**
- 잘못된 위치: `/prototype/robots.txt`
- 올바른 위치: `/robots.txt` (웹 서버 루트)

---

### 3. 네이버 검색로봇 User-Agent 차단

#### 확인 방법:
웹 서버 설정 파일 확인 (Apache `.htaccess` 또는 Nginx config)

#### 차단 예시 (잘못된 설정):
```apache
# Apache .htaccess - 잘못된 예시
RewriteCond %{HTTP_USER_AGENT} Yeti [NC]
RewriteRule .* - [F,L]
```

```nginx
# Nginx - 잘못된 예시
if ($http_user_agent ~* (Yeti)) {
    return 403;
}
```

#### 해결 방법:
네이버 검색로봇(Yeti) User-Agent를 허용하도록 설정 변경:

**Apache (.htaccess):**
```apache
# 네이버 검색로봇 허용
<IfModule mod_rewrite.c>
    RewriteEngine On
    # Yeti 차단 규칙이 있다면 제거
</IfModule>
```

**Nginx:**
```nginx
# Yeti 차단 규칙 제거 또는 주석 처리
# if ($http_user_agent ~* (Yeti)) {
#     return 403;
# }
```

---

### 4. 방화벽/보안 프로그램 차단

#### 네이버 검색로봇 IP 대역:
네이버 검색로봇은 다양한 IP에서 접근합니다.
- IP 확인 방법: 역 DNS 조회 시 `*.naver.com` 도메인

#### 해결 방법:
**방화벽 화이트리스트 추가:**
- Cloudflare, AWS WAF, 기타 방화벽 사용 시
- 네이버 검색로봇 IP 범위 허용 설정
- User-Agent "Yeti" 허용

**서버 방화벽 (Linux iptables):**
```bash
# 네이버 검색로봇 IP 대역 허용 (예시)
# 실제 IP 대역은 네이버 웹마스터 도구 참조
```

---

### 5. 웹 서버 응답 속도 느림 (10초 이상)

#### 확인 방법:
```bash
curl -w "@curl-format.txt" -o /dev/null -s http://www.inbiomat.co.kr
```

**curl-format.txt 내용:**
```
time_total: %{time_total}s
```

#### 해결 방법:
- 서버 리소스 확인 (CPU, 메모리)
- 데이터베이스 쿼리 최적화
- CDN 사용 고려
- 이미지/스크립트 최적화 (이미 적용됨)

---

### 6. HTTPS vs HTTP 문제

#### 확인 사항:
- robots.txt와 sitemap.xml의 URL 프로토콜 일치
- 현재 설정: `http://www.inbiomat.co.kr`
- HTTPS 사용 시: URL을 `https://`로 변경 필요

#### 해결 방법:
**HTTPS 사용 시 파일 수정:**

**robots.txt:**
```
Sitemap: https://www.inbiomat.co.kr/sitemap.xml
```

**sitemap.xml:**
```xml
<loc>https://www.inbiomat.co.kr/index.html</loc>
```

**모든 HTML 파일의 canonical 태그:**
```html
<link rel="canonical" href="https://www.inbiomat.co.kr/index.html">
```

---

## 단계별 해결 프로세스

### Step 1: 웹사이트 접속 확인
```bash
# Windows CMD
curl http://www.inbiomat.co.kr
# 또는
ping www.inbiomat.co.kr
```

결과:
- ❌ 접속 불가 → **웹 서버 배포 및 도메인 설정 확인**
- ✅ 접속 가능 → Step 2로

### Step 2: robots.txt 확인
```
http://www.inbiomat.co.kr/robots.txt
```

결과:
- ❌ 404 에러 → **robots.txt 파일을 루트에 업로드**
- ✅ 파일 보임 → Step 3으로

### Step 3: sitemap.xml 확인
```
http://www.inbiomat.co.kr/sitemap.xml
```

결과:
- ❌ 404 에러 → **sitemap.xml 파일을 루트에 업로드**
- ✅ 파일 보임 → Step 4로

### Step 4: 네이버 웹마스터 도구에서 수집 요청
1. [네이버 서치어드바이저](https://searchadvisor.naver.com) 접속
2. **요청 > robots.txt > 수집 요청**
3. **요청 > 사이트맵 제출 > URL 입력**

### Step 5: 수집 현황 모니터링
- 24-48시간 후 **통계 > 수집 현황** 확인
- 오류 발생 시 상세 메시지 확인

---

## 체크리스트

### ✅ 배포 전 확인사항
- [ ] 웹 호스팅 서비스 계약 완료
- [ ] 도메인 DNS 설정 완료 (A 레코드)
- [ ] 웹 서버 실행 중
- [ ] FTP/SFTP 접속 가능

### ✅ 파일 배치 확인
- [ ] `/robots.txt` (루트)
- [ ] `/sitemap.xml` (루트)
- [ ] `/index.html` (루트)
- [ ] `/products.html` (루트)
- [ ] `/product-detail.html` (루트)
- [ ] `/quote.html` (루트)
- [ ] `/css/` 폴더
- [ ] `/js/` 폴더
- [ ] `/assets/` 폴더
- [ ] `/data/` 폴더
- [ ] `/product_images/` 폴더

### ✅ 네이버 웹마스터 도구 설정
- [x] 사이트 소유 확인 (HTML 메타 태그)
- [ ] robots.txt 수집 요청
- [ ] sitemap.xml 제출
- [ ] 수집 현황 모니터링

### ✅ 서버 설정 확인
- [ ] 방화벽 포트 80, 443 오픈
- [ ] User-Agent "Yeti" 차단 없음
- [ ] 웹 서버 응답 속도 10초 이내
- [ ] robots.txt, sitemap.xml HTTP 200 응답

---

## 네이버 검색로봇 User-Agent 정보

### Yeti (검색 수집 로봇)
```
Mozilla/5.0 (compatible; Yeti/1.1; +https://naver.me/spd)
```
또는
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Yeti/1.1; +https://naver.me/spd) Chrome/W.X.Y.Z Safari/537.36
```

### 테스트 방법
웹 서버 로그에서 Yeti User-Agent 접근 기록 확인:
```bash
# Apache access.log
tail -f /var/log/apache2/access.log | grep Yeti

# Nginx access.log
tail -f /var/log/nginx/access.log | grep Yeti
```

---

## 추가 도움말

### 웹 호스팅 서비스 추천
- **Cafe24**: 국내 대표 호스팅, 네이버 검색 최적화 지원
- **가비아**: 도메인 + 호스팅 통합 관리
- **AWS/Azure**: 클라우드 서버 (고급 사용자)

### 도메인 DNS 설정 (예시)
```
타입: A
호스트: www
값: [웹 서버 IP 주소]
TTL: 3600
```

### 문의
- 네이버 서치어드바이저 고객센터
- 웹 호스팅 업체 기술 지원

---

**작성일**: 2026-02-14
