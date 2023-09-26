import numpy as np
import matplotlib.pyplot as plt


fig, splts = plt.subplots(1,1)
splts.plot([1,2,3,4], [10,15,20,25], 'go--')
plt.show()


fig, splts = plt.subplots()
splts.plot(np.random.randn(50).cumsum(), color='blue', linestyle='', marker='o')
plt.show()


fig, splts = plt.subplots(1)
splts.plot(np.random.randn(50).cumsum(), drawstyle='steps-mid', color='red',
    linestyle='-', marker='None')


fig, splts = plt.subplots(2,1)
splts[0].plot(np.random.randn(1000).cumsum())
splts[1].plot(np.random.randn(1000).cumsum())
splts[1].set_xticks([0,100,200,300,400,500,600,700,800,900,1000])
plt.show()


fig, splts = plt.subplots(2,1)
splts[0].plot(np.random.randn(1000).cumsum())
splts[1].plot(np.random.randn(1000).cumsum())
splts[1].set_xticks([0,100,200,300,400,500,600,700,800,900,1000])
splts[1].set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5',
    'pt6', 'pt7', 'pt8', 'pt9', 'pt10'], rotation=30, fontsize='small')

splts[1].set_xlabel('points')
splts[0].set_title('matplot subject')
plt.show()


heights = [100, 120, 130, 140, 150, 160, 170, 180, 190]
footSize = [200, 205, 210, 220, 230, 250, 270, 280, 285]
fig, splts = plt.subplots()
splts.scatter(heights, footSize)
plt.xlabel('height (cm)')
plt.ylabel('foot size (mm)')
plt.show()


'''
color
복합문자열 : k, r, b, g, y...
명시적 표현 : black, red, blue, green, yellow...
cf) #rrggbb

linestyle : - (solid), -- (dashed), -. (dashdot), dotted, ' ' (none)
marker : . (dot), v (arrow), o (big dot)
drawstyle : 'default', 'steps', 'stesp-pre', 'steps-mid', 'steps-post'
'''
