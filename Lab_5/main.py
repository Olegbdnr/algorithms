import time

B = 13
Q = 256


def get_hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result


def search_patterns_in_text(main_text: str, pattern: str) -> int:
    global B, Q
    pattern_len = len(pattern)
    main_text_len = len(main_text)

    multiplier = 1
    for i in range(1, pattern_len):
        multiplier = (multiplier * B) % Q

    pattern_hash = get_hash(pattern)
    main_text_hash = get_hash(main_text[:pattern_len])

    count = 0
    for index_symbol in range(main_text_len - pattern_len + 1):
        if pattern_hash == main_text_hash and main_text[index_symbol: index_symbol + pattern_len] == pattern:
            count += 1

        if index_symbol < main_text_len - pattern_len:
            main_text_hash = ((main_text_hash - ord(main_text[index_symbol]) * multiplier) * B + ord(
                main_text[index_symbol + pattern_len])) % Q

            if main_text_hash < 0:
                main_text_hash += Q
    return count


def worst_case():
    pattern = "mem"
    with open("worstCase.txt", encoding="utf-8") as file_read:
        main_text = file_read.read()
    t0 = time.time()
    count = search_patterns_in_text(main_text, pattern)
    t1 = time.time()
    print(f"Worst case Result: {count}; The running time of the algorithm is equal to: {t1 - t0}")


def average_case():
    pattern = "Rabin"
    with open("averageCase.txt", encoding="utf-8") as file_read:
        main_text = file_read.read()
    t0 = time.time()
    count = search_patterns_in_text(main_text, pattern)
    t1 = time.time()
    print(f"Average case Result: {count}; The running time of the algorithm is equal to: {t1 - t0}")


def best_case():
    pattern = "Pneumonoultramicroscopicsilicovolcanoconiosis"
    with open("bestCase.txt", encoding="utf-8") as file_read:
        main_text = file_read.read()
    t0 = time.time()
    count = search_patterns_in_text(main_text, pattern)
    t1 = time.time()
    print(f"Best case Result: {count}; The running time of the algorithm is equal to: {t1 - t0}")


def main():
    worst_case()
    average_case()
    best_case()


if __name__ == '__main__':
    main()
