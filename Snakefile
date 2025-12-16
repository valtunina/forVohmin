configfile: "config.yaml"

rule all:
    input:
        "results/top_10_words.txt"

rule download_book:
    output:
        "data/input.txt"
    params:
        url = config["book_url"]
    shell:
        "curl -L {params.url} -o {output}"

rule count_all_words:
    input:
        "data/input.txt"
    output:
        "results/word_counts.tsv"
    script:
        "scripts/count_words.py"

rule get_top_words:
    input:
        "results/word_counts.tsv"
    output:
        "results/top_10_words.txt"
    shell:
        "head -n 11 {input} > {output}"
