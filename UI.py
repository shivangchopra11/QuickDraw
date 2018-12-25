import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from my_preprocessing import parse_line


lstm_model = load_model('./Models/Quick_Draw_LSTM.h5')
cnn_model = load_model('./Models/Quick_Draw_CNN.h5')


x_g = []
y_g = []
time = []
ctr=0


drawing = False # true if mouse is pressed

def draw_circle(event,x,y,flags,param):
	global ix,iy,drawing,mode,x_g,y_g,time,ctr,img

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True

	elif event == cv2.EVENT_MOUSEMOVE:

		if drawing == True:
			ctr+=1
			print ctr
			cv2.circle(img,(x,y),4,(0,0,255),-1)
			if ctr%5==0:
				x_g.append(x)
				y_g.append(y)
				time.append(ctr)
				print(x,y)
				arr = np.zeros((len(x_g), 3), dtype=np.int)
				arr[:,0] = x_g
				arr[:,1] = y_g
				arr[:,2] = time
				if arr.shape[0]>100:
					arr1 = parse_line(arr)
					arr2 = arr1[-100:,]
					arr2 = arr2.reshape(1,100,3)
					result = lstm_model.predict(arr2)
					ans = np.argmax( result[0] )
					print("Prediction:"+str(ans))

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.circle(img,(x,y),4,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
	cv2.imshow('image',img)
	img1 = cv2.resize(img,(28,28))
	img1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	cv2.imshow('processed_img',img1)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
img1 = img1.reshape((1,28,28,1))
img1 = img1/255.0
result = cnn_model.predict(img1)
ans = np.argmax( result[0] )
print(ans)