#!/usr/bin/env python3
"""
Скрипт для подсчета слов. Работает с Snakemake.
Snakemake передает объект через глобальную переменную 'snakemake'.
"""

import re
from collections import Counter
import os
import sys

def count_words_snakemake():
    """Версия для Snakemake"""
    try:
        # Snakemake передает объект через глобальную переменную
        # Используем globals() чтобы получить его
        smk = globals().get('snakemake')
        
        if smk is None:
            print("❌ Ошибка: объект snakemake не найден")
            return False
        
        input_file = smk.input[0]
        output_file = smk.output[0]
        
        print(f"🔧 Snakemake: {input_file} -> {output_file}")
        
        return process_file(input_file, output_file)
        
    except Exception as e:
        print(f"❌ Ошибка Snakemake: {e}")
        return False

def count_words_manual():
    """Версия для ручного запуска"""
    if len(sys.argv) != 3:
        print("📖 Использование: python count_words.py ВХОД ВЫХОД")
        print(f"   Получено аргументов: {len(sys.argv) - 1}")
        return False
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print(f"🔧 Ручной запуск: {input_file} -> {output_file}")
    
    return process_file(input_file, output_file)

def process_file(input_file, output_file):
    """Обработка файла"""
    try:
        # Проверяем файл
        if not os.path.exists(input_file):
            print(f"❌ Файл не найден: {input_file}")
            return False
        
        # Читаем
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        print(f"📄 Размер: {len(text):,} символов")
        
        # Находим слова
        words = re.findall(r'[a-zA-Z]+', text.lower())
        print(f"📊 Всего слов: {len(words):,}")
        
        # Считаем
        counts = Counter(words)
        print(f"🔢 Уникальных слов: {len(counts):,}")
        
        # Создаем папку
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Сохраняем
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("word\tcount\n")
            for word, count in counts.most_common():
                f.write(f"{word}\t{count}\n")
        
        print(f"✅ Результат: {output_file}")
        
        # Топ-5
        print("\n🏆 Топ-5 слов:")
        for i, (word, count) in enumerate(counts.most_common(5), 1):
            print(f"{i}. {word}: {count:,}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка обработки: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Главная функция"""
    # Проверяем запущены ли мы из Snakemake
    if 'snakemake' in globals():
        print("�� Запуск из Snakemake")
        success = count_words_snakemake()
    else:
        print("🎯 Ручной запуск")
        success = count_words_manual()
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
