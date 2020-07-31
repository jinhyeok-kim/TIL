import pyautogui as pag

# 참고 사이트 : https://blankspace-dev.tistory.com/416

# 현재 사용하고 있는 모니터의 사이즈 반환
w, h = pag.size()
print('{0}, {1}'.format(w, h))

# 현재 마우스의 위치 반환
x, y = pag.position()
print('{0}, {1}'.format(x, y))

# x, y 좌표로 마우스 움직이기
pag.moveTo(50, 50)
pag.moveTo(100, 1000, 1) # x, y 좌표로 z초 동안