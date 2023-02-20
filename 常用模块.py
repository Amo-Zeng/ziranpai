#! /usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#import scipy.interpolate as itp
#from matplotlib.mlab import griddata
#import matplotlib.tri as tri
#from scipy import integrate
#import vegas
#import os
#XLog=False
#YLog=False
#XBigTicker=0
#XSmallTicker=0
#YBigTicker=0
#YSmallTicker=0
#XLabel="x axis"
#YLabel="y axis"
#YMin=0
#YMax=0
#Title="title"
#SaveName="savename.pdf"
#def Reset():
#    XLog=False
#    YLog=False
#    XBigTicker=0
#    XSmallTicker=0
#    YBigTicker=0
#    YSmallTicker=0
#    XLabel="x axis"
#    YLabel="y axis"
#    YMin=0
#    YMax=0
#    Title="title"
#    SaveName="savename.pdf"
#def SetPlot():
#    plt.xlabel(XLabel)
#    plt.ylabel(YLabel)
#    plt.title(Title)
#    ax=plt.gca()
#    if XLog:
#        ax.set_xscale('log')
#    if YLog:
#        ax.set_yscale('log')
#    if YMax!=0:
#        plt.ylim(YMin,YMax)
#    if XBigTicker!=0:
#        xmajorLocator=MultipleLocator(XBigTicker)#将x主刻度标签设置为20的倍数
#        #xmajorFormatter=FormatStrFormatter('%d')#设置x轴标签文本的格式
#        xminorLocator=MultipleLocator(XSmallTicker)#将x轴次刻度标签设置为5的倍数
#        ymajorLocator=MultipleLocator(YBigTicker)#将y轴主刻度标签设置为0.5的倍数
#        #ymajorFormatter=FormatStrFormatter('%d')#设置y轴标签文本的格式
#        yminorLocator=MultipleLocator(YsmallTicker)#将此y轴次刻度标签设置为0.1的倍数
#        #设置主刻度标签的位置,标签文本的格式  
#        ax.xaxis.set_major_locator(xmajorLocator)  
#        #ax.xaxis.set_major_formatter(xmajorFormatter)  
#  
#        ax.yaxis.set_major_locator(ymajorLocator)  
#        #ax.yaxis.set_major_formatter(ymajorFormatter)  
#  
#        #显示次刻度标签的位置,没有标签文本  
#        ax.xaxis.set_minor_locator(xminorLocator)  
#        ax.yaxis.set_minor_locator(yminorLocator)
#    plt.legend()
#def Plot(func,xmin,xmax,ndot,*args):
#    x=np.linspace(xmin,xmax,ndot)
#    y=func(x) 
#    plt.plot(x,y,*args)
#    SetPlot()
#    plt.show()
#    if SaveName!="savename.pdf":
#        plt.savefig(SaveName)
#def Scatter(x,y,*args):
#    plt.scatter(x,y,*args)
#    SetPlot()
#    plt.show()
#    if SaveName!="savename.pdf":
#        plt.savefig(SaveName)
#def Load(filename,cols):
#    return np.loadtxt(filename, dtype='float', unpack=True, usecols=cols)
#def LinSpace(xmin,xmax,ndot):
#    return list(np.linspace(xmin,xmax,ndot))
#def LogSpace(xmin,xmax,ndot):
#    return list(np.logspace(xmin,xmax,ndot))
#def Interpolate(x,y,xi):
#    return itp.splev(xi,itp.splrep(x,y))
#def Interpolate3D(x,y,z,xi,yi):
#    triang = tri.Triangulation(x, y)
#    interpolator = tri.LinearTriInterpolator(triang, z)
#    Xi, Yi = np.meshgrid(xi, yi)
#    return interpolator(Xi, Yi)
#    #return griddata(x, y, z, xi, yi)
#def Contourf(x,y,z,qujian,*args):
#    plt.contourf(x,y,z,levels=qujian,*args)
#    SetPlot()
#    plt.show()
#    if SaveName!="savename.pdf":
#        plt.savefig(SaveName)
#def Contour(x,y,z,qujian,*args):
#    plt.contour(x,y,z,levels=qujian,*args)
#    SetPlot()
#    plt.show()
#    if SaveName!="savename.pdf":
#        plt.savefig(SaveName)
#def IntegrateRomberg(func,xmin,xmax):
#    return integrate.romberg(func,xmin,xmax)
#def IntegrateVegas(func,qujian):
#    integ = vegas.Integrator(qujian)
#    return integ(func, nitn=10, neval=3000).mean()
import os
#def genxwzfunc1(cmd):
#    return lambda x: os.popen('bash ~/.xwz.sh '+cmd+' '+str(x)).readlines()
#def genxwzfunc2(cmd):
#    return lambda x,y: os.system('bash ~/.xwz.sh '+cmd+' '+str(x)+' '+str(y))
#def genxwzfunc3(cmd):
#    return lambda x,y,z: os.system('bash ~/.xwz.sh '+cmd+' '+str(x)+' '+str(y)+' '+str(z))
#def genxwzfunc4(cmd):
#    return lambda x,y,z,w: os.system('bash ~/.xwz.sh '+cmd+' '+str(x)+' '+str(y)+' '+str(z)+' '+str(w))
def genxwzfunc(cmd):
    def res(*x):
        #print('bash ~/.xwz.sh '+cmd+' '+' '.join([str(i) for i in x]))
        t=os.popen('bash ~/.xwz.sh '+cmd+' '+' '.join([str(i) for i in x])).readlines()
        #print("27",t[0].strip("\n"),"hi")
        if len(t)==0:
            return "done"
        return t[0].strip("\n") if len(t)==1 else [i.strip("\n") for i in t]
    return res
    #return lambda *x: os.popen('bash ~/.xwz.sh '+cmd+' '+' '.join([str(i) for i in x])).readlines()[0].strip("\n")

xwz1={"免密登陆":genxwzfunc('mianmissh'),"行数":genxwzfunc('hang'),"最后行":genxwzfunc('lasth'),"全查":genxwzfunc('chazhaoa')}
xwz2={"文搜":genxwzfunc('cg'),"终循":genxwzfunc('xunl'),"目搜":genxwzfunc('lg'),"查找":genxwzfunc('chazhao'),"显示行":genxwzfunc('xianshih'),"删除行":genxwzfunc('shanchuh'),"循次":genxwzfunc('xunc'),"追加行":genxwzfunc('zhuijia')}
xwz3={"如果":genxwzfunc('if'),"替换":genxwzfunc('tihuan'),"插入":genxwzfunc('charu')}
xwz4={"行中替换":genxwzfunc('tihuanh')}

函子={}#接受一个变量的函数字典
#函丑={"载入":Load,"维积分":IntegrateVegas,"散点图":Scatter}#接受两个变量的函数字典，依此类推
函丑={}
#函寅={"插值":Interpolate,"线性数组":LinSpace,"对数数组":LogSpace,"荣积分":IntegrateRomberg}
#函卯={"画线":Plot,"等高线":Contour,"等高区":Contourf}
#函辰={"三维插值":Interpolate3D}
函寅={}
函卯={}
函子.update(xwz1)
函丑.update(xwz2)
函寅.update(xwz3)
函卯.update(xwz4)
函辰={}
函巳={}
函午={}
函未={}
函申={}
函酉={}
函戌={}
函亥={}
函括={"有用":genxwzfunc('yy'),"别名":genxwzfunc('alias')}
#函括={"等高线1":Contour,"等高区1":Contourf}#接受任意个变量的函数字典，引用函数时需要用括号把函数和变量括起来。
