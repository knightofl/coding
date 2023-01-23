import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import  rc


# 설치된 폰트 출력
font_list = [font.name for font in fm.fontManager.ttflist]
print(font_list)

# 원하는 경로의 폰트 확인
#font_list = fm.findSystemFonts(fontpaths="/usr/share/fonts/", fontext='ttf')
#print(font_list)

# 나눔고딕으로 설정
plt.rcParams['font.family'] = 'NanumGothicCoding'


if __name__ == '__main__':
    plt.text(0.3, 0.3, '테스트', size=20)
    plt.show()

