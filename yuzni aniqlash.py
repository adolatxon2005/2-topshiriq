# OpenCV program to detect face in real time
# python OpenCV import kutubxonalari
# uning funksionalligi qaerda
import cv2 

# kerakli o'qitilgan XML tasniflagichlarini yuklang
# https://github.com/Itseez/opencv/blob/master/
# data/haarcascades/haarcascade_frontalface_default.xml
# O'qitilgan XML klassifikatorlari ba'zilarining ba'zi xususiyatlarini tavsiflaydi
#Biz kaskad funktsiyasini aniqlamoqchi bo'lgan 
# ob'ekt o'qitilgan
# ko'p ijobiy (yuzlar) va salbiy (yuz bo'lmagan)
# ta rasm.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# https://github.com/Itseez/opencv/blob/master
# /data/haarcascades/haarcascade_eye.xml
# Ko'zlarni aniqlash uchun o'qitilgan XML fayli
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

# kameradan kadrlarni suratga olish
cap = cv2.VideoCapture(0)

#Agar suratga olish ishga tushirilgan bo'lsa, 
# tsikl ishlaydi.
while 1: 

    # kameradan kadrlarni o'qiydi
    ret, img = cap.read() 

    # har bir ramkaning kulrang shkalasiga aylantirish
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Kirish tasviridagi turli oʻlchamdagi yuzlarni aniqlaydi
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        # Yuzga to'rtburchak chizish uchun
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Kirish tasvirida turli o'lchamdagi ko'zlarni aniqlaydi
        eyes = eye_cascade.detectMultiScale(roi_gray) 

        # Ko'zlarga to'rtburchak chizish
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

    # Tasvirni oynada ko'rsatish
    cv2.imshow('img',img)

    # Esc tugmachasini to'xtatishni kuting
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Oynani yoping
cap.release()

# Har qanday bog'liq xotiradan foydalanishni ajrating
cv2.destroyAllWindows()
