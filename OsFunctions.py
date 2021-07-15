import os
from pathlib import Path
def foldercheck():
    username = os.getlogin()
    print(username)
    default_osu_directory = os.path.join( r'C:\Users', str(username), 'AppData\Local\osu!\Skins')
    print(default_osu_directory)
    return default_osu_directory
    
def skinlist():
    skinlist = next(os.walk(foldercheck()))[1]
    print(foldercheck())
    print(list(skinlist))
    return list(skinlist)
 
skinlist()  