import json

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from interface import INTERFACE_HTML
from gpt_bot import GPTBot

STYLE_SHEET = "https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.3.1/js/all.js"
MAX_TURN = 20


def server():
    # GPT-3.5/4
    bot = GPTBot()

    class MyHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            paths = {
            '/': {'status': 200},
            '/dialogue': {'status': 200},
            '/favicon.ico': {'status': 202},  # Need for chrome
            }
            if not urlparse(self.path).path in paths.keys():
                response = 500
                self.send_response(response)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                content = ""
                self.wfile.write(bytes(content, 'UTF-8'))
            else:
                parsed_path = urlparse(self.path)
                response = paths[parsed_path.path]['status']

                print('headers\r\n-----\r\n{}-----'.format(self.headers))

                self.send_response(response)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                if parsed_path.path == '/':
                    response = 500
                    self.send_response(response)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.end_headers()
                    content = ""
                    self.wfile.write(bytes(content, 'UTF-8'))
                elif parsed_path.path == '/dialogue':
                    if 'id' not in parse_qs(parsed_path.query).keys():
                        response = 500
                        self.send_response(response)
                        self.send_header('Content-Type', 'text/html; charset=utf-8')
                        self.end_headers()
                        content = ""
                        self.wfile.write(bytes(content, 'UTF-8'))
                    else:
                        dialogue_id = parse_qs(parsed_path.query)['id'][0]
                        content = INTERFACE_HTML.format(STYLE_SHEET, FONT_AWESOME, dialogue_id, MAX_TURN)
                        self.wfile.write(bytes(content, 'UTF-8'))


        def do_POST(self):
            """
            Handle POST request, especially replying to a chat message.
            """
            print('path = {}'.format(self.path))
            parsed_path = urlparse(self.path)
            print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))

            print('headers\r\n-----\r\n{}-----'.format(self.headers))

            if self.path == '/interact':
                content_length = int(self.headers['content-length'])
                try:
                    content = self.rfile.read(content_length).decode('utf-8')
                    body = json.loads(content)

                    print('body = {}'.format(body))

                    # GPT-3.5/4
                    ret = bot.ret_system_utt(body['context'], body['utt'], body["dialogueId"])

                    if ret is not None:
                        print("sys: " + ret, flush=True)
                    model_response = {"text": ret}
                except Exception as e:
                    print("error", e, flush=True)
                    model_response = {"text": f"error Message: {e}"}

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                json_str = json.dumps(model_response)
                self.wfile.write(bytes(json_str, 'utf-8'))


    print("Start", flush=True)
    address = ('localhost', 8080)

    MyHTTPRequestHandler.protocol_version = 'HTTP/1.0'
    with HTTPServer(address, MyHTTPRequestHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    server()