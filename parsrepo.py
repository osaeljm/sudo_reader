import typer, os, re, csv_module, rich_module

app = typer.Typer()


def list_of_files():
    #function that retrives list of file under specific path in list format
    listFiles = []
    for dirpath, dirnams,filename in os.walk('/Users/osaeljm/Documents/Cosas'):
        #print("Current path: ", dirpath)
        #print('Directories: ', dirnams)
        #print("file names: ", filename)
        listFiles.append(filename)
    return listFiles


def Finder(alias):
    #funtions that retrieves aliases on list format
    aliases = []
    if alias == 'User_Alias':
        pattern = re.compile(r'(?<=User_Alias).*$')
    elif alias == 'Host_Alias':
        pattern = re.compile(r'(?<=Host_Alias).*$')
    else:
        pattern = re.compile(r'(?<=Cmnd_Alias).*$')
    
    with open('test_sudo_file','r') as file:
        content = file.readlines()
    
        for line in content:
            matches = pattern.finditer(line)
            for m in matches:
                aliases.append(m.group().split('='))
    return aliases

@app.command()
def listFiles():
    '''Command that shows the file under a /Users/osaeljm/Documents/Cosas'''
    lista = list_of_files()
    print("lista de archivos en /Users/osaeljm/Documents/Cosas")
    print(type(lista))
    for i in lista:
        print(i)

@app.command()
def find_alias(alias: str):
    '''Command that shows the out put for command/user/host alias and export the out come to an excel file.'''
    archivo = Finder(alias)
    rich_module.print_Table(archivo,alias)
    csv_module.exporter_to_excel(alias, archivo)

@app.command()
def find_single_rules():
    '''Command that show all single rules. '''
    pass
  
if __name__ == "__main__":
    app()