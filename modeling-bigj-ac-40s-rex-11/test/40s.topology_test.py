map_p2c={}
map_p2c["RPS0"]="A"
map_p2c["RPS2"]="C"
map_p2c["RPS3"]="D"
map_p2c["RPS1"]="B"
map_p2c["RPS4"]="E"
map_p2c["RPS5"]="F"
map_p2c["RPS6"]="G"
map_p2c["RPS7"]="H"
map_p2c["RPS8"]="I"
map_p2c["RPS9"]="J"
map_p2c["RPS10"]="K"
map_p2c["RPS11"]="L"
map_p2c["RPS12"]="M"
map_p2c["RPS13"]="N"
map_p2c["RPS14"]="O"
map_p2c["RPS15"]="P"
map_p2c["RPS22"]="W"
map_p2c["RPS16"]="Q"
map_p2c["RPS17"]="R"
map_p2c["RPS18"]="S"
map_p2c["RPS19"]="T"
map_p2c["RPS20"]="U"
map_p2c["RPS21"]="V"
map_p2c["RPS23"]="X"
map_p2c["RPS24"]="Y"
map_p2c["RPS25"]="Z"
map_p2c["RPS26"]="a"
map_p2c["RPS27"]="b"
map_p2c["RPS31"]="f"
map_p2c["RPS28"]="c"
map_p2c["RPS29"]="d"
map_p2c["RPS30"]="e"
map_p2c["RACK1"]="g"

rigid_body_list=[]

pdbbits=[]

beadsize=20

for p in map_p2c:
    simo.add_component_name(p)
    simo.add_component_sequence(p,sequencedir+"protein_fasta.40S.SC_2.txt")
    
    
    if p in ["RPS9","RPS3","RPS27","RPS1","RPS20","RPS5","RPS11"]:
       pdbbits+=simo.autobuild_model(p,datadir+'40S_43S_map_fitted_helix_final.pdb', map_p2c[p],resolutions=[1,10], color=0.1,attachbeads=True,missingbeadsize=beadsize)
    elif p=="RPS14":
       pdbbits+=simo.autobuild_model(p,datadir+'40S_43S_map_fitted_helix_final.pdb', map_p2c[p],resolutions=[1,10], color=0.1,offset=+1,attachbeads=True,missingbeadsize=beadsize)

    elif p=="RPS8":
       pdbbits+=simo.autobuild_model(p,datadir+'40S_43S_map_fitted_helix_final.pdb', map_p2c[p],resolutions=[1,10], color=0.1,resrange=(1,200),attachbeads=True,missingbeadsize=beadsize)

    else:
       pdbbits+=simo.autobuild_model(p,datadir+'40S_43S_map_fitted_helix_final.pdb', map_p2c[p],resolutions=[1,10], color=0.1,attachbeads=True,missingbeadsize=beadsize)

    rigid_body_list.append(p)
    
    simo.show_component_table(p)
    simo.set_coordinates_from_rmf(p,"modeling-triple-12.1_cluster.0_0.rmf3",0)
    #simo.draw_component_composition(p)
    

simo.add_component_name("rnaribo")
pdbbits+=simo.add_component_pdb("rnaribo",datadir+'40S_43S_map_fitted_helix_final.pdb', "6",cacenters=True,resolutions=[1,10], color=0.4,isnucleicacid=True)
rigid_body_list.append("rnaribo")
simo.setup_component_geometry("rnaribo")
simo.set_coordinates_from_rmf("rnaribo","modeling-triple-12.1_cluster.0_0.rmf3",0)

simo.add_component_name("eIF1",color=1.0)
simo.add_component_beads("eIF1",[(1,24)])
pdbbits+=simo.add_component_pdb("eIF1",datadir+'eIF1_map_fitted_final.pdb', "i",cacenters=True,resolutions=[1,10], color=0.45,resrange=(25,108))
rigid_body_list.append("eIF1")
simo.setup_component_geometry("eIF1")
simo.setup_component_sequence_connectivity("eIF1",resolution=1,scale=scale)
simo.set_coordinates_from_rmf("eIF1","modeling-triple-12.1_cluster.0_0.rmf3",0)

rb40s=simo.set_rigid_bodies(rigid_body_list)

for p in map_p2c:
   simo.setup_component_sequence_connectivity(p,resolution=1,scale=scale)
   simo.setup_component_geometry(p)



