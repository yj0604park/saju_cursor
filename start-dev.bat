@echo off
echo 🚀 사주 프로그램 개발 서버 시작...

echo.
echo 📦 백엔드 서버 시작 중...
cd backend
start "FastAPI Backend" cmd /k "pip install -r requirements.txt && uvicorn main:app --reload --port 8000"

echo.
echo ⏳ 3초 후 프론트엔드 서버를 시작합니다...
timeout /t 3 /nobreak > nul

echo.
echo 🎨 프론트엔드 서버 시작 중...
cd ../frontend
start "Vue Frontend" cmd /k "npm install && npm run dev"

echo.
echo ✅ 개발 서버가 시작되었습니다!
echo 🌐 백엔드: http://localhost:8000
echo 🎨 프론트엔드: http://localhost:3000
echo.
echo 💡 브라우저에서 http://localhost:3000 을 열어보세요!
pause 