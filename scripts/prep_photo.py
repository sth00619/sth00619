"""
source-photo.jpg 를 읽어서
1. 배경 제거 (rembg)
2. 로컬 대비 향상 (CLAHE)
3. 흰 배경 합성
결과: assets/source-prepped.png
"""
from pathlib import Path
import numpy as np
import cv2
from rembg import remove
from PIL import Image
import io

ROOT       = Path(__file__).resolve().parent.parent
INPUT_PATH = ROOT / "assets" / "source-photo.jpg"
OUT_PATH   = ROOT / "assets" / "source-prepped.png"


def main():
    print("1. 이미지 읽는 중...")
    img_bytes = INPUT_PATH.read_bytes()

    print("2. 배경 제거 중... (첫 실행 시 모델 다운로드로 1~2분 걸릴 수 있음)")
    removed = remove(img_bytes)   # RGBA PNG bytes 반환

    print("3. 대비 향상 중...")
    pil_img = Image.open(io.BytesIO(removed)).convert("RGBA")

    # 흰 배경 합성
    bg = Image.new("RGBA", pil_img.size, (255, 255, 255, 255))
    bg.paste(pil_img, mask=pil_img.split()[3])
    gray_pil = bg.convert("L")

    # CLAHE 적용 (OpenCV)
    gray_np = np.array(gray_pil)
    clahe   = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray_np)

    result = Image.fromarray(enhanced).convert("RGB")
    result.save(OUT_PATH)
    print(f"저장 완료: {OUT_PATH}")


if __name__ == "__main__":
    main()