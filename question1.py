import numpy as np

import cv2
def colored_image(input):
    bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for y in range(input.shape[0]):
        for x in range(input.shape[1]):
            if image[y, x] == 255 and y < 7:
                bgr[y,x,:]=[235,206,135]
            elif image[y, x] == 255 and (y > 7 or y==7 ):
                bgr[y,x,:]=[203,192,255]
            elif image[y,x]==155:
                bgr[y, x, :] = [181, 228, 255]




    print(bgr)
    cv2.imshow("need to return",cv2.resize(bgr, (512,512), interpolation = cv2.INTER_AREA))






image=np.zeros((10,10),dtype="uint8")

image[2:4,2:4]=255

image[3:4,7:9]=255

image[4:7,5:6]=155

image[7:9,3:4]=255

image[7:9,7:8]=255

image[8:9,4:7]=255


colored_image(image)






print(image)
cv2.imshow("made image",cv2.resize(image, (512,512), interpolation = cv2.INTER_AREA))
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)