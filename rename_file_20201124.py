# 将文件改成文件名+当前日期
# 获得当前日期，并转化为YYYYMMDD的字符串
from datetime import datetime
import os.path as op
import os
current_time=datetime.now()

# 获得自己想要的日期形式
Year_month_day = str(current_time.year)+str(current_time.month)+str(current_time.day)

# 读取文件名：获得文件路径，和文件名字
file_name = op.basename("D://ex//农产品供求交易服务平台暂停服务公告.docx")
print('原文件名称：', file_name)

# 文件名+字符串
new_file_name=file_name.replace('.',f'{Year_month_day}.')

print('新文件名称：',new_file_name)

# 将原文件名替换为新的文件名
os.rename(file_name, new_file_name)




