import os

TEXT = 'This is my resignation — effective immediately, my enthusiasm has already left the building and taken the good pens.'

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
