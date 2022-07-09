
format PE Console 

entry start 

include 'win32a.inc' 


section '.data' data readable writeable 

	hello db 'hei',0 

section '.code' code readable writeable executable 

start: 
	invoke printf, hello 
  
  invoke getch 
  
  
  invoke ExitProcess, 0 
  

section '.idata' data import readable 
        library kernel, 'kernel32.dll',\ 
                msvcrt, 'msvcrt.dll'
  
  import kernel,\
  				ExitProcess, 'ExitProcess'
          
  import msvcrt,\
  				printf, 'printf',\
          getch, '_getch'
