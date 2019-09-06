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
    os.rename('goodybye.txt','hello.txt')
    os.rename('hello.txt','goodybye.txt')
    print(os.stat("goodybye.txt").st_size)
    mod_time = os.stat("goodybye.txt").st_mtime
    from datetime import datetime
    print(datetime.now())
    print(f'Modification time: {datetime.fromtimestamp(mod_time)}')

    for dirpath, dirnames, filenames in os.walk(r'c:\itay'):
        print(f'-------{dirpath}')
        for folder in dirnames:
            print(f'[{folder}]')
        for file1 in filenames:
            print(file1)

    # targil 1: input a file name:
    # print the location of the file and exit
    # targil 2: inpurt an extenstion (*.txt)
    # print all files with this extension
    # targl 3: find the biggest file in the tree


main()
