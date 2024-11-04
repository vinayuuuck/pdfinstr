import pypdf
import sys
import os


def main():
    if len(sys.argv) != 2:
        raise Exception("Incorrect usage")
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise Exception("File does not exist")

    reader = pypdf.PdfReader(filename)

    for i in range(len(reader.pages)):
        print(reader.pages[i].extract_text())


if __name__ == "__main__":
    main()
