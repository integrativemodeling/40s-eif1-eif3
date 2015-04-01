

beadsize=20

simo.add_component_name("eIF3c",color=0.25)
eIF3c_ntd=simo.add_component_necklace("eIF3c",1,216,beadsize)
simo.add_component_sequence("eIF3c",sequencedir+"protein_fasta.eIF3c.SC.txt")
eIF3c=simo.autobuild_pdb_and_intervening_beads("eIF3c",pdbdir+'/eIF3ac_yeast_EM_fitted_variant.pdb', "A",
                                             resolutions=[1,10],beadsize=beadsize,resrange=(217,779))
eIF3c_cterm_helix=simo.add_component_pdb("eIF3c",pdbdir+'/eIF3ac_yeast_EM_fitted_variant.pdb', "A",
                                             resolutions=[1,10],cacenters=True,resrange=(780,794))
eIF3c_cterm_beads=simo.add_component_necklace("eIF3c",795,812,beadsize)

simo.show_component_table("eIF3c")

simo.setup_component_geometry("eIF3c")
#simo.draw_component_composition("eIF3c")


simo.add_component_name("eIF3a",color=0.75)
simo.add_component_sequence("eIF3a",sequencedir+"protein_fasta.eIF3a.SC.txt")
eIF3a=simo.autobuild_pdb_and_intervening_beads("eIF3a",pdbdir+'/eIF3ac_yeast_EM_fitted_variant.pdb', "C",
                                             resolutions=[1,10],beadsize=beadsize,resrange=(1,514))
eIF3a_ctd=simo.add_component_necklace("eIF3a",515,964,beadsize)                                             

#simo.add_component_name("ac_densities",color=0.75)
#eIF3ac_dens=simo.add_component_density("ac_densities",eIF3c+eIF3a,
#                               num_components=15,resolution=1,
#                               inputfile=datadir+'/eIF3ac_dens.txt')

simo.show_component_table("eIF3a")

simo.setup_component_geometry("eIF3a")
#simo.draw_component_composition("eIF3a")

simo.setup_component_sequence_connectivity("eIF3c",resolution=1.0,scale=scale)
simo.setup_component_sequence_connectivity("eIF3a",resolution=1.0,scale=scale)
simo.setup_component_geometry("eIF3c")
simo.setup_component_geometry("eIF3a")

ac_rb=simo.set_rigid_body_from_hierarchies(eIF3c+eIF3a) 
eIf3c_cterm_rb=simo.set_rigid_body_from_hierarchies(eIF3c_cterm_helix) 
   
simo.set_chain_of_super_rigid_bodies(eIF3c_ntd+eIF3c+eIF3c_cterm_helix+eIF3c_cterm_beads,2,3)
simo.set_chain_of_super_rigid_bodies(eIF3a+eIF3a_ctd,2,3)

simo.set_super_rigid_bodies(["eIF3a","eIF3c"])
