# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract

class ValidateImageCode():
    def __init__(self):
        pass
    def Image_to_String(self,x,y,width,height):
       rangle = (int(x), int(y), int(x + int(width)), int(y + int(height))) #写成我们需要截取的位置坐标
       i=Image.open("D://aa.png")   #打开截图
       frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
       frame4.save('D://frame4.png')
       img = Image.open('D://frame4.png')
       print img.load()
       aa =pytesseract.image_to_string(img)
       print u"识别的验证码为："
       return aa
if __name__ == "__main__":
   a = ValidateImageCode().Image_to_String()
   print a