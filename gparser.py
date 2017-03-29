from os import path
from collections import deque
import re


class Parser():
    '''Abstract fetcher for Gaussian's files parameter value

    Attrs
    _file: File object
    _matrix_unpacker: Unpacks the atom coordinates into a list


    Comments:

    1- Should implement subclasses for different kinds of parsers for different
    kinds of File (ie IM, TS, etc)

    2- I can set a section 'class' to handle different sections for the input/
    output docs. class Parser could call Section's getter functions to retrieve
    valuable data
    '''

    def __init__(self, p):
        self._file = deque(open(path.abspath(p), 'r'))
        self._sections = self._get_sections

    def _get_calctype(self, delim, start=0):
        calctype = None
        p_delim, p_calctype = (re.compile(delim),
                           re.compile(r'(?P<calc_type>\b([\w-])+\b)')

        for i, line in enumerate(self._file[start:]):
            m_delim = p_delim.match(line)

            if m_delim:
                m_calctype = p_calctype.match(self._file[start+i+1])
                calctype = m_calctype.group('calc_type')
                return calctype
            else:
                continue

        return calctype

    def _get_name(self, delim, start=0):
        '''
        TODO: This function is unable to return file name if it exceeds one line
        '''

        name = None
        p_delim, p_name = (re.compile(delim),
                           re.compile(r'''
                                      (?:\b([\w-])+\b)
                                      [ ]
                                      (?P<name> .+)
                                      ''', re.X))

        for i, line in enumerate(self._file[start:]):
            m_delim = p_delim.match(line)

            if m_delim:
                m_name = p_name.match(self._file[start+i+1])
                name = m_name.group('name')
                return name
            else:
                continue

        return name


    def _get_z_matrix(self, udelim, ldelim):
        '''
        This method could be used to search and retrieve any z-matrix, including
        intermediate steps in an optimization. If such function were desirable,
        the delim concept would need to be changed to something else...
        '''

        p_udelim, p_ldelim, p_coords = (re.compile(udelim),
                                        re.compile(ldelim),
                                        re.compile(r'''
                                                       [ ]?
                                                       (?P<elem> [a-zA-Z])
                                                       [ ]+
                                                       (?P<x> -?[0-9]+[.][0-9]+\b)
                                                       [ ]+
                                                       (?P<y> -?[0-9]+[.][0-9]+\b)
                                                       [ ]+
                                                       (?P<z> -?[0-9]+[.][0-9]+\b)
                                                       ''', re.X)
                                        )
        m = p.match(line)

        if m:
            coord_dict = m.groupdict()
            coord_dict['index'] = index

        return coord_dict

    def _get_charge(self):
        pass

    def _get_multiplicity(self):
        pass



    def _matrix_unpacker(self, coord, index):
        # TODO Decide if this feature is needed
        # Useful only for Parser's subclasses internal methods; should this be
        # implemented some other way?
        pass

        p = re.compile(r'''
                       [ ]?
                       (?P<elem> [a-zA-Z])
                       [ ]+
                       (?P<x> -?[0-9]+[.][0-9]+\b)
                       [ ]+
                       (?P<y> -?[0-9]+[.][0-9]+\b)
                       [ ]+
                       (?P<z> -?[0-9]+[.][0-9]+\b)
                       ''', re.X)

        m = p.match(line)

        if m:
            coord_dict = m.groupdict()
            coord_dict['index'] = index

        return coord_dict


class I_Parser(Parser):
    '''I_GFiles' fetcher of parameter values

    _name: File's Title Card
    _z_matrix: File's Z-matrix
    _calctype: Calculation Type
    '''

    def __init__(self, p, calc):
        super().__init__(p)


    @property
    def _name(self):
        p1, p2, p3 = (re.compile('^ *$'),
             re.compile('.+'),
             re.compile('^ *$'))

        # Isn't there a more pythonic way to do this?

        for i in range(len(self._file) - 2):
            m1, m2, m3 = (p1.match(self._file[i]),
                         p2.match(self._file[i+1]),
                         p3.match(self._file[i+2]))

            if m1 is None:
                continue
            elif m2 and m3:
                return self._file[i+1]
        else:
            return None

    @_name.setter
    def _name(self, value):
        raise AttributeError('Property is Read-Only')

    @_name.deleter
    def _name(self): #
         # Causes RecursionError
         # TODO Learn how to implement deleter
         # self._name
         pass

    @property
    def _z_matrix(self):
        p = re.compile(r'[0-9] [0-9]')

        for i, l in enumerate(self._file):
            m = p.match(l)

            if m:
                for k, l in self._file[i+1:]:
                    self._z_matrix()

    @_z_matrix.setter
    def _z_matrix(self, value):
        raise AttributeError('Property is Read-Only')

    @_z_matrix.deleter
    def _z_matrix(self):
        # TODO implement deleter
        pass

class O_Parser(Parser):
    '''O_GFiles' fetcher of parameter values

    _name: File's Title Card
    _z_matrix: File's Z-matrix
    _calctype: Calculation Type
    '''

    def __init__(self, p, calc):
        super().__init__(p)


    @property
    def _name(self):
        p1, p2, p3 = (re.compile('^ *$'),
             re.compile('.+'),
             re.compile('^ *$'))

        # Isn't there a more pythonic way to do this?

        for i in range(len(self._file) - 2):
            m1, m2, m3 = (p1.match(self._file[i]),
                         p2.match(self._file[i+1]),
                         p3.match(self._file[i+2]))

            if m1 is None:
                continue
            elif m2 and m3:
                return self._file[i+1]
        else:
            return None

    @_name.setter
    def _name(self, value):
        raise AttributeError('Property is Read-Only')

    @_name.deleter
    def _name(self): #
         # Causes RecursionError
         # TODO Learn how to implement deleter
         # self._name
         pass

    @property
    def _z_matrix(self):
        p = re.compile(r'[0-9] [0-9]')

        for i, line in enumerate(self._file):
            m = p.match(line)

            if m:



        return coords

    @_z_matrix.setter
    def _z_matrix(self, value):
        raise AttributeError('Property is Read-Only')

    @_z_matrix.deleter
    def _z_matrix(self):
        # TODO implement deleter
        pass
