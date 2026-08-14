import argparse
import tarfile
import pathlib


def archive(src, dest):
    src = pathlib.Path(src)
    with tarfile.open(dest, "w:gz") as tar:
        tar.add(src, arcname=src.name)
    return dest


def main():
    p = argparse.ArgumentParser(prog="dataset_archiver")
    p.add_argument("--input", required=True)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    print(archive(a.input, a.out))


if __name__ == "__main__":
    main()
