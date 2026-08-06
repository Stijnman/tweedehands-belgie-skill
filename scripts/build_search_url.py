#!/usr/bin/env python3
from urllib.parse import quote_plus

def build_2dehands(query: str) -> str:
    return f"https://www.2dehands.be/q/{quote_plus(query.strip())}/"

def build_vinted(query: str, price_to: int | None = None, order: str = "relevance") -> str:
    url = f"https://www.vinted.be/catalog?search_text={quote_plus(query.strip())}&order={order}"
    if price_to:
        url += f"&price_to={price_to}"
    return url

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "test"
    print(build_2dehands(q))
    print(build_vinted(q))
