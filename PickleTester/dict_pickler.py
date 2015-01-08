#!/usr/local/bin/python
import pickle

if __name__ == '__main__':
    dict = {'firstname':'John', 'lastname':'Marks'}
    print "dict = ", dict

    # pickle and then unpickle
    filename = 'dictfile'
    with open(filename, 'w') as file:
        pickle.dump(dict, file)
    with open(filename, 'r') as file:
        afterdict = pickle.load(file)

    print "afterdict = ", afterdict
