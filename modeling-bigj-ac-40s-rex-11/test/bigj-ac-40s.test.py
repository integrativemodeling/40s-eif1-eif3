
import IMP
import IMP.core
import IMP.base
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.restraints.crosslinking
import IMP.pmi.representation as representation
import IMP.pmi.tools as tools
import IMP.pmi.samplers as samplers
import IMP.pmi.output as output
import IMP.pmi.macros as macros

import os
import sys


root='../'

datadir=root+"./data/"
pdbdir=root+"./data/"
sequencedir=root+"./Sequence/"
outputobjects = []
sampleobjects = []

#data="Only_10_7_13"
#datafile="XL_MS_all_data_19.12.13.csv"

data="Only_10_7"
datafile="XL_MS_all_data_20.12.13.csv"
modeled_complex="all"
scale=2.0
move_ac="move_ac"
crosslink_classification="Triple"
psi1=0.1
psi2=0.2
psi3=0.3
sigma1=0.4
sigma2=0.5

if data=="Only_Big_S.cer":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%8_1%" OR 
   ":Sample}" == "%8_2%"  '''

if data=="Only_Big_D.han":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%13_1%" '''
   
if data=="Only_Big_D.han_S.cer":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%8_1%" OR 
   ":Sample}" == "%8_2%" OR  
   ":Sample}" == "%13_1%" '''

if data=="Only_Big_40s_bound":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%10_1%" OR
   ":Sample}" == "%10_2%" OR
   ":Sample}" == "%10_3%" OR
   ":Sample}" == "%11_1%" OR
   ":Sample}" == "%11_2%" OR   
   ":Sample}" == "%11_3%"  
   '''
if data=="Only_Big_All":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%10_1%" OR
   ":Sample}" == "%10_2%" OR
   ":Sample}" == "%10_3%" OR
   ":Sample}" == "%11_1%" OR
   ":Sample}" == "%11_2%" OR   
   ":Sample}" == "%11_3%" OR
   ":Sample}" == "%8_1%" OR 
   ":Sample}" == "%8_2%" OR
   ":Sample}" == "%13_1%"      
   '''

if data=="Only_10_8_13":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%10_1%" OR
   ":Sample}" == "%10_2%" OR
   ":Sample}" == "%10_3%" OR
   ":Sample}" == "%8_1%" OR
   ":Sample}" == "%8_2%" OR
   ":Sample}" == "%13_1%"  '''

if data=="Only_10_7_13":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%10_1%" OR
   ":Sample}" == "%10_2%" OR
   ":Sample}" == "%10_3%" OR
   ":Sample}" == "%7_1%" OR
   ":Sample}" == "%7_2%" OR
   ":Sample}" == "%7_3%" OR
   ":Sample}" == "%7_4%" OR
   ":Sample}" == "%7_5%" OR
   ":Sample}" == "%13_1%"  '''

if data=="Only_10":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%10_1%" OR
   ":Sample}" == "%10_2%" OR
   ":Sample}" == "%10_3%" '''

if data=="Only_10_13":
   filters='''
   "{ID_Score}" >= 28 AND
   ":Sample}" == "%10_1%" OR
   ":Sample}" == "%10_2%" OR
   ":Sample}" == "%10_3%" OR
   ":Sample}" == "%13_1%"  '''

if data=="Only_10_7":
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
simo = representation.SimplifiedModel(m,upperharmonic=True,disorderedlength=False)


execfile("bigj.topology_test.py")
execfile("ac.topology_test.py")
execfile("40s.topology_test.py")


simo.set_floppy_bodies()
simo.setup_bonds()

o=IMP.pmi.output.Output()
o.init_rmf("final.rmf3",[simo.prot])
o.write_rmf("final.rmf3")
o.close_rmf("final.rmf3")

outputobjects.append(simo)
sampleobjects.append(simo)


ev = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
ev.add_to_model()
outputobjects.append(ev)



columnmap={}
columnmap["Protein1"]='Protein_1'
columnmap["Protein2"]='Protein_2'
columnmap["Residue1"]='S.cer_Corr_1'
columnmap["Residue2"]='S.cer_Corr_2'
columnmap["IDScore"]='ID_Score'

if crosslink_classification=="Unique":
   ids_map=tools.map()
   ids_map.set_map_element(30,0.01)
elif crosslink_classification=="Double":
   ids_map.set_map_element(32.0,0.1)
   ids_map.set_map_element(37,0.01)
elif crosslink_classification=="Triple":
   ids_map=tools.map()
   ids_map.set_map_element(30.0,0.1)
   ids_map.set_map_element(34,0.05)
   ids_map.set_map_element(38,0.01)
else:
   print "wrong crosslink classification"
   exit()

xl = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo, 
                                   datadir+datafile,
                                   length=21.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   csvfile=True,
                                   ids_map=ids_map,
                                   filters=filters,
                                   resolution=1.0,
                                   attributes_for_label=["Unique ID"])
xl.add_to_model()
sigma=xl.get_sigma(1.0)[0]
psi1=xl.get_psi(0.01)[0]
psi2=xl.get_psi(0.05)[0]
psi3=xl.get_psi(0.1)[0]
psi1.set_scale(0.0928111098123)
psi2.set_scale(0.354725658612)
psi3.set_scale(0.457004420521)
sigma.set_scale(10.2928954697)
sampleobjects.append(xl)
outputobjects.append(xl)


print "Starting test"
o.write_test("test.current.dict",[simo,ev,xl])
#o.test("test.IMP-ee1763c6.PMI-4669cfca.dict",log_objects)



