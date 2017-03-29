import gparser

GFILEPATH = 'C:\Zulmiro\O_UEAU_open.com'

gp = gparser.I_Parser(GFILEPATH, 'Opt')

print('Name: ' + gp._name)
print('Printing Atom List:\n')

for atom in gp._z_matrix:
    print(atom)
