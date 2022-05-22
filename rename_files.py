from pathlib import Path
import os
import sys
import shutil

def create_dir(path_dir):
    path = Path(path_dir)
    path.mkdir(exist_ok=True)

def clean_files(path_dir, output_dir, trash):
    create_dir(output_dir)
    files = os.listdir(path_dir)

    for file in files:
        src_file = path_dir+file
        without_trash = file.lower().split(trash)
        new_name_and_move = output_dir + "".join(without_trash)

        if(os.path.isfile(new_name_and_move)):
            print("> Arquivo ja existe -> %s" %new_name_and_move)
        else:
            shutil.copyfile(src_file, new_name_and_move)


def main():
    if(len(sys.argv) < 4):
        print("-->> ERROR: Parametros de entrada pendentes")
        return 
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    remove_from_file = sys.argv[3]
    clean_files(input_dir, output_dir, remove_from_file)
    print("# Concluido com sucesso.\n# Verificar pasta de destino: %s" %output_dir)

main()