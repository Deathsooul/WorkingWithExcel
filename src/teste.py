import openpyxl
from pathlib import Path

xlsx_file = Path('/home/wallace/Documents/WallaceDocs/WorkingWithExcel/src', 'Simulador_Site_v2.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)

BASEGERACAO = wb_obj['BaseGeracao']
SIMULADOR = wb_obj['Simulador_Site']

print(BASEGERACAO['E12'].value)
print(SIMULADOR['E14'].value)
print(SIMULADOR['I13'].value)
