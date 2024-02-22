import toml

from pycodedoc.docgen import DocGen


def write_toml(content, path):
    with open(path, "w") as f:
        toml.dump(content, f)


def main():
    docgen = DocGen()
    write_toml(docgen.prompts, "prompts.toml")


if __name__ == "__main__":
    main()
