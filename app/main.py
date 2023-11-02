#!/usr/bin/env python3

from flask import Flask, render_template, send_from_directory, abort, Response
import os

class WebServer:

    def __init__(self, app, root_dir):
        self.app = app
        self.root_dir = root_dir

    def serve_file(self, filename):
        try:
            safe_path = os.path.abspath(os.path.join(self.root_dir, 'files', filename))
            if not safe_path.startswith(os.path.join(self.root_dir, 'files')):
                abort(403)
            return send_from_directory(os.path.join(self.root_dir, 'files'), filename)
        except Exception as e:
            abort(404)

    def read_txt_file(self, filename):
        try:
            with open(os.path.join(self.root_dir, 'files', filename), 'r') as f:
                return f.read()
        except Exception as e:
            return "File not found."

    def list_files(self):
        try:
            uf2_dir = os.path.join(self.root_dir, 'files')
            all_uf2_files = [f for f in os.listdir(uf2_dir) if f.endswith('.uf2')]
            info_files = [f for f in os.listdir(uf2_dir) if f.endswith('.txt')]

            nuke_files = [f for f in all_uf2_files if f.startswith('flash_')]
            uf2_files = [f for f in all_uf2_files if not f.startswith('flash_')]

            build_info = self.read_txt_file('build_info.txt')
            hash_howto = self.read_txt_file('hash_howto.txt')

            return render_template('index.html', uf2_files=uf2_files, info_files=info_files, nuke_files=nuke_files, build_info=build_info, hash_howto=hash_howto)
        except Exception as e:
            abort(500)

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
web_server = WebServer(app, "/app/html")

@app.route('/files/<path:filename>', methods=['GET'])
def serve_file(filename: str) -> Response:
    return web_server.serve_file(filename)

@app.route('/', methods=['GET'])
def list_files() -> Response:
    return web_server.list_files()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
