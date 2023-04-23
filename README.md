# Auto-Router
## Inspiration
**An anecdote from one of our developers:** <br>
Over winter break, I went on a vacation to the mountains for a skiing trip with my roommates. Upon checking into the hostel, I found the WiFi network to be unbearably slow. I couldn't believe that the WiFi could be this bad and count as "Free WiFi". So I took the initiative to see if the owners configured their wireless router improperly. When I tried the gateway IP. I was met with the usual login page. <br><br>
After only 2 quick attempts, I was in. This became a major security concern for other guests and me staying at the hostel. When I informed the landlord, they told me they had no idea that the router was so vulnerable and asked me if I could change the password for them. They didn't even know how to access the login page and I found that to be concerning. If people don't even know how to access their router's login page, how could they possibly secure their network against attackers? <br><br>

That is what this project aims to solve. We developed a web-based tool that makes it very intuitive to see if your router is using default credentials and change them.<br>


## What it does
After user approval, the program attempts the brute force the router's username and password by guessing the commonly used credentials from many different manufacturers.  If the program can log into the router, it then warns the user that their router is insecure and that they should change their router's password and takes them to the router's change password page.  If the program is unable to guess the password it tells the user that their credentials are not commonly found on the internet, and shows them other ways to harden their security.

## How we built it
Using Django and Python, we created a web-based GUI for running our Python scripts.
For scraping the router login page, we used the Selenium package.

## Challenges we ran into
Web scraping using Python was brand new to all of us and Django was unfamiliar to most of us. There was a steep learning curve in learning how to scrape web pages. Initially, we wanted to have features such as uploading pictures of router stickers to automatically extract credentials, connect to the WiFi network, and configure the router. But that proved to be too difficult.

## Accomplishments that we're proud of
We're proud of the fact that our project works and can guide a user through the entire process of detecting if their router is insecure. Being able to see how easy it is to use our tool makes us proud that we accomplished our objective.

## What we learned
We learned a great many things during this project. Web scraping is not as easy as searching through HTML files. We learned how to use Selenium, and how we can secure the everyday home networks we use.


## What's next for Router Secure
At the current point, Router Secure is in a very early phase of development.  In the future, we hope to allow further router configuration through our tool such as SSID changing, updating firmware, turning off WPS, and more. We also would like to add the automatic configuration of brand-new networks by simply uploading a picture of the sticker on the router containing the credentials.

# Installation
Requires Python 3 and Django to be installed
```
cd testing
python manage.py runserver
```
## Libraries Used
```
pip install selenium
pip install mac-vendor-lookup
pip install scapy
pip install pytessseract
pip install opencv-python
```

### Tesseract Installation
Install Google Tesseract OCR, installation information can be found [here](https://tesseract-ocr.github.io/tessdoc/Installation.html). 

## Acknowledgements
Thank you to Nicole Ju for working on the automatic connection to WiFi feature. Unfortunately we could not have hardware present for us to tinker with so this feauture could not ultimately be used. Thank you to Andy Zhang for writing the computer vision code to process a router label. Again, we could not use this feature given the circumstances, but we hope to incorporate it in the future. Their code can be found in commit ID: 70f0535e1cc7fb0ff56b21c8dc559dea1455d860 and earlier.
