import turtle as t
a = -580 #"x軸調位"
t.speed (10000000) #"速度"

t.penup () #"外圏"
t.goto ( 0 + a , -60) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.circle ( 110 ) #"半徑"
t.end_fill() #"結束填充"

t.penup () #"內圏"
t.goto ( 0 + a , -53) 
t.pendown ()
t.color ( 'white' ) #"法國國旗色"
t.begin_fill() #"開始填充"
t.circle ( 103 ) #"半徑"
t.end_fill() #"結束填充"

t.penup () #"三角形"
t.goto ( 80 + a , -40)
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.forward ( 180 )
t.penup ()
t.goto ( 80 + a , -40)
t.pendown ()
t.left ( 118 )
t.forward ( 85 )
t.right (161) #"轉右"
t.forward ( 3 ) #"前進"
for i in range (3): #"重複次數"
    t.left (4) #"轉左"
    t.forward ( 3 ) #"前進"
for i in range (6): 
    t.left (0.95)
    t.forward (2)
for i in range (13):
    t.left (0.5)
    t.forward (5)
for i in range (15):
    t.left (0.12)
    t.forward (5)
for i in range (15):
    t.left (0.69)
    t.forward (5)
t.end_fill() #"結束填充"

t.penup ()#" ☇“
t.goto ( 120 + a , 190) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.right (130.5)
t.forward (45)
t.left (3)
t.forward (45)
for i in range (8):
    t.left (3)
    t.forward (28)
t.left (5)
t.forward (4)
t.left (15)
t.forward (5)
t.left (11)
t.forward (7)
for i in range (6):
    t.left (16.95)
    t.forward (5)
for i in range (6):
    t.left (3)
    t.forward (7.6)

t.right (170)
t.forward (33)
for i in range (2):
    t.right (3)
    t.forward (2)
for i in range (10):
    t.right (3)
    t.forward (3)
t.forward ( 7 )
for i in range (10):
    t.right (5)
    t.forward (2)
for i in range (15):
    t.right (4)
    t.forward (2)
for i in range (4):
    t.right (5)
    t.forward (18)
for i in range (3):
    t.right (2.4)
    t.forward (23)
for i in range (3):
    t.right (3)
    t.forward (21)
for i in range (3):
    t.right (2.5)
    t.forward (21)
for i in range (3):
    t.right (1)
    t.forward (14)
t.goto ( 120 + a , 190)
t.end_fill() #"結束填充"

t.penup () # 字母（B）
t.goto ( 230 + a , 3 ) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.right (38)
t.forward (150)
for i in range (19):
    t.left (3)
    t.forward (1.5)
t.forward (37)
for i in range (20):
    t.left (4)
    t.forward (1)
t.right ( 110 )
for i in range (12):
    t.forward (3)
    t.left (3)
t.forward (33.5) 
for i in range (23):
    t.left (5.01)
    t.forward (1.5)
t.left (2)
t.forward (150)
t.left (65)
t.forward (155) #"淺藍色"
t.end_fill() #"結束填充"
    
t.penup ()# 字母（B）
t.goto ( 320 + a , 30 ) 
t.pendown ()
t.color ( 'white' ) #"白色"
t.begin_fill() #"開始填充"
t.left ( 115 )
t.forward ( 23 )
for i in range (24):
    t.left (2.5)
    t.forward (0.5)
t.forward ( 10 )
for i in range (24):
    t.left (5)
    t.forward (0.5)
t.forward ( 23 )
t.left ( 65 )
t.forward (26)
t.end_fill() #"結束填充"

t.penup () # 字母（B）
t.goto ( 342 + a , 88 ) 
t.pendown ()
t.color ( 'white' ) #"白色"
t.begin_fill() #"開始填充"
t.left ( 115 )
t.forward ( 23 )
for i in range (24):
    t.left (2.5)
    t.forward (0.5)
t.forward ( 10 )
for i in range (24):
    t.left (5)
    t.forward (0.5)
t.forward ( 23 )
t.left ( 65 )
t.forward (26)
t.end_fill() #"結束填充"

t.penup () # 字母（O）
t.goto ( 445 + a , 3 ) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.left ( 115 )
t.forward ( 130 )

for i in range (12):
    t.left (5)
    t.forward (3)
t.forward ( 117 )
for i in range (15):
    t.left (8)
    t.forward (1.83)
t.forward ( 130 )
for i in range (12):
    t.left (5)
    t.forward (3)
t.forward ( 117 )
for i in range (15):
    t.left (8)
    t.forward (1.83)
t.end_fill() #"結束填充"

t.penup () # 字母（O）
t.goto ( 518 + a , 27 ) 
t.pendown ()
t.color ( 'white' ) #"白色"
t.begin_fill() #"開始填充"
t.forward ( 16 )

for i in range (11):
    t.left (5.6)
    t.forward (1)
t.forward ( 89 )
for i in range (12):
    t.left (9.9)
    t.forward (1)
t.forward ( 16 )
for i in range (11):
    t.left (5.6)
    t.forward (1)
t.forward ( 89 )
for i in range (12):
    t.left (9.9)
    t.forward (1)
t.end_fill() #"結束填充"

t.penup () # 字母（E）
t.goto ( 623 + a , 3 ) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.right ( 0.75 )
t.forward ( 139 )
t.left ( 65 )
t.forward ( 32 )
t.left ( 115 )
t.forward ( 67.5 )
t.right (  115 )
t.forward ( 32 )
t.right ( 65 )
t.forward ( 67.5 )
t.left ( 65 )
t.forward ( 32 )
t.left ( 115)
t.forward ( 67.5 )
t.right (  115 )
t.forward ( 32 )
t.right ( 65 )
t.forward ( 67.5 )
t.left ( 65 )
t.forward ( 32 )
t.left ( 115)
t.forward ( 136 )
t.left ( 62.5 )
t.forward ( 165 )
t.end_fill() #"結束填充"

t.penup () # 字母（i）
t.goto ( 780 + a , 3 ) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.left ( 117.5 )
t.forward ( 54 )
t.left ( 65 )
t.forward ( 160 )
t.left ( 115 )
t.forward ( 54 )
t.left ( 65 )
t.forward ( 160 )
t.end_fill() #"結束填充"

t.penup () # 字母（N）
t.goto ( 855 + a , 3 ) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.left ( 115 )
t.forward ( 42.9 )
t.left ( 65 )
t.forward ( 80 )
t.right ( 130)
t.forward ( 80 )
t.left ( 65 )
t.forward ( 48 )
t.left ( 65 )
t.forward ( 160 )
t.left ( 114.5 )
t.forward ( 42.9 )
t.left ( 65 )
t.forward ( 80 )
t.right ( 130 )
t.forward ( 80 )
t.left ( 65.5 )
t.forward ( 48 )
t.left ( 65 )
t.forward ( 160 )
t.end_fill() #"結束填充"

t.penup () # 字母（G）
t.goto ( 1070 + a , 3 ) 
t.pendown ()
t.color ( 'navy blue' ) #"淺藍色"
t.begin_fill() #"開始填充"
t.left ( 115 )
t.forward ( 110 )

for i in range ( 32 ):
    t.left ( 2 )
    t.forward ( 2 )
t.forward ( 6 )
t.right ( 65 )
t.forward ( 15 )
t.left ( 65 )
t.forward ( 25 )
t.left ( 116 )
t.forward ( 76 )
t.left ( 65 )
t.forward ( 35 )
for i in range ( 26 ):
    t.right ( 2.5 )
    t.forward ( 0.75 )
t.forward ( 15 )
for i in range ( 47 ):
    t.right ( 2.5 )
    t.forward ( 0.3 )
t.forward ( 90 )
for i in range ( 25 ):
    t.right ( 2.5 )
    t.forward ( 0.75 )
t.forward ( 14 )
for i in range ( 46 ):
    t.right ( 2.5 )
    t.forward ( 0.3 )
t.forward ( 35 )
t.left ( 115 )
t.forward ( 75 )
t.left ( 65 )
t.forward ( 52 )
for i in range ( 57 ):
    t.left ( 2 )
    t.forward ( 0.467 )
t.left ( 1 )
t.forward ( 140 )
for i in range ( 32 ):
    t.left ( 2 )
    t.forward ( 2 )
t.forward ( 100 )
for i in range ( 57 ):
    t.left ( 2 )
    t.forward ( 0.467 )
t.left ( 0.5 )
t.forward ( 15 )
t.end_fill() #"結束填充"
