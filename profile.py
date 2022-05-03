import os,sys,platform

def clear():
 os.system('clear')
 print('\n\n{:^170}'.format(' '.join("PYTHON @ DEEPAK'S")))
 print('\n\n{:^170}\n\n'.format(''.join('version - '+platform.python_version())))
 sys.ps1='DS>'
 sys.ps2='-->'
 
clear()
