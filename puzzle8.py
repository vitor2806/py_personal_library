# -*- coding: utf-8 -*- 
def searchFile(name):
    archive = open(name)
    return archive

    
choice = 0

while choice != 3:
    try:
        choice = int(input('\nChoose an option\n1 - Search file\n2 - Read file content\n3 - Leave\nChoice: '))
        match choice:
            case 1:
                file_name = input('Insert file name: ')
                archive = searchFile(file_name)
                print('Your file: ', archive)

            case 2:
                archive_content = archive.read()
                print('File content:')
                print(archive_content)

            case 3:
                print('Leaving...')
    except:
        print('\nInvalid option. Try again: \n')
