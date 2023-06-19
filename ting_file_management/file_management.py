import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")
    # if os.path.exists(path_file):
    #     sys.stderr.write(f"Arquivo {path_file} não encontrado")
    try:
        with open(path_file, "r") as file:
            lines = file.read().splitlines()
        return lines
    except FileNotFoundError:
        print(sys.stderr.write(f"Arquivo {path_file} não encontrado\n"))
