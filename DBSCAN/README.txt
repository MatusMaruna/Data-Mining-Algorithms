Weekly exercise 1 submission by Matus Maruna MM223FJ


To run dbscan.py you can use Terminal (OSX) or CMD (Windows). Navigate to the folder containing dbscan.py and execute it using "python dbscan.py --data file_location". dbscan.py requires you to specify the dataset location as an argument, epsilon and minpts are set to 0.2 and 20 respectively by default. They can also be changed by specifing the new values as arguments when executing dbscan.py. Lastly, the output can be saved to a seperate text file by specifing the output file location when executing dbscan.py if the output file location is not set the results will only be printed in the console. 

Example execution command: 

"python dbscan.py --data noisy_circles.csv --epsilon 0.2 --minpts 20 --output results.txt"

Printout with possible arguments: 

dbscan.py [-h] [--data DATA] [--epsilon EPSILON] [--minpts MINPTS]
                 [--output OUTPUT]

optional arguments:
  -h, --help         show this help message and exit
  --data DATA        Location of the CSV dataset
  --epsilon EPSILON
  --minpts MINPTS
  --output OUTPUT    Location for output of the results


Requirements: 

numpy == 1.19.2
pandas == 1.1.2
argparse == 1.4.0

If you do not have these libraries installed use "pip install -r requirements.txt" 

