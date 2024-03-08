import cv2
import pytesseract
import os

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(2)

img_counter = 0

def take_image():
	img_name = "opencv_frame1.png"
	cv2.imwrite(img_name, frame1)
	print("written!")
	img_name = "opencv_frame2.png"
	cv2.imwrite(img_name, frame2)
	print("written!")
	bgr_img1 = cv2.imread("opencv_frame1.png")  # Load the image
	gry_img1 = cv2.cvtColor(bgr_img1, cv2.COLOR_BGR2GRAY)
	gry_img1 = cv2.bilateralFilter(gry_img1, 11, 17, 17)
	thresh1 = cv2.adaptiveThreshold(gry_img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 21)
	border_img1 = cv2.copyMakeBorder(thresh1, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=255)
	cv2.imwrite("thresh_image.png", border_img1)
	txt1 = pytesseract.image_to_string(border_img1, config='--psm 6')
	print(txt1) 
	os.remove("opencv_frame1.png")
	os.remove("opencv_frame2.png")

def close_camera():
	cam1.release()
	cam2.release()
	cv2.destroyAllWindows()
 
while True:
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    if not ret1:
        print("failed to grab frame1")
        break
    if not ret2:
        print("failed to grab frame2")
        break
    take_image()
    break
    
close_camera()