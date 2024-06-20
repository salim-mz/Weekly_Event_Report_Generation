import pandas as pd
from openpyxl import Workbook

def generate_report():
    # Load processed data
    df = pd.read_csv('data/processed_data.csv')

    # Create a new Excel workbook and sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Weekly Event Report"

    # Write data to Excel sheet
    for r, row in enumerate(dataframe_to_rows(df, index=False, header=True), 1):
        for c, cell_value in enumerate(row, 1):
            ws.cell(row=r, column=c, value=cell_value)

    # Save the workbook
    wb.save('reports/weekly_event_report.xlsx')

if __name__ == "__main__":
    generate_report()
