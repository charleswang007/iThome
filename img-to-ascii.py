import cv2
#ascii_char = list("01") # 可以自己改成想要標記的符號
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

WIDTH = 30 # 寬
HEIGHT = 30 # 高

def get_char(gray_value):
   length = len(ascii_char) # 根據傳進來的灰階值判斷此位置要使用哪個字元
   unit = 256.0 / length # 區分灰階範圍
   return ascii_char[int(gray_value / unit)]

if __name__ == '__main__':
   img = cv2.imread('image/dog.jpg', cv2.IMREAD_GRAYSCALE) # 將圖片自動轉為灰階圖片
   img = cv2.resize(img, (WIDTH, HEIGHT)) # 將灰階圖縮小成指定大小
   txt = ""
   for i in range(HEIGHT):
       for j in range(WIDTH):
           txt += get_char(img[i][j]) # 轉為指定字符
       txt += '\n'
   print(txt)