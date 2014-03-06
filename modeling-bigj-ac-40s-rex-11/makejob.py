from sys import argv
import os
import shutil



# 1.      10_x + 7_x (complete) - fixed AC              - OK
# 2.      10_x + 7_x (complete) with relaxed settings - fixed AC   - OK
# 3.      10_x + 7_x (no eIF3-eIF3 interlinks) - fixed AC  - OK 
# 4.      10_x + 7_x (no eIF3-eIF3 interlinks) with relaxed settings - fixed AC - OK
# 5.      10_x + 7_x (complete) - loose AC    - OK 
# 6.      10_x + 7_x (complete) with relaxed settings - loose AC  - OK
# 7.      10_x + 7_x (no eIF3-eIF3 interlinks) - loose AC    - OK
# 8.      10_x + 7_x (no eIF3-eIF3 interlinks) with relaxed settings - loose AC   - OK
# 9.      10_x + 7_x (no eIF3a-eIF3c interlinks) - fixed AC
# 10.     10_x + 7_x (no eIF3a-eIF3c interlinks) with relaxed settings - fixed AC
# 11.     10_x + 7_x (no eIF3a-eIF3c interlinks) - loose AC
# 12.     10_x + 7_x (no eIF3a-eIF3c interlinks) with relaxed settings - loose AC
# 13.     10_x + 7_x (run with eIF3b not attached to anything, i.e. no additional constraints beyond the cross links)

#            template_directory,                      directory_name,  script,                    data_type,     data_file,                        system,     scale_linker,     move_ac,       job_name,     nprocesses,   xl_slope,    xl_class     
jobs_table=[("template",  "modeling-triple-1.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "fix_ac",      "j.01",        "64",  "0.01", "Triple" ),
            ("template",  "modeling-triple-1.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "fix_ac",      "j.02",        "64",  "0.01", "Triple" ),  
            ("template",  "modeling-triple-2.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "fix_ac",      "j.03",        "64",  "0.01", "Triple" ),
            ("template",  "modeling-triple-2.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "fix_ac",      "j.04",        "64",  "0.01", "Triple" ),  
            ("template",  "modeling-triple-3.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "fix_ac",      "j.05",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-3.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "fix_ac",      "j.06",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-4.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "fix_ac",      "j.07",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-4.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "fix_ac",      "j.08",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-5.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "fix_ac",      "j.09",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-5.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "fix_ac",      "j.10",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-6.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "fix_ac",      "j.11",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-6.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "fix_ac",      "j.12",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-7.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "move_ac",      "j.13",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-7.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "move_ac",      "j.14",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-8.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "move_ac",      "j.15",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-8.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "move_ac",      "j.16",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-9.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "move_ac",      "j.17",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-9.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "move_ac",      "j.18",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-10.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "move_ac",      "j.19",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-11.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "move_ac",      "j.20",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-12.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "move_ac",      "j.21",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-13.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "move_ac",      "j.22",        "64",  "0.01", "Triple"  ),  
            ("template",  "modeling-triple-14.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "move_ac",      "j.23",        "64",  "0.01", "Triple"  ),
            ("template",  "modeling-triple-15.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "move_ac",      "j.24",        "64",  "0.01", "Triple"  ),
#########       
            ("template",  "modeling-triple-16.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "fix_ac",      "j.25",        "64",  "0.015", "Triple" ),
            ("template",  "modeling-triple-16.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "fix_ac",      "j.26",        "64",  "0.015", "Triple" ),  
            ("template",  "modeling-triple-17.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "fix_ac",      "j.27",        "64",  "0.015", "Triple" ),
            ("template",  "modeling-triple-17.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "fix_ac",      "j.28",        "64",  "0.015", "Triple" ),  
            ("template",  "modeling-triple-18.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "fix_ac",      "j.29",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-18.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "fix_ac",      "j.30",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-19.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "fix_ac",      "j.31",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-19.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "fix_ac",      "j.32",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-20.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "fix_ac",      "j.33",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-20.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "fix_ac",      "j.34",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-21.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "fix_ac",      "j.35",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-21.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "fix_ac",      "j.36",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-22.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "move_ac",      "j.37",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-22.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "1.0",           "move_ac",      "j.38",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-23.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "move_ac",      "j.39",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-23.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "2.0",           "move_ac",      "j.40",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-24.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "move_ac",      "j.41",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-24.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13.csv",    "all",      "4.0",           "move_ac",      "j.42",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-25.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "move_ac",      "j.43",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-25.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "1.0",           "move_ac",      "j.44",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-26.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "move_ac",      "j.45",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-26.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "2.0",           "move_ac",      "j.46",        "64",  "0.015", "Triple"  ),  
            ("template",  "modeling-triple-27.1",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "move_ac",      "j.47",        "64",  "0.015", "Triple"  ),
            ("template",  "modeling-triple-27.2",  "bigj-ac-40s.modeling.py", "Only_10_7",   "XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv",    "all",      "4.0",           "move_ac",      "j.48",        "64",  "0.015", "Triple"  )]

for n,job in enumerate(jobs_table):
  
  template_directory=job[0]
  directory_name=job[1]
  script=job[2] #ex. bigj-ac-40s.modeling.py
  data_type=job[3] #ex Only_10_13
  data_file=job[4] #ex XL_MS_all_data_20.12.13.csv
  system=job[5] #ex bigj
  scale_linker=job[6] #ex 2.0
  move_ac=job[7] #ex fix_ac/move_ac
  job_name=job[8]
  nprocesses=job[9]  
  crosslink_slope=job[10]
  crosslink_classification=job[11]
  output_file_name=os.getcwd()+"/"+directory_name+"/job.output"
  error_file_name=os.getcwd()+"/"+directory_name+"/job.error"
  
  info=''
  info+="# "+str(n)+" job name           "+job_name+"\n"
  info+="# "+str(n)+" number of proc     "+nprocesses+"\n"
  info+="# "+str(n)+" template directory "+template_directory+"\n"
  info+="# "+str(n)+" final directory    "+directory_name+"\n"
  info+="# "+str(n)+" script name        "+script+"\n"
  info+="# "+str(n)+" data type          "+data_type+"\n"
  info+="# "+str(n)+" data file          "+data_file+"\n"
  info+="# "+str(n)+" system             "+system+"\n"
  info+="# "+str(n)+" scale linker       "+scale_linker+"\n"
  info+="# "+str(n)+" move ac            "+move_ac+"\n"
  info+="#########################################"+"\n"
  
  print info
  
  shutil.copytree(template_directory, directory_name)
  
  os.chdir(directory_name)
  
  jobscript='''
#!/bin/bash
#
#$ -S /bin/bash
#$ -l netapp=1G,scratch=1G
#$ -cwd
#$ -o ####OUTPUT####
#$ -e ####ERROR####
#$ -j y
#$ -l arch=linux-x64
#$ -l mem_free=2G
#$ -pe ompi ####NPROCESSES####
#$ -R yes
#$ -l netappsali=2G                  
#$ -l scrapp=2G
#$ -V
#$ -l h_rt=300:00:0.
#$ -t 1
#$ -N ####JOBNAME####

####INFO####
  
# load MPI modules
module load openmpi-1.6-nodlopen
module load sali-libraries
# IMP stuff

export IMP=/netapp/sali/pellarin/imp-250114/imp-pmi-fast/setup_environment.sh


# write hostname and starting time 
hostname
date

# run the job
mpirun -np $NSLOTS $IMP python ####SCRIPT#### ####DATATYPE#### ####DATAFILE#### ####SYSTEM#### ####SCALE#### ####MOVEAC####  ####CROSSLINKSLOPE####  ####CROSSLINKCLASSIFICATION####  

# done
date
'''

  jobscript=jobscript.replace("####OUTPUT####",output_file_name)
  jobscript=jobscript.replace("####ERROR####",error_file_name)
  jobscript=jobscript.replace("####JOBNAME####",job_name)
  jobscript=jobscript.replace("####MOVEAC####",move_ac)
  jobscript=jobscript.replace("####SCALE####",scale_linker)
  jobscript=jobscript.replace("####SYSTEM####",system)
  jobscript=jobscript.replace("####DATAFILE####",data_file)
  jobscript=jobscript.replace("####DATATYPE####",data_type)
  jobscript=jobscript.replace("####SCRIPT####",script)
  jobscript=jobscript.replace("####NPROCESSES####",nprocesses)
  jobscript=jobscript.replace("####INFO####",info)
  jobscript=jobscript.replace("####CROSSLINKSLOPE####",crosslink_slope)
  jobscript=jobscript.replace("####CROSSLINKCLASSIFICATION####",crosslink_classification)
  jobfile=open("job.sh","w")
  jobfile.write(jobscript)
  
  os.chdir("../")

