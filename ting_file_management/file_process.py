import sys

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
    try:
        my_data = instance.search(position)
        print(my_data)
    except IndexError:
        sys.stderr.write("Posição inválida")
