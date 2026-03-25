#!/bin/bash
# 지출증빙생성기 HTML 변경 감지 → NAS + Vercel 자동 동기화
SRC="/Users/chrictvictory/코딩/Antigravity/영수증 증빙/지출증빙생성기_8.html"
DST1="/Users/chrictvictory/코딩/Antigravity/영수증 증빙/docker_deploy/index.html"
DST2="/Volumes/미디어/00_앱개발/영수증증빙/docker_deploy/index.html"
VERCEL_DIR="/Users/chrictvictory/코딩/Antigravity/영수증 증빙/vercel_deploy"

echo "🔄 자동 동기화 시작: 파일 변경 감시 중..."
echo "   소스: $SRC"
echo "   대상: NAS + Vercel"

fswatch -o "$SRC" | while read -r; do
  sleep 1
  cp "$SRC" "$DST1"
  cp "$SRC" "$DST2" 2>/dev/null
  cp "$SRC" "$VERCEL_DIR/index.html"
  echo "$(date '+%H:%M:%S') ✅ NAS 동기화 완료"
  cd "$VERCEL_DIR" && /opt/homebrew/bin/vercel --yes --prod > /dev/null 2>&1 &
  echo "$(date '+%H:%M:%S') 🚀 Vercel 배포 시작"
done
