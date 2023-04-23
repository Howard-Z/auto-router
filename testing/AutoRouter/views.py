from django.shortcuts import render
import subprocess
import cv2
from pytesseract import pytesseract


def read_image(image):
    print(image)
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
                                 cv2.THRESH_BINARY_INV)

    # Can change kernel size based on area of text
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))
    # Change iteration numbers
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=3)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    im2 = img.copy()
    temp_dict = {}
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Draw the bounding box on the text area
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the bounding box area
        cropped = im2[y:y + h, x:x + w]

        # open the text file
        # file = open("text_output2.txt", "a")

        # Using tesseract on the cropped image area to get text
        text = pytesseract.image_to_string(cropped)
        texts = text.split(':')
        for i in range(len(texts)):
            texts[i] = texts[i].strip()
        temp_dict[texts[0]] = texts[1]

    return (temp_dict)


def execute_script(request):
    if request.method == "POST":
        image = request.POST['image']
        print(image)
        dict = read_image("static/"+image)
        # print(dict)
        return render(request, 'results.html', {'dict': dict})

    image = "static/test3.png"
    dict = read_image(image)

    return render(request, 'results.html', {'dict': dict})


def home(request):
    return render(request, 'home.html')


def new_router(request):
    return render(request, 'new_router.html')
# Create your views here.
