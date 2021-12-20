import pandas as pd
from openpyxl import load_workbook

'''
pandas读取excel
'''
def read_excel_by_pandas(path):
    df = pd.read_excel(path)  # pandas读取出来的格式是DataFrame
    print(df)
    # 3.读取excel的某一个sheet
    df = pd.read_excel(path, sheet_name='Sheet1')  # 读取指定sheet
    print(df)
    # 4.获取列标题
    print(df.columns)
    # 5.获取列行标题
    print(df.index)
    # 6.制定打印某一列
    print(df["姓名"])
    # 7.描述数据
    print(df.describe())
    return df

'''
openpyxl读取excel
'''
def read_excel_by_openpyxl(path):
    # 1.打开 Excel 表格并获取表格名称
    workbook = load_workbook(filename=path)  # 只支持.xlsx格式
    print(workbook.sheetnames)
    # 2.通过 sheet 名称获取表格
    sheet = workbook["Sheet1"]
    print(sheet)
    # 3.获取表格的尺寸大小(几行几列数据) 这里所说的尺寸大小，指的是 excel 表格中的数据有几行几列，针对的是不同的 sheet 而言。
    print(sheet.dimensions)
    # 4.获取表格内某个格子的数据
    # 1 sheet["A1"]方式
    cell1 = sheet["B2"]  # 按列名获取
    cell2 = sheet["C11"]
    print(cell1.value, cell2.value)
    """
    workbook.active 打开激活的表格; sheet["A1"] 获取 A1 格子的数据; cell.value 获取格子中的值;
    """
    # 4.2sheet.cell(row=, column=)方式
    cell1 = sheet.cell(row=1, column=1)
    cell2 = sheet.cell(row=11, column=3)
    print(cell1.value, cell2.value)

    # 5. 获取一系列格子
    # 获取 A1:C2 区域的值
    cell = sheet["A1:C2"]
    print(cell)
    for i in cell:
        for j in i:
            print(j.value)

def read_txt_all(path):
    with open(path,"r",encoding="utf-8") as file:
        data=file.read() #读取所有
    print(data)
    return data

def read_txt_to_list(path):
    res_list=[]
    with open(path, "r") as file:
        for line in file.readlines():
            line.strip("\n").split('\t')  # 去掉列表中每一个元素的换行符
            print(line)


if __name__=="__main__":
    path="../data/read_file_test/"
    file_name="number_test.txt"
    read_txt_to_list(path+file_name)
    excel_name="test_excel.xlsx"
    read_excel_by_pandas(path+excel_name)
    read_excel_by_openpyxl(path+excel_name)