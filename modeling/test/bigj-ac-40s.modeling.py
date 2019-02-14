
import IMP
import IMP.core
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi1.restraints.stereochemistry
import IMP.pmi1.restraints.em
import IMP.pmi1.restraints.crosslinking
import IMP.pmi1.representation as representation
import IMP.pmi1.tools as tools
import IMP.pmi1.samplers as samplers
import IMP.pmi1.output as output
import IMP.pmi1.macros as macros

import os
import sys


root='../'

datadir=root+"./data/"
pdbdir=root+"./data/"
sequencedir=root+"./Sequence/"
rmf_file="0.rmf3"
outputobjects = []
sampleobjects = []

datafile="cross-links.csv"

crosslink_slope=0.01
scale=4.0

filters='''
"{ID_Score}" >= 28 AND
":Sample}" == "%10_1%" OR
":Sample}" == "%10_2%" OR
":Sample}" == "%10_3%" OR
":Sample}" == "%7_1%" OR
":Sample}" == "%7_2%" OR
":Sample}" == "%7_3%" OR
":Sample}" == "%7_4%" OR
":Sample}" == "%7_5%"'''

m = IMP.Model()
simo = representation.Representation(m,upperharmonic=True,disorderedlength=False)

exec(open("bigj.topology.py").read())
exec(open("ac.topology.py").read())
exec(open("40s.topology.py").read())

simo.fix_rigid_bodies([rb40s])  

simo.set_floppy_bodies()
simo.setup_bonds()

outputobjects.append(simo)
sampleobjects.append(simo)

ev = IMP.pmi1.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
ev.add_to_model()
outputobjects.append(ev)

columnmap={}
columnmap["Protein1"]='Protein_1'
columnmap["Protein2"]='Protein_2'
columnmap["Residue1"]='S.cer_Corr_1'
columnmap["Residue2"]='S.cer_Corr_2'
columnmap["IDScore"]='ID_Score'

ids_map=tools.map()
ids_map.set_map_element(30.0,0.1)
ids_map.set_map_element(34,0.05)
ids_map.set_map_element(38,0.01)

xl = IMP.pmi1.restraints.crosslinking.ISDCrossLinkMS(simo, 
                                   datadir+datafile,
                                   length=21.0,
                                   slope=crosslink_slope,
                                   columnmapping=columnmap,
                                   csvfile=True,
                                   ids_map=ids_map,
                                   filters=filters,
                                   resolution=1.0,
                                   attributes_for_label=["Unique ID"])
xl.add_to_model()
sampleobjects.append(xl)
outputobjects.append(xl)

xl.set_psi_is_sampled(False)
psi=xl.get_psi(0.01)[0]
psi.set_scale(0.0904085866341)

psi=xl.get_psi(0.05)[0]
psi.set_scale(0.310076000416)

psi=xl.get_psi(0.1)[0]
psi.set_scale(0.460970843856)

xl.set_sigma_is_sampled(False)
sigma=xl.get_sigma(1.0)[0]
sigma.set_scale(9.61342059784)

o=IMP.pmi1.output.Output()
o.write_test("test.new.stat."+rmf_file+".out",outputobjects)
o.test("test.stat."+rmf_file+".out",outputobjects)

exit()

rex=macros.ReplicaExchange0(m,
                      simo,
                      monte_carlo_sample_objects=sampleobjects,
                      output_objects=outputobjects,
                      crosslink_restraints=[xl],
                      monte_carlo_temperature=1.0,
                      replica_exchange_minimum_temperature=1.0,
                      replica_exchange_maximum_temperature=2.5,
                      number_of_best_scoring_models=100,
                      monte_carlo_steps=10,
                      number_of_frames=10000,
                      write_initial_rmf=True,
                      initial_rmf_name_suffix="initial",
                      stat_file_name_suffix="stat",
                      best_pdb_name_suffix="model",
                      do_clean_first=True,
                      do_create_directories=True,
                      global_output_directory="./output",
                      rmf_dir="rmfs/",
                      best_pdb_dir="pdbs/",
                      replica_stat_file_suffix="stat_replica",
                      em_object_for_rmf=None,
                      replica_exchange_object=None)
rex.execute_macro()


