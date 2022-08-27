import typer
import os
import re

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


def Find_Alias(alias):
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
                
                aliases.append(m.group())
    return aliases

@app.command()
def listFiles():
    #command that shows the file under a specific path
    lista = list_of_files()
    print("lista de archivos en /Users/osaeljm/Documents/Cosas")
    print(type(lista))
    for i in lista:
        print(i)

@app.command()
def find_alias(alias: str):
    #function that shows the out put for command/user/hoist alias.
    archivo = Find_Alias(alias)
    for arch in archivo:
        print(arch)

if __name__ == "__main__":
    app()