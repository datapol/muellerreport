#!/usr/bin/env python3
"""Write persons and organizationsin Mueller report to an xlsx spreadsheet"""

__copyright__ = 'Copyright (C) 2019, https://github.com/datapol. All rights reserved.'

# pylint: disable=superfluous-parens,import-error,undefined-loop-variable
import os
import xlsxwriter
from muellerreport.organizations import ORGANIZATION2DESC
from muellerreport.persons import PERSON2DESC

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")


def test_wrxlsx():
    """Write persons and organizations in Mueller report to an xlsx spreadsheet"""
    _wrxlsx('persons.xlsx', PERSON2DESC)
    _wrxlsx('organizations.xlsx', ORGANIZATION2DESC)

def _wrxlsx(fout_xlsx, name2desc):
    """Write name and description to an xlsx file."""
    workbook = xlsxwriter.Workbook(os.path.join(REPO, fout_xlsx))
    worksheet = workbook.add_worksheet()
    max_width = 20
    # pylint: disable=
    for row, (name, desc) in enumerate(sorted(name2desc.items())):
        worksheet.write(row, 0, name)
        worksheet.write(row, 1, desc)
        max_width = max(len(name), max_width)
    worksheet.set_column(0, 0, max_width-10)
    workbook.close()
    print('  {R:3} rows WROTE: {XLSX}'.format(R=row, XLSX=fout_xlsx))


if __name__ == '__main__':
    test_wrxlsx()

# Copyright (C) 2019, https://github.com/datapol. All rights reserved.
