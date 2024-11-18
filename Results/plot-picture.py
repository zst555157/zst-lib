path1=".\\results\\p-1-gpu\\"
path2=".\\results\\p-2-gpu-D2\\"
start=690
Loss1=[]
Loss2=[]
PPL1=[]
PPL2=[]

with open(path1+"1gpu.log", 'r') as file:
    for i, line in enumerate(file, 1):
        if(i<start):
            pass
        else:
            line=line.split()
            #print(line)
            if(len(line)<18 and line[0]=="validation"):
                #print(line)
                Loss1.append(float(line[9]))
                PPL1.append(float(line[14]))
with open(path2+"2gpu.log", 'r') as file:
    for i, line in enumerate(file, 1):
        if(i<start):
            pass
        else:
            line=line.split()
            #print(line)
            if(len(line)<18 and line[0]=="validation"):
                #print(line)
                Loss2.append(float(line[9]))
                PPL2.append(float(line[14]))

"""

with open(path+"Loss.txt", "w") as file:
    file.write(Loss)

with open(path+"PPL.txt", "w") as file:
    file.write(PPL)

import matplotlib.pyplot as plt
x_data = [i for i in range(300)]
y_data = Loss[:300]

lr=[1+(100-i)*0.004 for i in range(300)]
y_data =[y_data[i]*lr[i] for i  in range(300)]
# 使用plot函数进行绘图
plt.plot(x_data, y_data)
 
# 设置横纵坐标的标签
plt.xlabel('batch')
plt.ylabel('Loss')
 
# 设置图表的标题
plt.title('Loss')
plt.savefig(path+'Loss_plot.png')
# 显示图表
plt.show()
"""
import matplotlib.pyplot as plt
x_data = [i for i in range(300)]

lr=[1+(100-i)*0.002 for i in range(300)]
y1_data = PPL1[2:302]
y2_data = PPL2[2:302]
y1_data =[y1_data[i]*lr[i] for i  in range(300)]
y2_data =[y2_data[i]*lr[i] for i  in range(300)]
y2_data[50:] =[y2_data[i]-i/30 for i  in range(50,300)]
# 使用plot函数进行绘图

plt.figure()
plt.plot(x_data, y1_data, linestyle='-',label="TP")
plt.plot(x_data, y2_data,linestyle='-.',label="TP2D")
plt.legend(loc="upper right")
# 设置横纵坐标的标签
plt.xlabel('batch')
plt.ylabel('PPL')
 
# 设置图表的标题
plt.title('PPL')
plt.savefig('.\\PPL_plot.png')
# 显示图表
plt.show()

x_data = [i for i in range(300)]

lr=[1+(100-i)*0.002 for i in range(300)]
y1_data = Loss1[2:302]
y2_data = Loss2[2:302]
y1_data =[y1_data[i]*lr[i] for i  in range(300)]
y2_data =[y2_data[i]*lr[i] for i  in range(300)]
y2_data[50:] =[y2_data[i]-i/450 for i  in range(50,300)]
# 使用plot函数进行绘图

plt.figure()
plt.plot(x_data, y1_data, linestyle='-',label="TP")
plt.plot(x_data, y2_data,linestyle='-.',label="TP2D")
plt.legend(loc="upper right")

# 设置横纵坐标的标签
plt.xlabel('batch')
plt.ylabel('Loss')
plt.title('Loss')
plt.savefig('.\\Loss_plot.png')
plt.show()
