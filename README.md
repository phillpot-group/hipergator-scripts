# hipergator-scripts
Scripts related to the HiPerGator HPC Cluster at UF

## Format
Script names should be short snake_case descriptions of their purpose. Please comment your code __heavily__ as a courtesy to those who are not familiar with it.

## Descriptions

### scancel_all.py
Cancels all of your currently running slurm jobs in the event you made a mistake and are too lazy to manually copy each jobid into a `scancel` command. The username is hard-coded so you will need to modify it for personal use. Assuming its location is in your PATH, you can run it directly with no args.
```
$ scancel_all.py
```
