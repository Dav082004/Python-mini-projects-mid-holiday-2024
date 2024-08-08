from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the hostname and port for the server
hostname = 'localhost'
server_port = 8000

# Create a custom HTTP request handler
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send a 200 OK response
        self.send_response(200)
        
        # Set the content type to HTML
        self.send_header("Content-type", 'text/html')
        self.end_headers()
        
        # Write the HTML content to the response
        self.wfile.write(bytes('<html><head><title>Python WEB</title></head>', 'utf-8'))
        self.wfile.write(bytes('<body><p>Este es un ejemplo de un servidor</p>', 'utf-8'))
        self.wfile.write(bytes('</body></html>', 'utf-8'))

if __name__ == '__main__':
    # Create and start the web server
    webServer = HTTPServer((hostname, server_port), MyServer)
    print(f'Servidor iniciado en http://{hostname}:{server_port}')

    try:
        # Run the server until interrupted
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        # Print any other exception that occurs
        print(f'Error: {e}')
    finally:
        # Close the server when done
        webServer.server_close()
        print('Servidor detenido')
