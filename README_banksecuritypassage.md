We will be creating a python package named BankSecurityPassage which 
will be used frequently in our main code and helps to enhance its efficiency 
and decreases code length.
1. A directory is created by the command:
>>>import os
>>>os.mkdir(“BankSecurityPassage”)
2. Different Modules are placed in the above created package
>>>
>>>Modules are:
>>>1. empver.py
>>>2. manver.py
>>>3. empreg.py
>>>4. empactfun.py
>>>5. autopdf.py
>>>6. loadf.py
>>>
>>>. _init_.py is created to consider the directories as a package
from empver import empverfun
from manver import manverfun
from empreg import empregfun
from empactfun import empactfunr, empactfunw
from autopdf import pdfn
from loadf import loadbar
 
G. The package can now be imported in our main code

Binary File:
Now, We have also saved a bankSecureEncryptedDATA.dat file which will be 
accessed by manager function in our main code.
The binary file is human unreadable and hence works as sort of encryption 
of top secret banking data
