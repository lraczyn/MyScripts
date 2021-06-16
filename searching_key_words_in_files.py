from os import listdir
from os.path import isfile, join
from contextlib import ExitStack

def select_files(*arg, path):
    """[Function let us find selected files in given path]

    Args:
        path ([Sting]): [Path to search]

    Returns:
        [List]: [List with selected files]
    """
        files = []
        path_files = [f'{path}\{f}' for f in listdir(path)
                   if isfile(join(path, f))]
        for select in [*arg]:
            for f_name in path_files:
                if select in f_name:
                    files.append(f_name)
        return files

def create_output(path, select, key_words):
    """[Function let us find key_words in chosen files in selected path]

    Args:
        path ([String]): [description]
        select ([List]): [description]
        key_words ([List]): [description]
    """

    
    f_names = select_files(*select, path=path)
    
    # saving to one file

    path = path
    with ExitStack() as stack:
        files = [stack.enter_context(open(f, encoding='UTF-8'), )
                for f in f_names]
        with open('output/'+path[-15:], 'a', encoding='UTF-8') as f:
            for file in files:
                print(file.name)



                # room switching & error state
                if 'scanning' in file.name:
                    while True:
                        try:
                            line = next(file)
                            if 'Switching' in line:
                                f.write(line)
                            if 'Error' in line:
                                f.write(line)  
                        except StopIteration:
                            break

                # taking data from radiation
                if 'access' in file.name:
                    while True:
                        try:
                            line = next(file)
                            if 'spot positions' in line:
                                f.write(line)
                        except StopIteration:
                            break
