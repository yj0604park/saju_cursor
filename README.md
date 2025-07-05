# 사주 프로그램 - FastAPI + Vue

사주를 봐주는 웹 애플리케이션입니다.

## 프로젝트 구조

```
saju_cursor/
├── backend/          # FastAPI 백엔드
│   ├── main.py
│   ├── requirements.txt
│   └── app/
├── frontend/         # Vue 프론트엔드
│   ├── package.json
│   ├── src/
│   └── public/
└── README.md
```

## 개발 환경 설정

### 백엔드 (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 프론트엔드 (Vue)
```bash
cd frontend
npm install
npm run dev
```

**환경별 API URL 설정:**
- **개발 환경**: 자동으로 `http://localhost:8000` 사용
- **배포 환경**: 자동으로 `https://saju-backend-vu8s.onrender.com` 사용
- **커스텀 설정**: `frontend/src/config.js` 파일에서 수정 가능

## 배포

- 백엔드: Render.com
- 프론트엔드: Netlify.com 