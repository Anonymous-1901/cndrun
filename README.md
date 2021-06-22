# cndrun
-----------------------------------------------------------------------------
Usage: cndrun.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  The file path you want to compile and run .
  -o SILENT, --out=SILENT
                        File name you want to save the executable as.
                        
  Example: cndrun.py -f <filename> <argument>
                     
-----------------------------------------------------------------------------
A simple script to compile and run .c code just like Python !!

-- Requirements : --
Python3 
GCC
optparse (pip3 install optparse)

1. Git clone : 
  
  git clone https://github.com/Anonymous-1901/cndrun

2. Mark Executable :
  
  cd cndrun && chmod +x cndrun.py

3. Run the script : 

  python3 cndrun.py
  
4. To run codes from any directory , paste the script in /usr/bin/ run : 
  cp cndrun.py /usr/bin
  
