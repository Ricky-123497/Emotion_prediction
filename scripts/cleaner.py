def _remove_punctuation_(string):
    punctuation= """<>?,./:";'{}|[]!@#$%^&*()_+-="""
    for i in punctuation:
        string=string.replace(i,"")
    return string

def _remove_number_(string):
    number="1234567890"
    for i in number:
        string=string.replace(i,"")
    return string

def clean(string):
    tmp=string.lower()
    tmp=_remove_punctuation_(tmp)
    tmp=_remove_number_(tmp)
    return tmp

def main() :
    pass

if __name__ == '__main__' :
    main()