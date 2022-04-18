import cv2

import imageio

cap = cv2.VideoCapture('traffic_predicted.mp4')

image_lst = []

count = 0
out= cv2.VideoWriter()
while True:
    if(count > 10 and count < 25):
        ret, frame = cap.read()

        #frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        cv2.imwrite("frame%d.jpg" % count, frame) 
        cv2.imshow('a', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    if(count >= 26):
        break
    count +=1


cap.release()
cv2.destroyAllWindows()

# Convert to gif using the imageio.mimsave method
#imageio.mimsave('asssqw.gif', image_lst, fps=60)