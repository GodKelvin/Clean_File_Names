from pathlib import Path
import os
from xxlimited import new

def create_dir(path_dir):
    path = Path(path_dir)
    path.mkdir(exist_ok=True)

def clean_files(path_dir, output_dir, trash):
    create_dir(output_dir)
    files = os.listdir(path_dir)
    
    for file in files:
        without_trash = file.lower().split(trash)
        print(without_trash)
        new_name_and_move = output_dir + "".join(without_trash)

        if(os.path.isfile(new_name_and_move)):
            print("Arquivo ja existe")
        else:
            os.rename(path_dir+file, new_name_and_move)


def main():
    input_dir = "test/"
    output_dir = "output/"
    remove_from_file = "arquivo"
    clean_files(input_dir, output_dir, remove_from_file)

main()




    