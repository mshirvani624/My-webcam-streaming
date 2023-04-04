import cv2
import numpy as np
import time

# Programmer Mohammad Shirvani
# Date 1402/12/28

# print(time.time())
# quit()
t0=time.time()

cap=cv2.VideoCapture(0)
while True:
	ret, frame= cap.read()
	# gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	if ret:

		# width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		# height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		# fps=cap.get(cv2.CAP_PROP_FPS)
		# print(width,height,fps)
		# frame=cv2.flip(frame,1)
		# frame=255-frame
		t1=time.time()-t0
		frame=cv2.flip(frame,1)
		t1_str=str(round(t1,2))
		# cv2.putText(frame,"Mohammad",(200,200),cv2.FONT_HERSHEY_SIMPLEX,
			         # 2,(0,255,255),5)
		cv2.putText(frame,t1_str,(100,100),cv2.FONT_HERSHEY_SIMPLEX,
			         2,(0,0,255),2)
		# frame_little=frame[100:200,300:500]
		cv2.imshow("webcamasdfasdf",frame)
		q=cv2.waitKey(1)
		if q==ord('q'):
			break
cv2.destroyAllWindows()
cap.release()

		