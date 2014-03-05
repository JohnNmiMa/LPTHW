import pickle

class Pickler:

    def list_pickler(self, alist, afile):
        pickle.dump(alist, afile, pickle.HIGHEST_PROTOCOL)

    def unpickler(self, afile):
        return pickle.load(afile)
