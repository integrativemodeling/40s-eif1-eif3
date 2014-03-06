simo.add_component_name("eIF3b",color=0.0)
simo.add_component_sequence("eIF3b",sequencedir+"protein_fasta.eIF3b.SC.txt")
eIF3b3=simo.add_component_pdb("eIF3b",pdbdir+'eIF3b_propeller_hybrid.pdb',
                               "A",resolutions=[1,10],cacenters=True)

#simo.draw_component_composition("eIF3b")
simo.setup_component_geometry("eIF3b")
simo.show_component_table("eIF3b")

simo.setup_component_sequence_connectivity("eIF3b",resolution=1.0,scale=scale)
simo.set_rigid_body_from_hierarchies(eIF3b3) 
