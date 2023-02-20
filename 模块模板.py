import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def 读入图片(ifile):
    print(np.array(Image.open(ifile)))
    return np.array(Image.open(ifile))
def 显示图像(a_img):
    plt.imshow(a_img)
    plt.show()
函子={"读入图片":读入图片,"显示图像":显示图像}#接受一个变量的函数字典
函丑={}#接受两个变量的函数字典，依此类推
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
函括={}#接受任意个变量的函数字典，引用函数时需要用括号把函数和变量括起来。
