# weekReportExcel.py
# 读取Excel中数字
# 参考[PYTHON如何读取和写入EXCEL里面的数据_python_脚本之家](https://www.jb51.net/article/172932.htm)

import xlrd

# 打开excel
x1 = xlrd.open_workbook("肉菜运维周报图表追溯数据（0928）.xlsx")

# 通过索引获取工作表

table = x1.sheets()[0]

# 获取单元格的值,索引从0开始

data = int(table.cell(1,8).value)
print(data)



