def exists_word(word, instance):
    new_dicionary = []
    for file in instance.queue:
        file_name = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        occurrences = [
            {"linha": index + 1}
            for index, line in enumerate(lines)
            if word.lower() in line.lower()
        ]

        if occurrences:
            new_dicionary.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )

    return new_dicionary


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
