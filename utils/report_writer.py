import pandas as pd
from openpyxl import Workbook

def write_report_to_excel(dataframe, filepath):
    wb = Workbook()
    ws = wb.active
    ws.title = "Weekly Event Report"

    for r, row in enumerate(dataframe_to_rows(dataframe, index=False, header=True), 1):
        for c, cell_value in enumerate(row, 1):
            ws.cell(row=r, column=c, value=cell_value)

    wb.save(filepath)
