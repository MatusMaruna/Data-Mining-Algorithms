Weekly exercise 6 submission by Matus Maruna MM223FJ


To run levenshtein.py you can use Terminal (OSX) or CMD (Windows). Navigate to the folder containing newman.py and execute it using "python levenshtein.py". levenshtein.py requires you to specify the string file location as an argument. The cost variables used in the distance calculation are set by default to cd:2, ci:2, cs:1 and can be adjusted using the arguments --c_del, --c_ins and --c_sub. The output is printed in console. 

Example execution command: 

"python levenshtein.py --file_path gene57.txt --c_del 2 --c_ins 2 --c_sub 1"

Printout with possible arguments: 
usage: levenshtein.py [-h] [--file_path FILE_PATH] [--c_del C_DEL]
                      [--c_ins C_INS] [--c_sub C_SUB]

optional arguments:
  -h, --help            show this help message and exit
  --file_path FILE_PATH File location
  --c_del C_DEL         Cost of deletion
  --c_ins C_INS         Cost of insertion
  --c_sub C_SUB         Cost of substitution



Requirements: 

argparse == 1.4.0
numpy == 1.19.2

If you do not have these libraries installed use "pip install -r requirements.txt" 

