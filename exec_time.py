from timeit import timeit
from typing import Any


def get_time(func: str,
             args: Any,
             module: str | None = None,
             number: int = 100) -> float:
    setup_str = f"from {module} import {func}" if module else ""
    all_time = timeit(f"{func}(*{args})", setup=setup_str, number=number)
    return all_time / number
