from urllib import request
import time
import io
import PIL.Image

url = "https://cdn.fastpick.co.kr/fastpick/2021/03/image_2322861011616642090118.png"

# time check
start = time.time()

# request.urlopen()
res = request.urlopen(url).read()

# 이미지 다운로드 시간 체크
print(time.time() - start)


# Image open
img = PIL.Image.open(io.BytesIO(res))