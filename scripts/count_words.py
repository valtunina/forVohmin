import sys
import re
from collections import Counter

def main():
    # Получаем имена файлов из аргументов командной строки, которые передаст Snakemake
    input_file = sys.argv[1]  # "data/input.txt"
    output_file = sys.argv[2] # "results/word_counts.tsv"

    # Читаем текст книги
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Очищаем текст: оставляем только буквы и пробелы, приводим к нижнему регистру
    words = re.findall(r'\b[а-яa-z]+\b', text.lower())

    # Подсчитываем частоту каждого слова
    word_counts = Counter(words)

    # Сортируем слова по частоте (по убыванию)
    sorted_counts = word_counts.most_common()

    # Сохраняем результат в файл (TSV - tab-separated values)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("word\tcount\n")  # Заголовок столбцов
        for word, count in sorted_counts:
            f.write(f"{word}\t{count}\n")

    print(f"Успешно! Подсчитано {len(sorted_counts)} уникальных слов. Результат в {output_file}")

if __name__ == "__main__":
    main()