목표: 랜딩페이지(prototype/index.html) 상단에 응용 분야 이미지 슬라이드쇼를 추가한다.
이미지 파일:

prototype/assets/applications/bone-graft.jpg
prototype/assets/applications/dental-implant.jpg
prototype/assets/applications/3d-scaffold.jpg

슬라이드쇼 요구사항:

위치: 헤더(header) 바로 아래, 기존 콘텐츠 위에 배치 (히어로 섹션 역할)
자동 전환: 5초 간격으로 자동 슬라이드 전환, 무한 루프
수동 전환: 좌우 화살표 버튼으로 이전/다음 이동 가능
인디케이터: 하단에 현재 슬라이드 위치를 나타내는 점(dot) 표시, 클릭으로 해당 슬라이드 이동
전환 효과: fade 또는 slide 애니메이션 (부드럽게)
반응형: 모바일에서도 전체 너비로 표시, 높이는 뷰포트 대비 적절하게 (데스크톱: 60vh, 모바일: 40vh 정도)
이미지 표시: object-fit: cover;로 영역을 꽉 채우되 비율 유지
텍스트 오버레이: 각 슬라이드에 응용 분야 텍스트를 반투명 배경 위에 표시

슬라이드 1 (bone-graft.jpg): "Bone Graft Substitutes" / "골이식재"
슬라이드 2 (dental-implant.jpg): "Dental Implants" / "치과 임플란트"
슬라이드 3 (3d-scaffold.jpg): "3D Printed Scaffolds" / "3D 프린팅 스캐폴드"
텍스트는 현재 언어 설정(i18n)에 따라 영어/한국어 전환


외부 라이브러리 없이 순수 HTML/CSS/JS로 구현
이미지 경로: ./assets/applications/bone-graft.jpg 등 prototype 내부 상대경로 사용

CSS 추가 위치: prototype/css/style.css에 슬라이드쇼 관련 스타일 추가
JS: prototype/index.html 내 인라인 스크립트 또는 별도 prototype/js/slideshow.js 파일 생성
i18n 지원: prototype/lang/en.json과 prototype/lang/ko.json에 슬라이드 텍스트 추가
수정 완료 후:
powershellgit add .
git commit -m "Add application slideshow hero section to landing page"
git push