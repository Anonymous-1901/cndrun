#! /usr/bin/env python3

import subprocess as s
import optparse

op = optparse.OptionParser()
output = 'run.c'

op.add_option("-f", "--file",  dest="file", help="The file path you want to compile and run .")
op.add_option("-o", "--out", dest="silent", help="File name you want to save the executable as.")

(options,arguments) = op.parse_args()

file = options.file
out_name = options.silent

if not file and not out_name:
    print("[-] No input file given , use --help to view usage.")

elif out_name:
    return_code = s.call("gcc " + file + " -o " + out_name , shell=True)
    if return_code != 0:
        print("[-] Please check your code again !")
    else:
        print("[+] " + file+" saved as " + out_name)
    
else:
    return_code = s.call("gcc " + file + " -o " + output, shell=True)
    if return_code != 0:
        print("[-] Please Check your code again !")
    else:
        s.call("chmod +x " + output, shell=True)
        s.call("./" + output, shell=True)
        s.call("rm -rf " + output,shell=True)
