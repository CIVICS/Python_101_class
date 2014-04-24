#note this file is not to complie but to serve as a reference as instructions you'd input into the REPL environment
>>> infile = open("qbdata.txt","r")
>>> aline = infile.readline()
>>> aline
'Colt McCoy QB, CLE\t135\t222\t1576\t6\t9\t60.8%\t74.5\n'
>>>
>>> infile = open("qbdata.txt","r")
>>> linelist = infile.readlines()
>>> print(len(linelist))
34
>>> print(linelist[0:4])
['Colt McCoy QB CLE\t135\t222\t1576\t6\t9\t60.8%\t74.5\n',
 'Josh Freeman QB TB\t291\t474\t3451\t25\t6\t61.4%\t95.9\n',
 'Michael Vick QB PHI\t233\t372\t3018\t21\t6\t62.6%\t100.2\n',
 'Matt Schaub QB HOU\t365\t574\t4370\t24\t12\t63.6%\t92.0\n']
>>>
>>> infile = open("qbdata.txt","r")
>>> filestring = infile.read()
>>> print(len(filestring))
1708
>>> print(filestring[:256])
Colt McCoy QB CLE   135     222     1576    6       9       60.8%   74.5
Josh Freeman QB TB  291     474     3451    25      6       61.4%   95.9
Michael Vick QB PHI 233     372     3018    21      6       62.6%   100.2
Matt Schaub QB HOU  365     574     4370    24      12      63.6%   92.0
Philip Rivers QB SD 357     541     4710    30      13      66.0%   101.8
Matt Ha
>>>
