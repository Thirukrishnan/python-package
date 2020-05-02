import cv2

# Load the cascade
car_cascade = cv2.CascadeClassifier('final.xml')

# Read the input image
img = cv2.imread(r'C:\Users\BALAMURUGAN\Desktop\final\pics\car 13.jpg')
#img=cv2.imread('.jpg')
img=cv2.resize(img,(320,240))

# Convert into grayscale
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect cars
cars= car_cascade.detectMultiScale(gray, 1.05, 4)

if  len(cars)!=0:
#draw rectangle
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
else:
    car_cascade = cv2.CascadeClassifier('final 2.xml')
    cars= car_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()


