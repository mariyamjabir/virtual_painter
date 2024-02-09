import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector()

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
        xp,yp=0,0
        if fingers[1] and fingers[2]:
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
                    print("yellow")
                    draw_colour = (0,0,0)

                cv2.rectangle(img,(x1,y1),(x2,y2),color=draw_colour,thickness=-1)
        #drawing mode
        if fingers[1] and not fingers[2]:
            print("Drawing mode")
            cv2.circle(img,(x1,y1),15,color=draw_colour,thickness=-1)
        
        
            

    cv2.imshow("Virtual Painter", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()