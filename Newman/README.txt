Weekly exercise 3 submission by Matus Maruna MM223FJ


To run newman.py you can use Terminal (OSX) or CMD (Windows). Navigate to the folder containing newman.py and execute it using "python newman.py". newman.py requires you to specify the edgelist location as an argument. The default number of communities is 2 which can be changed using the communities argument. The output is printed in console and can be saved into a text file using the data_out argument and specifing the output location. 

Example execution command: 

"python newman.py --data karate.edgelist --data_out results.txt --communities 2"

Printout with possible arguments: 
usage: newman.py [-h] [--data DATA] [--data_out DATA_OUT]
                 [--communities COMMUNITIES]

optional arguments:
  -h, --help            show this help message and exit
  --data DATA           Edgelist file location
  --data_out DATA_OUT   Output save location
  --communities COMMUNITIES


Requirements: 

numpy == 1.19.2
pandas == 1.1.2
argparse == 1.4.0

If you do not have these libraries installed use "pip install -r requirements.txt" 

