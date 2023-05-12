# Usage:
# test_obfuscated.py target.exe "Hello World"
# returns exit code 0 if obfuscated, 1 if not

import sys

def test_obfuscated(path, string):
    with open(path, 'rb') as f:
        contents = f.read()
        return (contents.find(string.encode()) == -1)

if __name__ == "__main__":
    path = sys.argv[1]
    string = sys.argv[2]
    if (test_obfuscated(path, string)):
        print(f'SUCCESS - string \"{string}\" is obfuscated')
        sys.exit(0)
    else:
        print(f'FAILURE - string \"{string}\" is not obfuscated')
        sys.exit(1)