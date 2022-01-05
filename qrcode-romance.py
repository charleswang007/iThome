import qrcode
from PIL import Image

def make_qrcode(text): # 建立QR Code
    qr = qrcode.QRCode(version=10, box_size=8, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")
    
def add_img(back_image, logo_image):
    qrcode_size = back_image.size[0] # 得到整張QR Code的邊長
    qr_back = Image.new('RGBA', back_image.size, 'white') # 建一個全白背景
    qr_back.paste(back_image) # 貼上QR code
    logo_size = int(qrcode_size / 5) # 調整logo大小
    logo_offset = int((qrcode_size - logo_size) / 2) # 把logo位置設定在正中間
    resized_logo = logo_image.resize((logo_size, logo_size))
    qr_back.paste(resized_logo, box=(logo_offset, logo_offset))
    return qr_back
       
logo_image_file = 'image/dog2.jpg'
text = '跟偶交往好嗎 (摸頭燦笑'
logo_image = Image.open(logo_image_file)
qr_code = make_qrcode(text)
final = add_img(qr_code, logo_image)
final.save('qrcode.png')
final.show()