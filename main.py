import os
import sys


def create_md_link(programming_lang_name: str, filename: str):
    return f"\n## [{programming_lang_name}]({'https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/' + filename})\n\n"


langs = [
    ("Basic", ".bas"),
    ("Batch", ".bat"),
    ("C#", ".cs"),
    ("Go", ".go"),
    ("Java", ".java"),
    ("JavaScript", ".js"),
    ("Lua", ".lua"),
    ("Perl", ".pl"),
    ("Powershell", ".ps1"),
    ("Python", ".py"),
    ("Ruby", ".rb"),
    ("Rust", ".rs"),
    ("Bash", ".sh"),
    ("TypeScript", ".ts"),
]
if __name__ == "__main__":
    with open("./README.md", mode="w+") as README:
        os.chdir("./src/fibonacci")
        README.write(
            """
# What is This?
The objective of this repository is to write a fibonacci sequence generator in many languages.

# Completed
            """
        )
        for file in os.listdir(os.getcwd()):
            file_ext = os.path.splitext(file)[1]
            lang_name = [name for name, ext in langs if ext == file_ext]
            lang_name = str(lang_name)[2:-2]
            README.write(create_md_link(lang_name, file))
            with open(file) as f:
                for line in f.readlines():
                    README.write("\t" + line)
            README.write("\n")
