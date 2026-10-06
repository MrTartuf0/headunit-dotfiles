#!/usr/bin/env python3
import http.server
import socketserver
import subprocess
import urllib.parse

PORT = 8080

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Custom Webapp Placeholder</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        h1 { font-size: 3em; margin-bottom: 40px; color: #ddd; }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            width: 80%;
            max-width: 800px;
        }
        button {
            background-color: #2b303b;
            color: white;
            border: none;
            padding: 40px;
            font-size: 2em;
            border-radius: 15px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            transition: all 0.2s ease-in-out;
            font-weight: bold;
        }
        button:active {
            background-color: #4b5263;
            transform: scale(0.95);
        }
        .btn-yt { border-bottom: 5px solid #ff0000; }
        .btn-spot { border-bottom: 5px solid #1db954; }
        .btn-term { border-bottom: 5px solid #00ff00; }
        .btn-flac { border-bottom: 5px solid #00aaff; }
    </style>
</head>
<body>
    <h1>App Launcher</h1>
    <div class="grid">
        <button class="btn-yt" onclick="launch('youtube')">YouTube</button>
        <button class="btn-spot" onclick="launch('spotify')">Spotify</button>
        <button class="btn-term" onclick="launch('terminal')">Terminal</button>
        <button class="btn-flac" onclick="launch('flac')">FLAC Player</button>
    </div>

    <script>
        function launch(app) {
            fetch('/launch?app=' + app)
                .then(response => {
                    if(!response.ok) alert("Error launching " + app);
                });
        }
    </script>
</body>
</html>
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode('utf-8'))
        elif self.path.startswith('/launch'):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            app = query.get('app', [''])[0]
            
            flags = "--disk-cache-dir=/tmp/chromium-cache --disk-cache-size=104857600 --enable-features=UseOzonePlatform --ozone-platform=wayland --ignore-gpu-blocklist --enable-gpu-rasterization --enable-zero-copy --disable-features=OverscrollHistoryNavigation,Translate --disable-pinch --overscroll-history-navigation=0 --disable-background-networking --disable-ipc-flooding-protection --js-flags=--max-old-space-size=512"
            
            try:
                if app == 'youtube':
                    subprocess.Popen(f"chromium {flags} --user-agent='Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36' --app=https://m.youtube.com", shell=True)
                elif app == 'spotify':
                    subprocess.Popen(f"chromium {flags} --app=https://open.spotify.com", shell=True)
                elif app == 'terminal':
                    subprocess.Popen("foot", shell=True)
                elif app == 'flac':
                    # Fallback to foot terminal if no specific player was found, user can customize this
                    subprocess.Popen("foot -e bash -c 'echo \"FLAC Player Placehoder\"; sleep 2'", shell=True)
            except Exception as e:
                print(f"Error launching {app}: {e}")

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Launched")
        else:
            self.send_response(404)
            self.end_headers()

# Allow address reuse
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving dashboard at http://localhost:{PORT}")
    httpd.serve_forever()
