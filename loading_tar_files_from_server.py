from os.path import isfile, join
from contextlib import redirect_stdout
from datetime import datetime
from os import listdir
from tqdm.notebook import tqdm
import colorama
import tarfile
import os
import re


def unpacking_tar_files(path, extraction_path):
    """[Script lets us auto-unpacking tar files located in selected path.
        Progress is displayed by tqmd]

    Args:
        path ([String]): [Location of tar files]
        extraction_path ([String]): [target destination]
    """
    files_paths = [f'{path}\{f}' for f in listdir(path)
                if isfile(join(path, f))]

    for file_path in tqdm(files_paths):
        # Opening tar file
        try:
            tar = tarfile.open(file_path)
            tar.extractall(path=extraxtion_path)
        except:
            tar.close()
            time = datetime.utcnow()
            log = f'corrupted file: {file_path}'
            with open('logs.txt', mode='a') as f:
                print(time,': ', log, file=f)
            print(log)
            continue
                    
        # Creating new folder if doesn't exist
        try:
            output_data = extraxtion_path+'\\'+re.findall('\d{8}-OUTPUT', file_path)[0]
            os.mkdir(output_data)
        except FileExistsError as e:
            print(colorama.Fore.RED, e, flush=False)
            continue
        
        # Saving log
        try:
            file = path+'\\'+listdir(path)[0]
            tar = tarfile.open(file)
            tar.extractall(path=output_data)
            tar.close()
            os.remove(file)
            print(colorama.Fore.GREEN + file_path[-22:]+' ->   successfully extracted', flush=false, end='\r')
        except:
            tar.close()
            time = datetime.utcnow()
            log = f'corrupted file: {file_path}'
            with open('logs.txt', mode='a') as f:
                print(time,': ', log, file=f)
            continue
    print(colorama.Fore.GREEN + 'DONE !!!', flush=False)
