import termcolor as tc

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

def wrk(fname:str='main.fsc'):
    with open(fname, 'rt+') as f:
        code:str = f.read()

    lines:list = code.splitlines()

    for line in lines:
        if line[0:7] == 'printl ':
            if line[7] == '"' and line[-1] == '"':
                print(f'{line[7:].replace('"', '')}')
            else: rse(DuoQuotesNotFound, f'Double Quotation Marks not found at a {tc.colored('printl', 'cyan')} statement')
    #-----------
        elif line[0:6] == 'print ':
            if line[6] == '"' and line[-1] == '"':
                print(f'{line[6:].replace('"', '')}', end='')
            else: rse(DuoQuotesNotFound, f'Double Quotation Marks not found at a {tc.colored('print', 'cyan')} statement')
    #-----------
        elif line[0] == '-' and line[1] == '-':
            ...
    #-----------
        else:
            rse(InvalidStatement, f'An invalid statement {line} was found')            

if __name__ == '__main__': wrk()        