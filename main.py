import os


def create_md_link(programming_lang_name: str, filename: str):
    return f"\n## [{programming_lang_name}]({'https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/' + filename})\n\n"


langs = [
    ("Basic", ".bas"),
    ("Batch", ".bat"),
    ("Bash", ".sh"),
    ("Powershell", ".ps1"),
    ("Lua", ".lua"),
    ("Perl", ".pl"),
    ("Ruby", ".rb"),
    ("Python", ".py"),
    ("JavaScript", ".js"),
    ("TypeScript", ".ts"),
    ("Go", ".go"),
    ("C#", ".cs"),
    ("Java", ".java"),
    ("Rust", ".rs"),
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
        for lang in langs:
            lang_name = lang[0]
            file_name = "fib-gen" + lang[1]
            file_path = os.getcwd() + "\\" + file_name
            README.write(create_md_link(lang_name, file_name))
            with open(file_path) as f:
                for line in f.readlines():
                    README.write("\t" + line)
            README.write("\n")
