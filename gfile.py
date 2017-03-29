class GFile():
    '''A Gaussian I/O file

    _parser: A GParser that searches for file's values

    _name : The file name
    _coords : Atom coordinates matrix
    _calctype : Calculation mode (i.e. IM optimization, Freeze, TS)
    _complete : Status of calculation (i.e. Complete, Uncomplete)

    _
    '''

    def __init__(self, path):

        self._parser = GParser(path)
        self._name = self._parser._name
        self._coords = self._parser._coords
