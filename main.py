import cv2
import HandTrackingModule as htm
import numpy as np

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
draw_colour = (0,0,255)
img_canvas = np.zeros((620,1010,3),np.uint8)
xp,yp=0,0

while True:
    x,img = cap.read()
    img = cv2.resize(img,(1010,620))
    img = cv2.flip(img,1)

    #draw rectangle
    img = cv2.rectangle(img,(10,100),(200,10),(255,0,0),-3)
    img = cv2.rectangle(img,(210,100),(400,10),(0,255,0),-3)
    img = cv2.rectangle(img,(410,100),(600,10),(0,0,255),-3)
    img = cv2.rectangle(img,(610,100),(800,10),(0,255,255),-3)
    img = cv2.rectangle(img,(810,100),(1000,10),(255,255,255),-3)
    img = cv2.putText(img,text="Eraser", org=(850,60),color=(0,0,0),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,thickness=3)

    # detect hands
    img = detector.findHands(img)
    
    #to get coordinator as landmarklist
    lmlist = detector.findPosition(img)
    print(lmlist)

    # get coordinates of drawing fingers that is x1y1 for coordinate 8(index fingertip) and x2y2 for coordinate 12(middle finger tip)
    if len(lmlist)!=0:
        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[12][1:]
    
        #detect if fingers are up
        fingers = detector.fingersUp()
        print(fingers)

        #selection mode
        
        if fingers[1] and fingers[2] and not any(fingers[3:]):
            print("Selection mode")
            
            #to select the colours of finger tips
            if y1<100:
                if 10<=x1<=200:
                    print("red")
                    draw_colour = (255,0,0)
                elif 210<=x1<=400:
                    print("green")
                    draw_colour = (0,255,0)
                elif 410<=x1<=600:
                    print("blue")
                    draw_colour = (0,0,255)
                elif 610<=x1<=800:
                    print("yellow")
                    draw_colour = (0,255,255)
                elif 810<=x1<=1000:
                    print("eraser")
                    draw_colour = (0,0,0)

                cv2.rectangle(img,(x1,y1),(x2,y2),color=draw_colour,thickness=-1)
        #drawing mode
                
        if (fingers[1] and not any(fingers[2:])):
            print("Drawing mode")
            cv2.circle(img,(x1,y1),15,draw_colour,thickness=-1)

            if xp==0 and yp==0:
             xp, yp = x1, y1

            if draw_colour==(0,0,0):

                cv2.line(img,(xp,yp),(x1,y1),color = draw_colour,thickness=50)                
                cv2.line(img_canvas,(xp,yp),(x1,y1),color = draw_colour,thickness=50)
            else:
                cv2.line(img,(xp,yp),(x1,y1),color = draw_colour,thickness=15)
                cv2.line(img_canvas,(xp,yp),(x1,y1),color = draw_colour,thickness=15)
            xp,yp = x1,y1

    # To join 2 windows
    img_grey = cv2.cvtColor(img_canvas,cv2.COLOR_BGR2GRAY)
    _,img_inv = cv2.threshold(img_grey,20,255,cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv,cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img,img_inv)
    img = cv2.bitwise_or(img,img_canvas)
    img = cv2.addWeighted(img,1,img_canvas,0.5,0)
                    

    cv2.imshow("Virtual Painter", img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()