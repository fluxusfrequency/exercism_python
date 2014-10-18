MOVES = {
    '1': 'wink',
    '10': 'double blink',
    '100': 'close your eyes',
    '1000': 'jump'
    }

def handshake(code):
    flag = False
    if type(code) is int:
        if (code < 0):
            return []
        code = bin(code)
        code = code[::-1][0:-2]
    else:
        if(len(code) > 4):
            flag = True
        code = code[::-1][0:4]
    coll = []
    for i, char in enumerate(code):
        if(char is '1'):
            key = char + ('0' * i)
            coll.append(MOVES[key])
        elif (char is not '0'):
            return []
    if (flag is True):
        return coll[::-1]
    return coll

def code(words):
    total = 0
    for word in words:
        if word not in MOVES.values():
            return '0'
        for code, move in reversed(sorted(MOVES.items())):
            if word == move:
                total += int(code, 2)
    return bin(total)[2:]

