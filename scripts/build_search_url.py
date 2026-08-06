#!/usr/bin/env python3
from urllib.parse import quote_plus

def build_2dehands(query: str) -> str:
    return f"https://www.2dehands.be/q/{quote_plus(query.strip())}/"

if __name__ == "__main__":
    import sys
    print(build_2dehands(sys.argv[1] if len(sys.argv) > 1 else "test"))
