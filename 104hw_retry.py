import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
             (100,330),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (0,0,255)
             )

cv2.putText(img,
            "Mercury",
             (110,250),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Venus",
             (190,260),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Earth",
             (280,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Mars",
             (380,255),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Jupiter",
             (550,50),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )            
            
cv2.putText(img,
            "Saturn",
             (790,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             ) 

cv2.putText(img,
            "Uranus",
             (970,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Neptune",
             (1110,140),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.imshow("Output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)