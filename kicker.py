MENU = [
    ["n",   "New"],
    ["c",   "Configure"],
    ["q",   "Quit"]
]

def do_menu():
    print chr(27) + "[2J"
    print "\nKicker - produce and serve kickstart files:\n\n"
    
    for m in MENU:
        print "\t%s)\t:\t%s" % (m[0], m[1])

    do_status()
    
    try:
        choice = raw_input("\n\n\tPlease enter your choice\t\t:\t")
    except KeyError:
        print "\n\n\tInvalid choice\n"
        choice = False
        
    return choice

def do_status():
    print "\n\n\tServer status: Not implemented\n"

def main():
    choice = do_menu()

    while choice.lower() != 'q':
        choice = do_menu()
        # TODO: Process the choice
    return

if __name__ == "__main__":
    main()
