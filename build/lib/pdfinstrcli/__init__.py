import pypdf
import sys
import os


def main(filename):
    if not os.path.exists(filename):
        raise Exception("File does not exist")

    reader = pypdf.PdfReader(filename)

    for i in range(len(reader.pages)):
        print(reader.pages[i].extract_text())


if __name__ == "__main__":
    n = len(sys.argv)
    if n != 2:
        print("Error: Invalid number of Arguments.")
        print("Usage: python3 pdfinstr <pdftoread>")
        exit()
    main(sys.argv[1])
