import sys, re
from collections import Counter

def main():
    input_file, output_file = sys.argv[1], sys.argv[2]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = re.findall(r'\b[а-яa-z]+\b', text.lower())
    word_counts = Counter(words)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("word\tcount\n")
        for word, count in word_counts.most_common():
            f.write(f"{word}\t{count}\n")
    
    print(f"Успешно! Подсчитано {len(word_counts)} уникальных слов.")

if __name__ == "__main__":
    main()
