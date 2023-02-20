import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
def 读入图像(ifile):
    #print(np.array(Image.open(ifile).convert('L')))
    #return np.array(Image.open(ifile).convert('L'))
    return np.array(Image.open(ifile))
def 显示图像(a_img):
    print(a_img.shape)
    if len(a_img.shape)==2:
        plt.imshow(a_img,cmap='gray')
    else:
        plt.imshow(a_img)
    plt.show()
def 透明图像(a_img,alpha):
    if len(a_img.shape)!=3:
        print("数据格式不对！应为RGB(M*N*3)或RGBA(M*N*4)")
    img=[]
    if a_img.shape[2]==3:
        for i in range(a_img.shape[0]):
            row=[]
            for j in range(a_img.shape[1]):
                xiang=list(a_img[i,j])
                xiang.append(alpha)
                row.append(xiang)
            img.append(row)
    elif a_img.shape[2]==4:
        for i in range(a_img.shape[0]):
            row=[]
            for j in range(a_img.shape[1]):
                xiang=list(a_img[i,j][:-1])
                xiang.append(alpha)
                row.append(xiang)
            img.append(row)
    plt.imshow(img)
    plt.show()
    return np.array(img)
def 灰度图像(a_img):
    if len(a_img.shape)!=3:
        print("数据格式不对！应为RGB(M*N*3)或RGBA(M*N*4)")
    img=[]
    if a_img.shape[2]==4:
        a_img=RGBA2RGB(a_img)
    if a_img.shape[2]==3:
        for i in range(a_img.shape[0]):
            row=[]
            for j in range(a_img.shape[1]):
                xiang=a_img[i,j][0]* 299/1000+a_img[i,j][1]* 587/1000+a_img[i,j][2]* 114/1000
                row.append(xiang)
            img.append(row)
    plt.imshow(img,cmap='gray')
    plt.show()
    return np.array(img)
def 函数图像(f,chang=100,kuan=100,beishu=1,xuanjiao=0,fanzhuan=False,pingyix=0,pingyiy=0,r=0,b=0,g=0,alpha=255):
    img=[]
    for i in range(chang):
        row=[]
        for j in range(kuan):
            try:
                f(i-chang/2)
            except Exception as e:
                xiang=[255,255,255,255]
                row.append(xiang)
                continue
            if abs(f(i-chang/2)-(j-kuan/2))<6: 
                xiang=[math.ceil(r+255*abs(f(i-chang/2)-(j-kuan/2))/6),math.ceil(b+255*abs(f(i-chang/2)-(j-kuan/2))/6),math.ceil(g+255*abs(f(i-chang/2)-(j-kuan/2))/6),alpha]
                row.append(xiang)
            else:
                xiang=[255,255,255,255]
                row.append(xiang)
        img.append(row)
    显示图像(np.array(img))
    return np.array(img)
def RGBA2RGB(a_img):
    bgr=255;bgb=255;bgg=255
    img=[]
    for i in range(a_img.shape[0]):
        row=[]
        for j in range(a_img.shape[1]):
            xiang=[]
            xiang.append(bgr*(1-a_img[i,j][3]/255)+a_img[i,j][3]/255*a_img[i,j][0])
            xiang.append(bgb*(1-a_img[i,j][3]/255)+a_img[i,j][3]/255*a_img[i,j][1])
            xiang.append(bgg*(1-a_img[i,j][3]/255)+a_img[i,j][3]/255*a_img[i,j][2])
            row.append(xiang)
        img.append(row)
    return np.array(img)
def 缩放图像(a_img,beishu):
    im=Image.fromarray(a_img)
    im.resize((math.ceil(im.width*beishu),math.ceil(im.height*beishu))).show()
    return np.array(im.resize((math.ceil(im.width*beishu),math.ceil(im.height*beishu))))
def 旋转图像(a_img,jiaodu):
    im=Image.fromarray(a_img)
    im.rotate(jiaodu).show()
    return np.array(im.rotate(jiaodu))
def 保存图像(a_img,ming):
    if len(a_img.shape)==2:
        plt.imsave(ming,a_img,cmap='gray')
    else:
        plt.imsave(ming,a_img.astype(np.uint8))
    #try:
    #    im=Image.fromarray(a_img,'RGBA')
    #    print(im)
    #    im.convert("RGB").show()
    #    im.save(ming)
    #except Exception as e:
    #    raise e

函子={"读入图像":读入图像,"灰度图像":灰度图像,"显示图像":显示图像}#接受一个变量的函数字典
函丑={"透明图像":透明图像,"缩放图像":缩放图像,"旋转图像":旋转图像,"保存图像":保存图像}#接受两个变量的函数字典，依此类推
函寅={}
函卯={}
函辰={}
函巳={}
函午={}
函未={}
函申={}
函酉={}
函戌={}
函亥={}
函括={"函数图像":函数图像}#接受任意个变量的函数字典，引用函数时需要用括号把函数和变量括起来。
