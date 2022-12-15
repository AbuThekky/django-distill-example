# from bs4 import BeautifulSoup
# import requests

# url = "https://centralmosque.org.uk/"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# prayer_start = print(doc.find_all('div', {'class': 'prayer-start'}))

# prayer_times_start = []
# prayer_times_jamaat = []

# for div in doc.find_all('div', {'class': 'prayer-start'}):
#     prayer_times_start.append(div.text)
    
# for div in doc.find_all('div', {'class': 'prayer-jamaat'}):
#     prayer_times_jamaat.append(div.text)
    
# print(prayer_times_start)
# print(prayer_times_jamaat) 

# ------------------------------------------------------------------------------------------------
# 
# # Page segmentation modes:
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line,
#        bypassing hacks that are Tesseract-specific.##




import pytesseract
import PIL.Image
import cv2

# 1ST IMAGE TO GENERATE TEXT~ -

myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("YCC_Prayer_Timetable_December_2022.jpg"), config=myconfig)
# print(text)

new_list = text.split("|")

numbers = []
times = []
for item in new_list:
    for subitem in item.split():
        if(subitem.isdigit() and len(subitem) == 3): 
            for a in str(subitem): 
             numbers.append(a)
             
for i in range(0,len(numbers)-1,3):
    test = numbers[i]+":"+numbers[i+1]+numbers[i+2]
    times.append(test)
    
    
        
        

    
print(times)
 





# 2ND IMAGE BOX GENERATOR

# myconfig = r"--psm 11 --oem 3"

# img = cv2.imread("YCC_Prayer_Timetable_December_2022.jpg")

# height, width, _ = img.shape

# boxes = pytesseract.image_to_boxes(img, config=myconfig)
# for box in boxes.splitlines():
#     box = box.split(" ")
#     img = cv2.rectangle(img, (int(box[1]), height - int(box[2])),(int(box[3]), height - int(box[4])), (0, 255, 0),2 )
    
# cv2.imshow("img",img)
# cv2.waitKey(0)