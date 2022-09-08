import openpyxl


def exporter_to_excel(nombre_alias,lista_valores):
    #function that takes an alias name(str) and list of list) and creates an excel file based on the alias
    headers       = ['Alias','Defenition']
    workbook_name = nombre_alias+'.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = nombre_alias
    ws.append(headers)
    for row in lista_valores:
        ws.append(row)
    wb.save(filename=workbook_name)