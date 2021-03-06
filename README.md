[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.46415.svg)](http://dx.doi.org/10.5281/zenodo.46415)

Eukaryotic translation initiation requires the recruitment of the large,
multiprotein eIF3 complex to the 40S ribosomal subunit. Using X-ray structures
of all major components of the minimal, six-subunit
_Saccharomyces cerevisiae_ eIF3 core, together with cross-linking
coupled to mass spectrometry, we were able to use
[IMP](http://integrativemodeling.org) to position and orient all eIF3
components on the 40S•eIF1 complex, revealing an extended, modular
arrangement of eIF3 subunits.

## Running the IMP/PMI scripts:

- `cd modeling/template`
- `./bigj-ac-40s.modeling.py Only_10_7 cross-links.csv all 4.0 move_ac 0.01 Triple` (on a single processor; prepend `mpirun -np 4` or similar if you built IMP with MPI support)

The calculation will generate a trajectory, `output/rmfs/0.rmf3`, in
[RMF format](http://integrativemodeling.org/rmf/). For convenience, the 100
best-scoring models are also output in PDB format in the `output/pdbs`
directory.

## Information

_Author(s)_: Riccardo Pellarin, Peter Cimermančič

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://salilab.org/imp/systems/?sysstat=10&branch=master)](http://salilab.org/imp/systems/) [![build info](https://salilab.org/imp/systems/?sysstat=10&branch=develop)](http://salilab.org/imp/systems/)

_Testable_: Yes.

_Parallelizeable_: Yes

_Publications_:
 - J. Erzberger, F. Stengel, R. Pellarin, S. Zhang, T. Schaefer, C. Aylett, P. Cimermančič, D. Boehringer, A. Sali, R. Aebersold, N. Ban. [Molecular architecture of the 40S•eIF1•eIF3 translation initiation complex](http://www.ncbi.nlm.nih.gov/pubmed/25171412), Cell 158, 1125-1135, 2014.
