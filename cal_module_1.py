import win32com.client as win32
import pythoncom
from time import sleep

pythoncom.CoInitialize()
xl = win32.gencache.EnsureDispatch('Excel.Application')
xl.Visible = True
wb = xl.Workbooks.Open(Filename=r"C:\example\workbook.xlsx")
ws = wb.Worksheets('AutoCAL')
