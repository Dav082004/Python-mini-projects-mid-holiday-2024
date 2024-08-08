import pandas as pd

# Create a DataFrame with sample data
datos = pd.DataFrame({
    'Columna 1': [1, 2, 3],
    'Columna 2': [4, 5, 6]
})

# Create an Excel writer object
excel_writer = pd.ExcelWriter('report.xlsx')

# Write the DataFrame to an Excel file
datos.to_excel(excel_writer, sheet_name='Hoja1')

# Save the Excel file
excel_writer._save()

# Print confirmation message
print('Reporte generado.')
