# Snakemake Workflow для анализа текста

Этот проект автоматизирует скачивание текста и анализ частоты слов.

## Как запустить
1. Установите Snakemake: `pip install snakemake`
2. Запустите workflow: `snakemake --cores 1`
3. Проверьте результат: `cat results/top_10_words.txt`

## Ожидаемый результат
Файл `results/top_10_words.txt` с топ-10 слов из книги.
