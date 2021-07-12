Weekly exercise 2 submission by Matus Maruna MM223FJ


To run sammon.py you can use Terminal (OSX) or CMD (Windows). Navigate to the folder containing sammon.py and execute it using "python sammon.py". sammon.py requires you to specify the dataset location as an argument. The default data output path is "data_out.csv", magic factor and the number of iterations is set to 0.35 and 50 respectively. The initilization argument specifies the initial projection, by default it is random however it can be set to "orthagonal" using the argument. 

Example execution command: 

"python sammon.py --data "blobs.csv" --data_out "blobs_out.csv" --magicfactor 0.35 --iterations 50 --initilization "orthagonal"

Printout with possible arguments: 
usage: sammon.py [-h] [--data DATA] [--data_out DATA_OUT]
                 [--magicfactor MAGICFACTOR] [--iterations ITERATIONS]
                 [--initilization INITILIZATION]

optional arguments:
  -h, --help            show this help message and exit
  --data DATA
  --data_out DATA_OUT
  --magicfactor MAGICFACTOR
  --iterations ITERATIONS
  --initilization INITILIZATION

Requirements: 

numpy == 1.19.2
pandas == 1.1.2
argparse == 1.4.0

If you do not have these libraries installed use "pip install -r requirements.txt" 

