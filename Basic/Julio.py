"""
This is the second practice.
"""
def julio (string, number):
    """
    I like this program.
    """
    alpha_cod = ""
    codificated = ""
    i = 0 
    position = 0
    alpha = "ABCDEFGHIKLMNOPQRSTVX"
    while i < len(alpha):
        if i + number >= len(alpha) or i + number <= -1:
            alpha_cod = alpha_cod + alpha [(i + number) % len(alpha)]
        else:
            alpha_cod = alpha_cod + alpha[i + number]
        i = i + 1
    while position < len(string):
        if ord(string[position]) < ord("A") or ord(string[position]) > ord("Z"):
            codificated = codificated + string[position]
        else:
            codificated = codificated + alpha_cod[alpha.index(string[position])]
        position = position + 1
    return codificated
