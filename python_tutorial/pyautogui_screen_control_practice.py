import pyautogui as pag

# 참고 사이트 : https://codetorial.net/pyautogui/screenshot.html

# screenshot 기본
im1 = pag.screenshot()
im2 = pag.screenshot('test.png')
# region x,y,a,b 인 경우, x,y를 기준으로 a,b 만큼 떨어진만큼 스크린샷
im3 = pag.screenshot('test1.png', region=(0,0,300,300))

# 참고 사이트 : https://pyautogui.readthedocs.io/en/latest/screenshot.html

# 사진 위치 찾기
five = pag.locateOnScreen('five.png', grayscale=True, confidence=0.9)
print(five)