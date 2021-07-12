Weekly exercise 4 submission by Matus Maruna MM223FJ


To run pagerank.py you can use Terminal (OSX) or CMD (Windows). Navigate to the folder containing pagerank.py and execute it using "python pagerank.py". pagerank.py requires you to specify the dataset location as an argument. The results location is optional and if not specified the results will simply be printed in the terminal. The rest of the arguments, err_tol, max_iter and beta are set respectively by default to 1e-06, 50 and 0.85. This can however be changed by specifing new values when executing pagerank. 
 

Example execution command: 

"python pagerank.py --data "three_communities.edgelist" --data_out "threecomm_results.txt" --err_tol 1e-06 --max_iter 50 --beta 0.85"

Printout with possible arguments: 
usage: pagerank.py [-h] [--data DATA] [--data_out DATA_OUT]
                   [--err_tol ERR_TOL] [--max_iter MAX_ITER] [--beta BETA]

optional arguments:
  -h, --help           show this help message and exit
  --data DATA          Edgelist file location
  --data_out DATA_OUT  Output save location
  --err_tol ERR_TOL
  --max_iter MAX_ITER
  --beta BETA

Requirements: 

numpy == 1.19.2
pandas == 1.1.2
argparse == 1.4.0

If you do not have these libraries installed use "pip install -r requirements.txt" 

