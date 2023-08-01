
filename="压力测试数据.txt"

def pre_deal(file):
    with open(file) as f:
        all=f.readlines()
        for i,line in enumerate(all):
            line=line.split(" ")
            print("new data",i)
            for index, value in enumerate(line):
                index=index+1
                if index >0 and index%9==0:
                    print(value)
                else:
                    print(cal_press(int(value,16)),end=" ")
def cal_press(x):
    return 22633.04*((3.3*255-3.3*x)/(330*x))**1.11

# with open(filename,'r') as file:
#     lines=file.readlines()
#     for line in lines:
#        if len(line)==27:
#            data_list=line.split(" ")[:-1]
#            voltage=list(map(lambda x:int(x.replace('O','0'),16),data_list))
#            press=list(map(cal_press,voltage))
#            print(press)


pre_deal(filename)