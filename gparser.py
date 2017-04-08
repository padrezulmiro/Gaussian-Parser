from os import path
from collections import deque
import re


class Parser():
    '''Abstract fetcher for Gaussian's files parameter value

    Comments:

    1- Should implement subclasses for different kinds of parsers for different
    kinds of File (ie IM, TS, etc)

    2- I can set a section 'class' to handle different sections for the input/
    output docs. class Parser could call Section's getter functions to retrieve
    valuable data

    3- Substitute for range() with for xrange() where needed
    '''

    def __init__(self, p):
        self._file = deque(open(path.abspath(p), 'r'))

    def parse_calctype(self, delim, start=0):

        calctype = None
        p_delim, p_calctype = (
                               re.compile(delim),
                               re.compile(r'(?P<calc_type>\b([\w-])+\b)')
                              )

        for i, line in enumerate(self._file[start:]):
            m_delim = p_delim.match(line)

            if m_delim:
                m_calctype = p_calctype.match(self._file[start+i+1])
                calctype = m_calctype.group('calc_type')
                return calctype
            else:
                continue

        return calctype

    def parse_name(self, titlecard):
        '''
        TODO: This function is unable to return file name if it exceeds one line
        If it were the case the titlecard should be given as a list of the lines
        of the titlecard.
        '''

        p_name = re.compile(r'''
                            (?:\b([\w-])+\b)
                            [ ]
                            (?P<name> .+)
                            ''', re.X)

        m_name = p_name.match(titlecard)

        return m_name.group('name')

    def parse_init_matrix(self, zmatrix):
        '''
        This method could be used to search and retrieve any z-matrix, including
        intermediate steps in an optimization. If such function were desirable,
        the delim concept would need to be changed to something else...
        '''

        index = 0
        p_coords = re.compile(r'''[ ]?
                              (?P<elem> [a-zA-Z])
                              [ ]+
                              (?P<x> -?[0-9]+[.][0-9]+\b)
                              [ ]+
                              (?P<y> -?[0-9]+[.][0-9]+\b)
                              [ ]+
                              (?P<z> -?[0-9]+[.][0-9]+\b)
                              ''', re.X)

        for line in zmatrix:
            index += 1
            m_coords = p_coords.match(line)

            if m_coords:
                coord_dict = m_coords.groupdict()
                coord_dict['index'] = index

        return coord_dict

    def _get_charge(self):
        pass

    def _get_multiplicity(self):
        pass

class I_Parser(Parser):
    '''I_GFiles' fetcher of parameter values'''

    def parse_name(self):
        delim = '\n'

        for i in range(len(self._file) - 2):
            if (
                self._file[i] == delim and
                not self._file[i+1] == '\n' and
                self._file[i+2] == delim
                ):

                return super().parse_name(self._file[i+1])

        return None

    def parse_init_matrix(self):
        matrix_list = []
        p_elec_state = re.compile(r'[0-9] [0-9]')

        for i in range(len(self._file) - 2):
            m = p_elec_state.match(self._file[i+1])

            if m:
                if self._file[i] == '\n' and not self._file[i+2] == '\n':
                    pass
                else:
                    continue

class O_Parser(Parser):
    '''O_GFiles' fetcher of parameter values'''

    pass
