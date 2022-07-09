import argparse
from string import printable


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Set path to file")
parser.add_argument("-enc", help="File encoding, standart - UTF-8")
parser.add_argument("-o", help="Set output file, standart - a.asm")


args = parser.parse_args()

output = args.o + ".asm" if args.o else "a.asm"
enc = args.enc if args.enc else "UTF-8"
path = args.path

ascii_letters = list(printable)


result = """
format PE Console 

entry start 

include 'INCLUDE/win32a.inc' 


section '.data' data readable writeable 

	hello db 'TEXT_BY_MEGA_BRAIN',0 

section '.code' code readable writeable executable 

start: 
	invoke printf, hello 
  
  invoke getch 
  
  
  invoke ExitProcess, 0 
  

section '.idata' data import readable 
        library kernel, 'kernel32.dll',\ 
                msvcrt, 'msvcrt.dll'
  
  import kernel,\\
  				ExitProcess, 'ExitProcess'
          
  import msvcrt,\\
  				printf, 'printf',\\
          getch, '_getch'
"""

with open(path, encoding=enc) as f:
    code = f.read().strip()

number = 0
text = ""

for s in code:
    match s:
        case "1":
            number += 1
        case "0":
            text += ascii_letters[number]
        case " ":
            number = 0


with open(output, "w", encoding=enc) as f:
    f.write(result.replace("TEXT_BY_MEGA_BRAIN", text))