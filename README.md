# Snakemake Workflow для анализа текста

## 📍 Репозиторий
https://github.com/valtunina/forVohmin

## 📋 Описание проекта
Этот проект автоматически скачивает книгу "Война и мир" с Project Gutenberg и анализирует частоту слов с использованием Snakemake workflow.

## 🚀 Как запустить проект

### Вариант 1: GitHub Codespaces (онлайн)
1. Откройте репозиторий на GitHub: https://github.com/valtunina/forVohmin
2. Нажмите клавишу `.` (точка) на клавиатуре
3. В открывшемся терминале выполните:
   pip install snakemake
   snakemake --cores 1
###Вариант 2: Через Docker
git clone https://github.com/valtunina/forVohmin.git
cd forVohmin
docker run --rm -v "$(pwd):/work" -w /work snakemake/snakemake snakemake --cores 1
###Вариант 3: Локально с установленным Snakemake
git clone https://github.com/valtunina/forVohmin.git
cd forVohmin
pip install snakemake
snakemake --cores 1

📊 Что делает workflow
download_book - Скачивает книгу "Война и мир" с Project Gutenberg
count_all_words - Анализирует текст, подсчитывает частоту всех слов
get_top_words - Извлекает топ-10 самых частых слов

✅ Ожидаемый результат
После успешного выполнения в папке results/ будут созданы:
results/word_counts.tsv
Полная таблица частот всех слов
results/top_10_words.txt
Топ-10 самых частых слов из книги:

text
word    count
the     34737
and     22302
to      16759
of      15013
a       10583
he      10007
in      9039
that    8205
his     7984
was     7365
