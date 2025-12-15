#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("No command provided")
        return

    command = sys.argv[1]
    print(f"Command: {command}")

if __name__ == "__main__":
    main()
