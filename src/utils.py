from termcolor import colored

def print_success(text, end='\n'):
    print(colored(text, 'green', attrs=['reverse']), end=end)

def print_warning(text, end='\n'):
    print(colored(text, 'yellow', attrs=['reverse']), end=end)

def print_failed(text, end='\n'):
    print(colored(text, 'red', attrs=['reverse']), end=end)
