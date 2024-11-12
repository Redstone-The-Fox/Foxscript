import termcolor as tc
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

class Errors: ...

class DuoQuotesNotFound(Errors):
    def __init__(self, msg):
        self.msg = msg
        exit(f'{tc.colored('(DuoQuotesNotFound)', 'red')} {self.msg}')

    def __str__(self):
        return f'DuoQuotesNotFound'

class InvalidStatement(Errors):
    def __init__(self, msg):
        self.msg = msg
        exit(f'{tc.colored('(InvalidStatement)', 'red')} {self.msg}')

    def __str__(self):
        return f'InvalidStatement'

def rse(error, message):
    print(error(message))

def collect_brace_content(text):
    content_list = []
    start = text.find('{')
    end = text.find('}', start)  # Find the closing brace after the opening brace

    while start != -1 and end != -1:
        # Extract content between the braces
        content = text[start + 1:end]
        
        # Add content to the list
        content_list.append(content)
        
        # Find the next `{` and `}`
        start = text.find('{', end)
        end = text.find('}', start)
    
    return content_list

def wrk(fname:str):
    with open(fname, 'rt+') as f:
        code:str = f.read()

    lines:list = code.splitlines()
    variables:dict = {"example_testvar": 'Hello, World!'}

    for line in lines:
        if line[0:7] == 'printl ':
            if line[7] == '"' and line[-1] == '"':
                collect_brace_content(line[6:].replace('"', ''))
                for i in collect_brace_content(line[6:].replace('"', '')):
                    thing_to_print = line[6:].replace('"', '').replace('{'+i+'}', variables[i])
                print(str(thing_to_print[1:]))
            else: rse(DuoQuotesNotFound, f'Double Quotation Marks not found at a {tc.colored('printl', 'cyan')} statement')
    #-----------
        elif line[0:6] == 'print ':
            if line[6] == '"' and line[-1] == '"':
                collect_brace_content(line[6:].replace('"', ''))
                for i in collect_brace_content(line[6:].replace('"', '')):
                    thing_to_print = line[6:].replace('"', '').replace('{'+i+'}', variables[i])
                print(str(thing_to_print), end='')
            else: rse(DuoQuotesNotFound, f'Double Quotation Marks not found at a {tc.colored('print', 'cyan')} statement')
    #-----------
        elif line[0] == '-' and line[1] == '-':
            ...
    #-----------
        else:
            rse(InvalidStatement, f'An invalid statement {line} was found')            

if __name__ == '__main__': wrk(args.filename)        