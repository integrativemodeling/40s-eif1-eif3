simo.add_component_name("eIF3b",color=0.0)
simo.add_component_sequence("eIF3b",sequencedir+"protein_fasta.eIF3b.SC.txt")
eIF3b0=simo.add_component_beads("eIF3b",[(1,36)])
eIF3b1=simo.add_component_pdb("eIF3b",pdbdir+'eIF3jb_model_updated.pdb',
                       "B",resolutions=[1,10], cacenters=True)
eIF3b2=simo.add_component_beads("eIF3b",[(131,145)])
eIF3b3=simo.add_component_pdb("eIF3b",pdbdir+'eIF3b_propeller_hybrid.pdb',
                               "A",resolutions=[1,10],cacenters=True)
eIF3b4=simo.add_component_beads("eIF3b",[(626,630)])
eIF3b5=simo.add_component_ideal_helix("eIF3b",resolutions=[1,10],resrange=(631,654))
#eIF3b4=simo.add_component_beads("eIF3b",[(626,635)])
eIF3b6=simo.add_component_pdb("eIF3b",pdbdir+'eIF3big_model_updated.pdb',
                               "B",resolutions=[1,10],cacenters=True,resrange=(655,698))
eIF3b7=simo.add_component_beads("eIF3b",[(699,724)])

#simo.add_component_name("bigj_densities",color=0.75)

#eIF3b1_dens_repr=simo.add_component_density_representation("bigj_densities",eIF3b1_dens[0])

#eIF3b3_dens=simo.add_component_density("bigj_densities",eIF3b3,
#                               num_components=5,resolution=1,
#                               inputfile=datadir+'eIF3b3_dens.txt')




#simo.draw_component_composition("eIF3b")
simo.setup_component_geometry("eIF3b")
simo.show_component_table("eIF3b")


simo.add_component_name("eIF3i",color=0.5)
simo.add_component_sequence("eIF3i",sequencedir+"protein_fasta.eIF3i.SC.txt")
eIF3i0=simo.add_component_pdb("eIF3i",pdbdir+'eIF3big_model_final.pdb', 
                          "I",resolutions=[1,10], resrange=(1,258), cacenters=True)
eIF3i1=simo.add_component_beads("eIF3i",[(259,270)])
eIF3i2=simo.add_component_pdb("eIF3i",pdbdir+'eIF3big_model_final.pdb', 
                          "I",resolutions=[1,10], resrange=(271,342), cacenters=True)

eIF3i3=simo.add_component_beads("eIF3i",[(343,347)])
#simo.draw_component_composition("eIF3i")
simo.setup_component_geometry("eIF3i")
simo.show_component_table("eIF3i")


simo.add_component_name("eIF3j",color=0.9)
simo.add_component_sequence("eIF3j",sequencedir+"protein_fasta.eIF3j.SC.txt")

eIF3j0=simo.add_component_beads("eIF3j",[(1,29)])
eIF3j1=simo.add_component_pdb("eIF3j",pdbdir+'eIF3jb_model_updated.pdb', "J",
                                                     resolutions=[1,10], cacenters=True)
eIF3j2=simo.add_component_necklace("eIF3j",41,116,25)
eIF3j5=simo.add_component_beads("eIF3j",[(117,145)])
eIF3j6=simo.add_component_pdb("eIF3j",pdbdir+'eIF3j_helical_model_updated.pdb', "J",
                                                     resolutions=[1,10], cacenters=True,resrange=(146,167))
eIF3j7=simo.add_component_pdb("eIF3j",pdbdir+'eIF3j_helical_model_updated.pdb', "J",
                                                     resolutions=[1,10], cacenters=True,resrange=(168,187))
eIF3j8=simo.add_component_pdb("eIF3j",pdbdir+'eIF3j_helical_model_updated.pdb', "J",
                                                     resolutions=[1,10], cacenters=True,resrange=(188,209))
eIF3j9=simo.add_component_beads("eIF3j",[(210,234),(235,265)])
#simo.setup_component_geometry("eIF3j")
simo.setup_component_geometry("eIF3j")
simo.show_component_table("eIF3j")


simo.add_component_name("eIF3g",color=1.0)
simo.add_component_sequence("eIF3g",sequencedir+"protein_fasta.eIF3g.SC.txt")
eIF3g0=simo.add_component_beads("eIF3g",[(1,7)])
eIF3g1=simo.add_component_pdb("eIF3g",pdbdir+'eIF3big_model_final.pdb', 
                              "G",resolutions=[1,10], resrange=(8,37),cacenters=True)
eIF3g2=simo.add_component_beads("eIF3g",[(38,42)])
eIF3g3=simo.add_component_pdb("eIF3g",pdbdir+'eIF3big_model_final.pdb', 
                              "G",resolutions=[1,10], resrange=(43,85),cacenters=True)
#simo.add_component_beads("eIF3g",[(85,85)])
eIF3g4=simo.add_component_pdb("eIF3g",pdbdir+'eIF3big_model_final.pdb', 
                              "G",resolutions=[1,10], resrange=(86,96),cacenters=True)
eIF3g5=simo.add_component_necklace("eIF3g",97,182,17)
eIF3g10=simo.add_component_pdb("eIF3g",datadir+'eif3g.183_281.pdb', "A",resolutions=[1,10], cacenters=True)
#simo.setup_component_geometry("eIF3g")
simo.setup_component_geometry("eIF3g")
simo.show_component_table("eIF3g")

#eIF3g1_dens=simo.add_component_density("bigj_densities",eIF3g1,
#                               num_components=1,resolution=1,
#                               inputfile=datadir+'eIF3g1_dens.txt')


#eIF3big_dens=simo.add_component_density("bigj_densities",eIF3i0+eIF3i2+eIF3b6+eIF3g3,
#                               num_components=5,resolution=1,
#                               inputfile=datadir+'eIF3big_dens.txt')



eIF3bRRM_Bprop=eIF3b0+eIF3b1+eIF3b2+eIF3b3+eIF3j0+eIF3j1+eIF3j2+eIF3j5+eIF3j6+eIF3j7+eIF3j8+eIF3j9
eIF3jhelices=eIF3j5+eIF3j6+eIF3j7+eIF3j8+eIF3j9
eIF3big_core=eIF3b4+eIF3b5+eIF3b6+eIF3b7+eIF3i0+eIF3i1+eIF3i2+eIF3i3+eIF3g0+eIF3g1+eIF3g2+eIF3g3+eIF3g4

simo.setup_component_sequence_connectivity("eIF3g",resolution=1.0,scale=scale)
simo.setup_component_sequence_connectivity("eIF3i",resolution=1.0,scale=scale)
simo.setup_component_sequence_connectivity("eIF3j",resolution=1.0,scale=scale)
simo.setup_component_sequence_connectivity("eIF3b",resolution=1.0,scale=scale)

simo.set_rigid_body_from_hierarchies(eIF3j0+eIF3j1+[eIF3j2[0]]+eIF3b0+eIF3b1) #RRM of eif3b + j(30-40) fragment
simo.set_rigid_body_from_hierarchies(eIF3b2+eIF3b3)     # b beta-propeller

simo.set_rigid_body_from_hierarchies(eIF3b4+eIF3b5)     # b short helix
simo.set_rigid_body_from_hierarchies(eIF3g2+eIF3g3+eIF3b6+eIF3b7+eIF3i0+eIF3i1+eIF3i2+eIF3i3) # b (c-term helix)+i (betapropller)+g (random coil) crystal
simo.set_rigid_body_from_hierarchies(eIF3g0+eIF3g1)     # g triple stranded beta-sheet
simo.set_rigid_body_from_hierarchies(eIF3g4+[eIF3g5[0]])   # g short helix
simo.set_rigid_body_from_hierarchies([eIF3g5[-1]]+eIF3g10)  # g RRM
simo.set_rigid_body_from_hierarchies(eIF3j5+eIF3j6)     # j helical region
simo.set_rigid_body_from_hierarchies(eIF3j7)            # j helical region
simo.set_rigid_body_from_hierarchies(eIF3j8+eIF3j9)     # j helical region


jlist=[eIF3j0,eIF3j1,eIF3j2,eIF3j5,eIF3j6,eIF3j7,eIF3j8,eIF3j9]
    
simo.set_chain_of_super_rigid_bodies(jlist,2,3)
    
blist=[eIF3b0,eIF3b1,eIF3b2,eIF3b3,eIF3b4,eIF3b5,eIF3b6,eIF3b7]

simo.set_chain_of_super_rigid_bodies(blist,2,3)
    
glist=[eIF3g0,eIF3g1,eIF3g2,eIF3g3,eIF3g4,eIF3g5,eIF3g10]
    
simo.set_chain_of_super_rigid_bodies(glist,2,3)
    
simo.set_super_rigid_body_from_hierarchies(eIF3bRRM_Bprop)
simo.set_super_rigid_body_from_hierarchies(eIF3jhelices)
simo.set_super_rigid_body_from_hierarchies(eIF3big_core)

simo.set_super_rigid_bodies(["eIF3b","eIF3i","eIF3g","eIF3j"])
simo.set_super_rigid_bodies(["eIF3b","eIF3i","eIF3g","eIF3j"])
simo.set_super_rigid_bodies(["eIF3b","eIF3i","eIF3g","eIF3j"])
simo.set_super_rigid_bodies(["eIF3b","eIF3i","eIF3g","eIF3j"])

