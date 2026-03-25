FROM python:3.9-slim

# 작업 위치 지정
WORKDIR /app

# 현재 폴더 안의 Python 서버 스크립트와 프론트엔드 HTML 뷰를 복사
COPY server.py /app/server.py

# 통신을 위한 포트 열기 (파이썬 서버 기본 포트 8000)
EXPOSE 8000

# 컨테이너가 켜질 때 실행될 명령어
CMD ["python", "server.py"]
