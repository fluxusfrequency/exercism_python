import re

COMMANDS = [
    'wink',
    'double blink',
    'close your eyes',
    'jump'
]

def handshake(code_pattern):
    code_pattern = __parse(code_pattern)
    message = [command for i, command in enumerate(COMMANDS) if __in_list(code_pattern, i)]
    if __in_list(code_pattern, 4):
        return list(reversed(message))
    return message

def code(messages):
    for message in messages:
        if message not in COMMANDS:
            return '0'
    return bin(sum([(2 ** i) for i, command in enumerate(COMMANDS) if command in messages]))[2:]

def __in_list(command, i):
    return command & (2 ** i) != 0

def __parse(code_pattern):
    if (type(code_pattern) is int and code_pattern < 0):
        code_pattern = 0
    if type(code_pattern) is not int:
        if re.match(r'^.*[2-9]+.*$', code_pattern):
            code_pattern = 0
        else:
            code_pattern = int(code_pattern, 2)
    return code_pattern
