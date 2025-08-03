import pickle

def save_file(file_name,obj,mode='wb'):
    with open(file_name,mode) as f:
        pickle.dump(obj,f)


def load_file(file_name,mode='rb'):
    with open(file_name,mode) as f:
        return pickle.load(f)


def main():
    pass

if __name__=='__main__':
    main()