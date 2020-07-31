# ---------python操作excel----------
#1- 读取用例
#常用的库openpyxl   xlrd    xlwt    xlutils

excelDir = r'/Users/jiying/Downloads/case.xls'
import  xlrd
import  json
workBook = xlrd.open_workbook(excelDir,formatting_info = True)
sheetNames = workBook.sheet_names()
print(sheetNames)

workSheet = workBook.sheet_by_name('课程管理')



#1-- 在缓存里copy一个excel对象--不影响源数据用例
from xlutils.copy import copy
new_workBook =copy(workBook)

#2- 判断测试用例是否通过
if res['retcode'] == '0':
    print('----pass----')
    info = 'pass'
else:
    print('----fail----')
    info = 'fail'

new_workSheet.write()
new_workSheet =new_workBook.get_sheet(1)


new_workBook.save(r'./res.xls')
#2------ 写用例--测试结果--------
