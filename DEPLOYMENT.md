# 🚀 배포 가이드

## 1. 백엔드 배포 (Render.com)

### 1.1 Render 계정 생성
- https://render.com 에서 계정 생성
- GitHub 계정으로 로그인

### 1.2 새 Web Service 생성
1. Dashboard에서 "New +" 클릭
2. "Web Service" 선택
3. GitHub 저장소 연결

### 1.3 설정
- **Name**: `saju-backend` (원하는 이름)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Root Directory**: `backend`

### 1.4 환경 변수 설정
- `PORT`: Render가 자동으로 설정
- `OPENAI_API_KEY`: OpenAI API 키 (ChatGPT 기능 사용 시 필요)
  - https://platform.openai.com/api-keys 에서 API 키 생성
  - Render Dashboard → Environment → Add Environment Variable

### 1.5 배포
- "Create Web Service" 클릭
- 배포 완료 후 URL 복사 (예: `https://saju-backend.onrender.com`)

---

## 2. 프론트엔드 배포 (Netlify.com)

### 2.1 API URL 업데이트
`frontend/src/App.vue` 파일에서:
```javascript
// 개발 환경
apiUrl: 'http://localhost:8000'

// 배포 환경 (Render URL로 변경)
apiUrl: 'https://saju-backend.onrender.com'
```

### 2.2 Netlify 계정 생성
- https://netlify.com 에서 계정 생성
- GitHub 계정으로 로그인

### 2.3 새 사이트 생성
1. "New site from Git" 클릭
2. GitHub 저장소 선택
3. 설정:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`

### 2.4 배포
- "Deploy site" 클릭
- 배포 완료 후 URL 복사 (예: `https://saju-frontend.netlify.app`)

---

## 3. CORS 설정 업데이트

백엔드가 배포된 후, `backend/main.py`에서 CORS 설정을 업데이트:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # 개발 환경
        "https://saju-frontend.netlify.app",  # 배포된 프론트엔드 URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 4. 도메인 연결 (선택사항)

### 4.1 커스텀 도메인 구입
- GoDaddy, Namecheap 등에서 도메인 구입

### 4.2 Netlify에 도메인 연결
1. Site settings → Domain management
2. "Add custom domain" 클릭
3. 도메인 입력 및 DNS 설정

---

## 5. 문제 해결

### 5.1 백엔드 배포 실패
- `requirements.txt` 파일이 `backend/` 폴더에 있는지 확인
- Build Command가 올바른지 확인

### 5.2 프론트엔드에서 API 호출 실패
- CORS 설정 확인
- API URL이 올바른지 확인
- 브라우저 개발자 도구에서 네트워크 탭 확인

### 5.3 환경 변수 문제
- Render에서 환경 변수가 올바르게 설정되었는지 확인
- `$PORT` 변수가 자동으로 설정되는지 확인

---

## 6. 무료 플랜 제한사항

### Render (백엔드)
- 월 750시간 무료
- 15분 동안 요청이 없으면 슬립 모드
- 첫 요청 시 30초 정도 로딩 시간

### Netlify (프론트엔드)
- 월 100GB 대역폭
- 무제한 사이트
- 커스텀 도메인 지원

---

## 7. 모니터링

### 7.1 로그 확인
- Render: Dashboard → Web Service → Logs
- Netlify: Site → Functions → Logs

### 7.2 성능 모니터링
- Render: Metrics 탭에서 CPU, 메모리 사용량 확인
- Netlify: Analytics 탭에서 방문자 통계 확인 