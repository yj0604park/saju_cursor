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

## 배포

- 백엔드: Render.com
- 프론트엔드: Netlify.com 