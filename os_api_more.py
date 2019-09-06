import os
def main():
    print(os.getcwd())
    print(os.listdir())
    os.chdir('c:/itay')
    print(os.getcwd())
    try:
        os.mkdir('new1/new2')
    except Exception as e:
        print("-----------------")
        print("ERROR creating folders")
        print(e)
        print("-----------------")
    os.makedirs('new1/new2')
    #os.rmdir()
    import shutil
    shutil.rmtree('new1')
    #os.rename('goodybye.txt','hello.txt')
    #os.rename('hello.txt','goodybye.txt')
    print(os.path.splitext('goodybye.txt'))
    #shutil.copytree()
    print(os.stat("goodybye.txt").st_size)
    mod_time = os.stat("goodybye.txt").st_mtime
    from datetime import datetime
    print(datetime.now())
    print(f'Modification time: {datetime.fromtimestamp(mod_time)}')

    # print
    '''
    for dirpath, dirnames, filenames in os.walk(r'c:\itay'):
        print(f'-------{dirpath}')
        for folder in dirnames:
            print(f'[{folder}]')
        for file1 in filenames:
            print(file1)
    '''

    # targil 1: input a file name:
    # print the location of the file and exit
    # targil 2: input an extenstion (*.txt)
    # print all files with this extension
    # targl 3: find the biggest file in the tree

    # 1
    search_for = 'test.data.db'
    for dirpath, dirnames, filenames in os.walk(r'c:\itay'):
        if search_for in filenames:
            print(dirpath)


    # 2
    search_for_ext = '.db'
    for dirpath, dirnames, filenames in os.walk(r'c:\itay'):
        for one_file in filenames:
            if os.path.splitext(one_file)[1] ==\
                    search_for_ext:
                print(one_file)

    #[{'a': 0}, {'b':0}, {'c':0}]

    # 3 - biggest
    max = -1
    file_max_name = 'not found...'
    for dirpath, dirnames, filenames in os.walk(r'c:\itay'):
        for one_file in filenames:
            size_of_file = \
                os.stat(os.path.join(dirpath, one_file)).st_size
            if size_of_file > max:
                max = size_of_file
                file_max_name = one_file
    print(f'Biggest file : {file_max_name} [{max}]')

    # danger!
    # os.environ["PATH"] = ""
    #print(os.getenv("OS"))

    os.startfile(r'c:\windows\System32\notepad.exe')
    # input("hey:")
    print("----------------------")

    import psutil # install frmo Settings
    for proc in  psutil.process_iter():
        if proc.name() == "notepad.exe":
            print("found...")
            proc.kill()

    import stat
    fileAttr = os.stat('hello.txt')
    # stat.S_IREAD -- read only
    #os.chmod('hello.txt', stat.S_IREAD)
    # stat.S_IWRITE -- read and write
    #os.chmod('hello.txt', stat.S_IWRITE)

    print(os.path.isfile('hello.txt'))
    print(os.path.isdir('hello.txt'))
    print(os.path.exists('hello.txt'))

main()

# targil
# targil 1 - find biggest
#            find files with ext
# process - display all processed

# myosapi.py
# Myapi
# - findbiggest(root)
# - findextfiles(root)
# - display all process
# Main
# import myosapi
# execute 3 methods
