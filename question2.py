import cv2

image=cv2.imread("images.jpg")
cv2.imshow("original",image)
blue=image[:,:,0]
cv2.imshow("blue",blue)
green=image[:,:,1]
cv2.imshow("green",green)
red=image[:,:,2]
cv2.imshow("red",red)

final=cv2.merge((blue,green,red))
cv2.imshow("final",final)
cv2.waitKey(0)

