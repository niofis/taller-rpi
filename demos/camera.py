from remote import initConnection, get_picture
from PIL import Image


initConnection(id=1234, url="https://localhost:3443")
with open('./picture.jpg', 'wb') as f:
    f.write(get_picture())
Image.open('./picture.jpg').show()
