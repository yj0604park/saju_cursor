from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json

app = FastAPI(title="사주 API", version="1.0.0")

# CORS 설정 (프론트엔드에서 API 호출 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # 개발 환경
        "https://saju-frontend.netlify.app",  # 배포된 프론트엔드 (예시)
        "https://sajuyou.netlify.app",  # 가능한 Netlify URL
        "*",  # 임시로 모든 도메인 허용
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 데이터 모델
class SajuRequest(BaseModel):
    birth_year: int
    birth_month: int
    birth_day: int
    birth_hour: int
    birth_minute: int
    gender: str


class SajuResponse(BaseModel):
    message: str
    data: dict


@app.get("/")
async def root():
    return {"message": "사주 API 서버가 실행 중입니다!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/api/saju", response_model=SajuResponse)
async def calculate_saju(request: SajuRequest):
    """
    사주 계산 API
    """
    try:
        # 간단한 사주 계산 로직 (예시)
        birth_date = (
            f"{request.birth_year}-{request.birth_month:02d}-{request.birth_day:02d}"
        )
        birth_time = f"{request.birth_hour:02d}:{request.birth_minute:02d}"

        # 여기에 실제 사주 계산 로직이 들어갈 예정
        saju_result = {
            "birth_info": {
                "date": birth_date,
                "time": birth_time,
                "gender": request.gender,
            },
            "saju": {
                "year_pillar": "갑자",
                "month_pillar": "을축",
                "day_pillar": "병인",
                "hour_pillar": "정묘",
            },
            "elements": {"wood": 2, "fire": 1, "earth": 1, "metal": 0, "water": 0},
            "fortune": "오행이 균형잡혀 있어 안정적인 운세입니다.",
        }

        return SajuResponse(message="사주 계산이 완료되었습니다.", data=saju_result)

    except Exception as e:
        return SajuResponse(
            message=f"사주 계산 중 오류가 발생했습니다: {str(e)}", data={}
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
