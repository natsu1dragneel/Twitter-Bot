import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = ' '

# download page
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate  elements of image tag
image_tags = soup.findAll('img')

# create directory 
if not os.path.exists('new folder'):
    os.makedirs('new folder')

# move to new directory
os.chdir('new folder')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('folder-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass