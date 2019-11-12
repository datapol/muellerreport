#!/usr/bin/env python3
"""Compare names in the Mueller Report to person IDs in Buzz's TrumpWorld"""

__copyright__ = 'Copyright (C) 2019, https://github.com/datapol. All rights reserved.'

# pylint: disable=superfluous-parens,import-error,undefined-loop-variable
import os
from muellerreport.persons import PERSON2DESC


def test_wrxlsx():
    """Compare names in the Mueller Report to person IDs in Buzz's TrumpWorld"""
    obj = _Run('data/trumpworld/SchemaPerson.csv')
    ## for per in sorted(obj.pers_tw):
    ##     print('MMM', per)

    pers_mtch1, pers_mtch0 = obj.get_pers_mtch()
    for pers in pers_mtch0:
        print('BUZZ ONLY: {NAME}\nBUZZ ONLY: {DESC}\n'.format(
            NAME=pers, DESC=PERSON2DESC[pers]))
    print('MATCHED', len(pers_mtch1))
    print('NOT MATCHED', len(pers_mtch0))
    print('{N} Persons in Mueller Report'.format(N=len(PERSON2DESC)))

# pylint: disable=too-few-public-methods
class _Run(object):
    """Match Buzz's TrumpWorld with Mueller report"""

    REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")

    # determined by hand: Matches of Mueller Report and Buzz's TrumpWorld
    mueller2tw = {
        'Bannon, Stephen (Steve)': 'STEPHEN BANNON',
        'Berkowitz, A vi': 'AVRAHM BERKOWITZ',
        'Bossert, Thomas (Tom)': 'TOM BOSSERT',
        'Calamari, Matt': 'MATTHEW CALAMARI',
        'Clovis, Samuel Jr.': 'SAM CLOVIS',
        'Cohen, Michael': 'MICHAEL D. COHEN',
        'Davis, Richard (Rick) Jr.': 'RICK DAVIS',
        'Dearborn , Rick': 'RICK DEARBORN',
        'Flynn, Michael T.': 'MICHAEL FLYNN',
        'Gates, Richard (Rick) III': 'RICK GATES',
        'Graff, Rhona': 'RHONA GRAFF RICCIO',
        'Kasowitz, Marc': 'MARC E. KASOWITZ',
        'Kilimnik, Konstantin': 'KONSTANTIN V. KILIMNIK',
        'Manafort, Paul Jr.': 'PAUL MANAFORT',
        'McFarland, Kathleen (K.T.)': 'KATHLEEN TROIA MCFARLAND',
        'McGahn, Donald (Don)': 'DON MCGAHN',
        'Parscale, Bradley': 'BRAD PARSCALE',
        'Sessions, Jefferson III (Jeff)': 'JEFF SESSIONS',
        'Trump, Donald Jr.': 'DONALD TRUMP JR.',
        'Yanukovych, Viktor': 'VIKTOR F. YANUKOVYCH',
    }

    def __init__(self, fin_csv):
        self.pers_tw = self._init_trumpworld_persons(fin_csv)

    def get_pers_mtch(self):
        """Match Mueller Report persons and Buzz's TrumpWorls pweaona"""
        mtch1 = {}
        mtch0 = set()
        for pers in PERSON2DESC:
            words = pers.split(', ')
            if len(words) == 2:
                name_uc = '{FIRST} {LAST}'.format(FIRST=words[1].upper(), LAST=words[0].upper())
                # Exact name matches
                if name_uc in self.pers_tw:
                    mtch1[pers] = name_uc
                # Matches determined by hand
                elif pers in self.mueller2tw:
                    mtch1[pers] = name_uc
                # Not matched
                else:
                    print('{:50} {}'.format(name_uc, pers))
                    mtch0.add(pers)
        return mtch1, mtch0

    def _init_trumpworld_persons(self, fin_csv):
        """Read TrumpWorld's person IDs"""
        with open(os.path.join(self.REPO, fin_csv)) as ifstrm:
            return {line.rstrip() for line in ifstrm if line[1:2] != 'p'}


if __name__ == '__main__':
    test_wrxlsx()

# Copyright (C) 2019, https://github.com/datapol. All rights reserved.
