#!/usr/bin/env python3
"""Create Pytohn modules for persons and organizationsin Mueller report"""

__copyright__ = 'Copyright (C) 2019, https://github.com/datapol. All rights reserved.'

import os

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..")

# pylint: disable=superfluous-parens
def main():
    """Create Pytohn modules for persons and organizationsin Mueller report"""
    fin_md = 'doc/mueller_report/md/README_appB_persons_orgs.md'
    fout_dct = {
        'Referenced Persons': 'src/py/muellerreport/persons.py',
        'Entities and Organizations': 'src/py/muellerreport/organizations.py'}

    type2name2desc = _get_type2name2desc(fin_md)
    for key, fout_py in sorted(fout_dct.items()):
        _wrpy(fout_py, type2name2desc[key], key)


def _wrpy(fout_py, name2desc, key):
    """Write name and description into a Python module"""
    with open(os.path.join(REPO, fout_py), 'w') as prt:
        num = len(name2desc)
        assert num > 15
        prt.write('"""{N} {KEY}"""\n\n'.format(N=num, KEY=key))
        prt.write("__copyright__ = '{C}'\n\n".format(C=__copyright__))
        prt.write('# pylint: disable=line-too-long\n')
        name = '{NAME}2DESC'.format(NAME=key.split(' ')[-1].upper()[:-1])
        prt.write('{NAME} = {{\n'.format(NAME=name))
        for name, desc in sorted(name2desc.items()):
            prt.write("    '{NAME}': '''{DESC}''',\n".format(NAME=name, DESC=desc))
        prt.write('}\n\n')
        prt.write('# {C}\n'.format(C=__copyright__))
        print('  {N:3} names WROTE: {PY}'.format(N=num, PY=fout_py))

def _get_type2name2desc(fin_md):
    """Read markdown file. Return names of people and orgs in a dict"""
    type2name2desc = {}
    print(fin_md)
    with open(os.path.join(REPO, fin_md)) as ifstrm:
        section = None
        name = None
        for line in ifstrm:
            line = line.rstrip()
            if line[:4] == '### ':
                name = line[4:]
            elif line[:3] == '## ':
                section = line[3:]
                type2name2desc[section] = {}
            elif line != '' and name is not None:
                type2name2desc[section][name] = line
        print('  READ: {MD}'.format(MD=fin_md))
    return type2name2desc



if __name__ == '__main__':
    main()

# Copyright (C) 2019, https://github.com/datapol. All rights reserved.
