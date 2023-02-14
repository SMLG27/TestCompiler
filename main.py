import re




def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

if __name__ == '__main__':
    my_txt = "The best preparation for tomorrow is doing your best today."
    print(LetterCompiler(my_txt))