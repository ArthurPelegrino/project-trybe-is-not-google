# def txt_importer(path_file):
#     if not path_file.endswith(".txt"):
#         sys.stderr.write("Formato inválido")
#     # if os.path.exists(path_file):
#     #     sys.stderr.write(f"Arquivo {path_file} não encontrado")
#     try:
#         with open(path_file, "r") as file:
#             lines = file.read().splitlines()
#         return lines
#     except FileNotFoundError:
#         print(sys.stderr.write(f"Arquivo {path_file} não encontrado\n"))


# vou receber um objeto instanciado de queue e um caminho

# teste = Queue()
# teste.enqueue(2)
# teste.enqueue(4)
# teste.queue == [2, 4]

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    resolved_file = txt_importer(path_file)
    file_name = path_file
    new_dictionary = {}
    for d in instance.queue:
        if d["nome_do_arquivo"] == file_name:
            return "File already registered"
    with open(path_file, "r") as file:
        number_of_lines = len(file.readlines())
        new_dictionary["nome_do_arquivo"] = file_name
        new_dictionary["qtd_linhas"] = number_of_lines
        new_dictionary["linhas_do_arquivo"] = resolved_file
        instance.enqueue(new_dictionary)
        print(new_dictionary)
        return new_dictionary


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
