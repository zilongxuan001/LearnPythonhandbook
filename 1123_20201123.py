# 批量修改目录下文件名称
# 输入：子目录下文件
# 输出：文件名称修改为所有文件+创建时间

import os,time
from datetime import datetime

path=input('请输入文件路径(结尾加上/)：')       

# 获取该目录下所有文件名称，以字符串形式存入列表中
fileList=os.listdir(path)

n=0
for i in fileList:
    
    # 设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + i  # os.sep添加系统分隔符\\

    # 获取该文件的创建时间，形成字符串形式
    t=time.gmtime(os.path.getctime(path + os.sep + i))
    creat_time=str(time.strftime("%Y%m%d",t))
    
    # 设置新文件名，如果文件名带后缀，则日期插在后缀前面，如果没有后缀，则日期直接放在最后
    if '.' in i:
        newname= path + os.sep + i.replace('.',f'_{creat_time}.')
    else:
        newname= path + os.sep + i+ '_'+ creat_time
    
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)

    

