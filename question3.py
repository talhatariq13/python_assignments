import cv2
import numpy as np


def euc(img,img2):
    print(img.shape)
    mi = np.sum((img2[0] - img ** 2))

    for i in range(1,8):
        print(img2[i])

        if np.sum((img2[i]-img**2))<mi:
            mi=np.sum((img2[i]-img**2))
            img=img2[i]

    return img





images=["quaid1.jpg","quaid2.jpg","quaid3.jpg","quaid4.jpg","quaid5.jpg","quaid6.jpg","quaid7.jpg","quaid8.jpg","quaid9.jpg"]










for i in range(9):
    # images[i]=cv2.resize(images[i], (3,3), interpolation = cv2.INTER_AREA)
    print(i)
    images[i]=cv2.imread(images[i])
    images[i] = cv2.resize(images[i], (9, 9), interpolation=cv2.INTER_AREA)

original_image=cv2.imread("quaid.jpg")

original_image= cv2.resize(original_image, (27, 27), interpolation=cv2.INTER_AREA)


print(type(images[0]))
print(original_image)
for i in range(0,27,9):
    for j in range(0,27,9):

        print(j**2)
        print(j)
        original_image[i:(i+9),j:(j+9)]=euc(original_image[i:(i+9),j:(j+9)],images)



print("a",original_image)
original_image=cv2.resize(original_image,(128,128),interpolation=cv2.INTER_CUBIC)
cv2.imshow("after_euclidean",original_image)
cv2.waitKey(0)