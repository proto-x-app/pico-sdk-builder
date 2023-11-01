#!/usr/bin/env python3

import os
import shutil
import hashlib
import datetime
import platform

def simple_md_to_html(md_text, css_path):
    html_text = f"""<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="{css_path}">
</head>
<body>
"""
    for line in md_text.split("\n"):
        if line.startswith("### "):
            html_text += f"<h3>{line[4:]}</h3>\n"
        elif line.startswith("## "):
            html_text += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith("# "):
            html_text += f"<h1>{line[2:]}</h1>\n"
        elif line.startswith("- "):
            html_text += f"<li>{line[2:]}</li>\n"
        else:
            html_text += f"<p>{line}</p>\n"

    html_text += """
</body>
</html>
"""
    return html_text


class Restructure:

    def __init__(self):
        self.root_dir = "/workspace/firmware"
        self.source_dir = "/workspace/source"
        self.files_dir = os.path.join(self.root_dir, "files/uf2")
        self.html_files_dir = '/workspace/html/files'
        self.files_txt = []
        self.hash_txt = []

    def calculate_hash(self, file_path):
        print(f"Calculating hash for {file_path}...")
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def move_and_hash_files(self):
        print("Moving and hashing uf2 files...")
        if not os.path.exists(self.html_files_dir):
            os.makedirs(self.html_files_dir)

        for dirpath, dirnames, filenames in os.walk("/pico-app/build"):
            for filename in filenames:
                if filename.endswith('.uf2'):
                    src = os.path.join(dirpath, filename)
                    dest = os.path.join(self.files_dir, filename)
                    html_dest = os.path.join(self.html_files_dir, filename)

                    shutil.move(src, dest)
                    shutil.copy(dest, html_dest)

                    relative_dir = os.path.relpath(dirpath, self.root_dir)
                    self.files_txt.append(f"{filename} originally from {relative_dir}")

                    file_hash = self.calculate_hash(dest)
                    self.hash_txt.append(f"{filename} hash: {file_hash}")

        for dirpath, dirnames, filenames in os.walk("/pico-app"):
            for filename in filenames:
                if filename == 'README.md':
                    md_filepath = os.path.join(dirpath, filename)
                    html_dest = os.path.join('/workspace/static', 'rtfm.html')

                    with open(md_filepath, 'r', encoding='utf-8') as f:
                        text = f.read()

                    html_text = simple_md_to_html(text, '/app/static/styles.css')
                    
                    with open(html_dest, 'w', encoding='utf-8') as f:
                        f.write(html_text)

    def move_source_files(self):
        print("Moving source files...")
        for dirpath, dirnames, filenames in os.walk("/pico-app"):
            for dirname in dirnames:
                if dirname != "build":
                    src = os.path.join(dirpath, dirname)
                    dest = os.path.join(self.source_dir, dirname)
                    shutil.move(src, dest)

    def write_txt_files(self):
        print("Writing files.txt and hash.txt...")
        with open(os.path.join(self.html_files_dir, 'files.txt'), 'w') as f:
            f.write("\n".join(self.files_txt))

        with open(os.path.join(self.html_files_dir, 'hash.txt'), 'w') as f:
            f.write("\n".join(self.hash_txt))

    def generate_build_info(self):
        print("Generating build information...")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hostname = platform.node()
        os_info = platform.platform()

        build_info = [
            f"Build Time: {current_time}",
            f"Hostname: {hostname}",
            f"Operating System: {os_info}"
        ]

        with open(os.path.join(self.html_files_dir, 'build_info.txt'), 'w') as f:
            f.write("\n".join(build_info))

    def generate_hash_howto(self):
        print("Generating hash verification how-to...")
        howto_content = [
            "How to verify SHA-256 hashes:",
            "",
            "Windows:",
            "CertUtil -hashfile pathToFile SHA256",
            "",
            "Linux:",
            "sha256sum pathToFile",
            "",
            "macOS:",
            "shasum -a 256 pathToFile"
        ]

        with open(os.path.join(self.html_files_dir, 'hash_howto.txt'), 'w') as f:
            f.write("\n".join(howto_content))

    def execute(self):
        if not os.path.exists(self.files_dir):
            os.makedirs(self.files_dir)
        if not os.path.exists(self.source_dir):
            os.makedirs(self.source_dir)

        self.move_and_hash_files()
        self.move_source_files()
        self.write_txt_files()
        self.generate_build_info()
        self.generate_hash_howto()


if __name__ == "__main__":
    restructure = Restructure()
    restructure.execute()
