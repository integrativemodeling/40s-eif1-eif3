#!/usr/bin/env python

import unittest
import sys
import os
import subprocess
import IMP.atom

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(unittest.TestCase):
    def test_modeling(self):
        os.chdir(os.path.join(TOPDIR, 'modeling', 'template'))
        p = subprocess.check_call([
             './bigj-ac-40s.modeling.py', '--test', 'Only_10_7',
             'cross-links.csv', 'all', '4.0', 'move_ac', '0.01', 'Triple'])
        # todo: make sure the outputs are actually reasonable
        for out in ('best.scores.rex.py', 'excluded.None.xl.db',
                    'included.None.xl.db', 'missing.None.xl.db',
                    'output/initial.0.rmf3', 'output/stat.0.out',
                    'output/stat_replica.0.out'):
            os.unlink(out)
        m = IMP.Model()
        mp = IMP.atom.read_pdb('output/pdbs/model.0.pdb', m)
        chains = IMP.atom.get_by_type(mp, IMP.atom.CHAIN_TYPE)
        self.assertEqual(len(chains), 41)
        atoms = IMP.atom.get_by_type(mp, IMP.atom.ATOM_TYPE)
        self.assertEqual(len(atoms), 9036)

if __name__ == '__main__':
    unittest.main()
