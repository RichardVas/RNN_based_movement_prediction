import cv2

import imageio

cap = cv2.VideoCapture('Highway - 20090.mp4_predicted.mp4')

image_lst = []

count = 1
out= cv2.VideoWriter()
while True:
    if(count <= 100):
        ret, frame = cap.read()

        #frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        cv2.imwrite("frame%d.jpg" % count, frame) 
        cv2.imshow('a', frame)

        count +=1

        if(count >= 100):
            break
        key = cv2.waitKey(1)
        if key == ord('q'):
            break




cap.release()
cv2.destroyAllWindows()

