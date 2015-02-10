
#!/bin/bash
#
#$ -S /bin/bash
#$ -l netapp=1G,scratch=1G
#$ -cwd
#$ -o /netapp/sali/pellarin/eIF3/modeling-bigj-ac-40s-rex-11/modeling-triple-14.1/job.output
#$ -e /netapp/sali/pellarin/eIF3/modeling-bigj-ac-40s-rex-11/modeling-triple-14.1/job.error
#$ -j y
#$ -l arch=linux-x64
#$ -l mem_free=2G
#$ -pe ompi 64
#$ -R yes
#$ -l netappsali=2G                  
#$ -l scrapp=2G
#$ -V
#$ -l h_rt=300:00:0.
#$ -t 1
#$ -N j.23

# 22 job name           j.23
# 22 number of proc     64
# 22 template directory template
# 22 final directory    modeling-triple-14.1
# 22 script name        bigj-ac-40s.modeling.py
# 22 data type          Only_10_7
# 22 data file          XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv
# 22 system             all
# 22 scale linker       4.0
# 22 move ac            move_ac
#########################################

  
# load MPI modules
module load openmpi-1.6-nodlopen
module load sali-libraries
# IMP stuff

export IMP=/netapp/sali/pellarin/imp-250114/imp-pmi-fast/setup_environment.sh


# write hostname and starting time 
hostname
date

# run the job
mpirun -np $NSLOTS $IMP python bigj-ac-40s.modeling.py Only_10_7 XL_MS_all_data_20.12.13_no_7_x_eif3_eif3.csv all 4.0 move_ac  0.01  Triple  

# done
date
