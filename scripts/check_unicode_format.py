#!/usr/bin/env python3
import argparse
import os
import re
import sys
import unicodedata

RED = "\033[31m"
RESET = "\033[0m"


def check_build_time(s: str) -> bool:
    """The first two spaces are permitted; any subsequent spaces and all formatting characters (Cf)/other whitespace are highlighted in red"""
    warn = False
    out = []
    space_count = 0
    for c in s:
        if c == " ":
            space_count += 1
            if space_count <= 2:
                out.append(f"U+{ord(c):04X} ")
            else:
                warn = True
                out.append(f"{RED}U+{ord(c):04X}{RESET} ")
            continue
        else:
            space_count = 0

        if unicodedata.category(c) == "Cf" or (c.isspace() and c != " "):
            warn = True
            out.append(f"{RED}U+{ord(c):04X}{RESET} ")
        else:
            out.append(f"U+{ord(c):04X} ")

    print("".join(out))
    if warn:
        print("::warning title=BUILD_TIME Error::A call to a custom build time exception symbol has been detected. Please take note!")
    return warn


def check_suffix(s: str) -> bool:
    warn = False
    out = []
    for c in s:
        if c.isspace() or unicodedata.category(c) == "Cf":
            warn = True
            out.append(f"{RED}U+{ord(c):04X}{RESET} ")
        else:
            out.append(f"U+{ord(c):04X} ")

    print("".join(out))
    if warn:
        print("::warning title=SUFFIX Error::An abnormal symbol call with a custom kernel suffix has been detected. Please be aware!")

    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}|-?android\d{2,3}-", s):
        print("::warning title=SUFFIX Format Error::Please note that duplicate or redundant content calls have been detected in the custom kernel suffix!")
        warn = True

    return warn


def main() -> int:
    parser = argparse.ArgumentParser(description="Unicode / Format Anomaly Detection")
    parser.add_argument("--mode", choices=["build_time", "suffix"], required=True)
    args = parser.parse_args()

    text = os.environ.get("CHECK_TEXT", "")

    if args.mode == "build_time":
        warn = check_build_time(text)
    else:
        warn = check_suffix(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
