from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
from saju_ai import saju_ai

# slowapi import
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI(title="사주 API", version="1.0.0")

# slowapi 초기화 (인코딩 문제 해결)
limiter = Limiter(key_func=get_remote_address, default_limits=["200/day", "50/hour"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
@limiter.limit("5/minute")  # 1분에 5회 제한
async def calculate_saju(request: Request, request_body: SajuRequest):
    """
    사주 계산 API
    """
    try:
        # 간단한 사주 계산 로직 (예시)
        birth_date = f"{request_body.birth_year}-{request_body.birth_month:02d}-{request_body.birth_day:02d}"
        birth_time = f"{request_body.birth_hour:02d}:{request_body.birth_minute:02d}"

        saju_result = {
            "birth_info": {
                "date": birth_date,
                "time": birth_time,
                "gender": request_body.gender,
            },
            "saju": {
                "year_pillar": "갑자",
                "month_pillar": "을축",
                "day_pillar": "병인",
                "hour_pillar": "정묘",
            },
            "elements": {"wood": 2, "fire": 1, "earth": 1, "metal": 0, "water": 0},
        }

        # ChatGPT를 사용한 다양한 해석 생성
        try:
            # 기본 운세 요약
            fortune_summary = saju_ai.generate_fortune_summary(saju_result)
            saju_result["fortune"] = fortune_summary

            # 올해의 금전운
            money_fortune = saju_ai.generate_money_fortune(saju_result)
            saju_result["money_fortune"] = money_fortune

            # 올해의 애정운
            love_fortune = saju_ai.generate_love_fortune(saju_result)
            saju_result["love_fortune"] = love_fortune

            # 상세 AI 해석
            ai_interpretation = saju_ai.generate_saju_interpretation(saju_result)
            saju_result["ai_interpretation"] = ai_interpretation

        except Exception as e:
            print(f"AI 해석 오류: {e}")
            # 오류 시 기본값 설정
            saju_result["fortune"] = "오행이 균형잡혀 있어 안정적인 운세입니다."
            saju_result["money_fortune"] = (
                "올해는 안정적인 재정 관리가 중요한 한 해가 될 것입니다."
            )
            saju_result["love_fortune"] = (
                "올해는 진정한 사랑을 찾는 중요한 한 해가 될 것입니다."
            )
            saju_result["ai_interpretation"] = (
                "AI 해석을 불러오는 중 오류가 발생했습니다."
            )

        return SajuResponse(message="사주 계산이 완료되었습니다.", data=saju_result)

    except Exception as e:
        return SajuResponse(
            message=f"사주 계산 중 오류가 발생했습니다: {str(e)}", data={}
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
