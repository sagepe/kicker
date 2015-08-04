from mako.template import Template

menu_actions = {
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

def main():
    choice = do_menu()

    while choice.lower() != 'q':
        choice = do_menu()
        if hasattr(menu_actions, choice):
            process_command(menu_actions[choice])
    return

if __name__ == "__main__":
    main()
