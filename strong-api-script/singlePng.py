import requests
from PIL import Image
from io import BytesIO

def print_hi(name):
    print(f" {name}")

responses = requests.get("http://10.37.3.130:10001/radar/DSD_DMP/2023/11/11/20231111_0120.png")

image = Image.open(BytesIO(responses.content))
image.show()
if __name__ == '__main__':
    print_hi('')