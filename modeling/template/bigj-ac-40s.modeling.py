#!/usr/bin/env python

from __future__ import print_function
import IMP
import IMP.core
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

test = False
if sys.argv[1] == '--test':
    test = True
    del sys.argv[1]
data=sys.argv[1]
datafile=sys.argv[2]
modeled_complex=sys.argv[3]
scale=float(sys.argv[4])
move_ac=sys.argv[5]
crosslink_slope=float(sys.argv[6])
crosslink_classification=sys.argv[7]

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
simo = representation.Representation(m, upperharmonic=True,
                                     disorderedlength=False)

if modeled_complex=="all":
   exec(open("bigj.topology.py").read())
   exec(open("ac.topology.py").read())

   exec(open("40s.topology.py").read())

   if move_ac=="fix_ac": 
      simo.shuffle_configuration(100,bounding_box=((0,0,-100),(200,200,100)),excluded_rigid_bodies=[rb40s,ac_rb,eIF3c_cterm_helix])
   elif move_ac=="move_ac": 
      simo.shuffle_configuration(100,bounding_box=((0,0,-100),(200,200,100)),excluded_rigid_bodies=[rb40s])
   else:
      print("cannot understand move_ac argument")
      exit()      

   #restore the position of the termini
   
   pos = tools.get_terminal_residue_position(simo, eIF3c, terminus="N",
                                             resolution=1)
   for h in eIF3c_ntd: 
       for p in IMP.atom.get_leaves(h):
           IMP.core.XYZ(p).set_coordinates(pos)
       
   pos = tools.get_terminal_residue_position(simo, eIF3a, terminus="C",
                                             resolution=1)
   for h in eIF3a_ctd: 
       for p in IMP.atom.get_leaves(h):
           IMP.core.XYZ(p).set_coordinates(pos)  
   
   pos = tools.get_terminal_residue_position(simo, eIF3c_cterm_helix,
                                             terminus="N", resolution=1)
   for h in eIF3c_cterm_beads:
       for p in IMP.atom.get_leaves(h):
           IMP.core.XYZ(p).set_coordinates(pos)         
   
   if move_ac=="fix_ac": 
      simo.fix_rigid_bodies([rb40s,ac_rb])
   elif move_ac=="move_ac": 
      simo.fix_rigid_bodies([rb40s])
   else:
      print("cannot understand move_ac argument")
      exit()      
elif modeled_complex=="bigj":
   exec(open("bigj.topology.py").read())
   simo.shuffle_configuration(100)   
if modeled_complex=="b40s":
   exec(open("bbetaprop.topology.py").read())
   exec(open("40s.topology.py").read())
   simo.shuffle_configuration(100,bounding_box=((0,0,-100),(200,200,100)),excluded_rigid_bodies=[rb40s])
   simo.fix_rigid_bodies([rb40s])


simo.set_floppy_bodies()
simo.setup_bonds()

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
   print("wrong crosslink classification")
   exit()

xl = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo, 
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



if test:
    nframes = 500
else:
    nframes = 10000
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
                      number_of_frames=nframes,
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


