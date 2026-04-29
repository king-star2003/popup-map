from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import uvicorn  # 이 줄을 맨 위에 추가하세요!
from fastapi.responses import FileResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def serve_html():
    return FileResponse("index.html")

popup_db = [
    {"name": "메타몽 놀이터 팝업", "lat": 37.5445, "lng": 127.0560, "start_date": "2026-04-20", "end_date": "2026-05-05", "address": "성수동 연무장길 15", "description": "포켓몬 테마의 귀여운 체험존", "image_url": "https://picsum.photos/400?random=1"},
    {"name": "블랙핑크 'DEADLINE' 팝업", "lat": 37.5455, "lng": 127.0575, "start_date": "2026-04-20", "end_date": "2026-05-10", "address": "성수동 무신사 테라스", "description": "한정판 MD와 미공개 영상 전시", "image_url": "https://picsum.photos/400?random=2"},
    {"name": "나이키 X 스킴스 콜라보", "lat": 37.5430, "lng": 127.0545, "start_date": "2026-04-25", "end_date": "2026-05-15", "address": "성수 연무장길 32", "description": "혁신적인 피트니스웨어 팝업", "image_url": "https://picsum.photos/400?random=3"},
    {"name": "헬로키티 50주년 기념", "lat": 37.5125, "lng": 127.1025, "start_date": "2026-04-01", "end_date": "2026-05-03", "address": "잠실 롯데월드몰 1F", "description": "전 세계가 사랑하는 키티의 연대기", "image_url": "https://picsum.photos/400?random=4"},
    {"name": "오늘의집 힐링 하우스", "lat": 37.5815, "lng": 126.9850, "start_date": "2026-04-25", "end_date": "2026-05-10", "address": "북촌 한옥마을 카페", "description": "공간이 주는 휴식의 가치 전시", "image_url": "https://picsum.photos/400?random=5"},
    {"name": "바세린 X OIOI 칵테일 바", "lat": 37.5460, "lng": 127.0600, "start_date": "2026-04-15", "end_date": "2026-05-08", "address": "성수동 포탈", "description": "컬러 립밤과 무알콜 칵테일의 만남", "image_url": "https://picsum.photos/400?random=6"},
    {"name": "화이트 타이거 굿즈샵", "lat": 37.5565, "lng": 126.9235, "start_date": "2026-04-20", "end_date": "2026-05-14", "address": "홍대 AK플라자 2F", "description": "인기 캐릭터 단독 굿즈 판매", "image_url": "https://picsum.photos/400?random=7"},
    {"name": "온고 플래그십 팝업", "lat": 37.5420, "lng": 127.0555, "start_date": "2026-04-25", "end_date": "2026-05-20", "address": "성수동 1가 12-5", "description": "전통 매듭 모티브의 현대적 재해석", "image_url": "https://picsum.photos/400?random=8"},
    {"name": "버터베어 베이커리", "lat": 37.5215, "lng": 127.0230, "start_date": "2026-04-20", "end_date": "2026-05-15", "address": "가로수길 메인스트릿", "description": "인스타 감성의 귀여운 곰돌이 빵집", "image_url": "https://picsum.photos/400?random=9"}

]

@app.get("/api/popups")
def get_active_popups(target_date: date):
    active_popups = [
        popup for popup in popup_db
        if popup["start_date"] <= str(target_date) <= popup["end_date"]
    ]
    return {"data": active_popups}

# --- 파일 맨 아래에 이 두 줄을 반드시 추가하세요 ---
if __name__ == "__main__":
    uvicorn.run("map:app", host="127.0.0.1", port=8000, reload=True)