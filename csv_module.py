import getpass, openpyxl


def exporter_to_excel(nombre_alias,lista_valores):
    headers       = ['Alias','Defenition']
    workbook_name = nombre_alias+'.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = nombre_alias
    ws.append(headers)
    for row in lista_valores:
        ws.append(row)
    print(f"Output exported to excel in User's home directory under the name {workbook_name}")
    wb.save('/Users/'+getpass.getuser()+'/Documents/'+ workbook_name)