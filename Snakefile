# Определяем правило по умолчанию, которое запустится если просто набрать "snakemake"
rule all:
    input:
        "results/top_10_words.txt"

# Правило 1: Скачать книгу из интернета
rule download_book:
    output:
        "data/input.txt"
    params:
        url = config["book_url"]
    shell:
        # Команда curl скачивает файл по ссылке. Флаг -L позволяет следовать перенаправлениям.
        "curl -L {params.url} -o {output}"

# Правило 2: Подсчитать частоту всех слов и сохранить полную таблицу
rule count_all_words:
    input:
        "data/input.txt"
    output:
        "results/word_counts.tsv"
    script:
        "scripts/count_words.py"

# Правило 3: Извлечь топ-10 слов из полной таблицы
rule get_top_words:
    input:
        "results/word_counts.tsv"
    output:
        "results/top_10_words.txt"
    shell:
        # Команда head берет первые 10 строк файла (заголовок + 9 слов)
        "head -n 11 {input} > {output}"