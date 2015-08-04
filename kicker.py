import sys

from mako.template import Template

import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"
Port         = 38149

MenuActions = {
    'c':    [],     # Configure
    'o':    [],     # Select OS
}

def do_menu():
    print chr(27) + "[2J"
    print "\nKicker - produce and serve kickstart files:\n\n"
    
    menu = Template(filename='menu/menu.tmpl', module_directory='/tmp')
    print(menu.render())
    do_status()
    
    try:
        choice = raw_input("\n\n\tPlease enter your choice\t\t:\t")
    except KeyError:
        print "\n\n\tInvalid choice\n"
        choice = False
        
    return choice

def do_status():
    print "\n\n\tServer status: Not implemented\n"
    return

def process_command(cmd):
    # TODO: Initialization of kickstart "engine"
    # TODO: Print command template
    # TODO: Execute necessary commands
    # TODO: Any exception handling
    return

def start_server():
    # TODO: Fork
    # TODO: Customise!
    server_address = ('0.0.0.0', Port)
    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTPD on ", sa[0], " port ", sa[1], "..."
    httpd.serve_forever()
    return

def main():
    choice = do_menu()
    start_server()

    while choice.lower() != 'q':
        choice = do_menu()
        if hasattr(MenuActions, choice):
            process_command(MenuActions[choice])
    return

if __name__ == "__main__":
    main()
