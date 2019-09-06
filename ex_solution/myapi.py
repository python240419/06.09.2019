import os

class os_fun():
    def search_ext(self, path, search_for_ext):
        for dirpath, dirnames, filenames in os.walk(r'c:\itay'):
            for one_file in filenames:
                if os.path.splitext(one_file)[1] ==\
                        search_for_ext:
                    print(one_file)

    def find_max(self, path):
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
        return file_max_name

    def print_processes(self):
        import psutil # install frmo Settings
        for proc in  psutil.process_iter():
            print(proc.name())
