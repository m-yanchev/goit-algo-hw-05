from typing import Any, Callable
import pandas as pd
from exec_time import get_time
from kmp import kmp_search
from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search

TEXT_FILES = {
    "стаття 1.txt": "Windows-1251",
    "стаття 2.txt": "utf-8"
}
EXEC_LIST = [
    ("стаття 1.txt", "видати решту суми"),
    ("стаття 1.txt", "являється побудов"),
    ("стаття 2.txt", "являється побудов"),
    ("стаття 2.txt", "видати решту суми")
]
ALGORITHMS: dict[str, tuple[str, Callable[[str, str], int]]] = {
    "KMP": ("kmp", kmp_search),
    "Boyer-Moore": ("boyer_moore", boyer_moore_search),
    "Rabin-Karp": ("rabin_karp", rabin_karp_search)
}


def main() -> None:
    table_index: list[tuple[str, str, str]] = []
    table_dict: dict[str, list[Any]] = {
        "time": [],
        "result": []
    }

    for filename, pattern in EXEC_LIST:
        with open(filename, "r", encoding=TEXT_FILES[filename]) as file:
            text = file.read()

        for algo_name, (module_name, algorithm) in ALGORITHMS.items():
            time = get_time(algorithm.__name__, (text, pattern), module_name)
            result = algorithm(text, pattern)

            table_dict["time"].append(time)            
            table_dict["result"].append(result)
            table_index.append((filename, pattern, algo_name))
            
    index = pd.MultiIndex.from_tuples(table_index, names=["filename", "pattern", "algorithm"])
    table = pd.DataFrame(table_dict, index=index)
    print(table)

if __name__ == "__main__":
    main()

