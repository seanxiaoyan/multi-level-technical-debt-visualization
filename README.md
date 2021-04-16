# multi-level-technical-debt-visualization(MLTDVT)
# Instruction
MLTDVT visualizes code/design and architecture smells from Java source code using the [GetSmells](https://github.com/tdresearchgroup/GetSmells/).

# Prerequisites
MLTDVT is written to work on either Windows or MacOS (tested on Windows 7 and MacOS 10.14)

1. Understand: 
  * You must have [Understand](https://scitools.com/features/) installed locally to run the GetSmells.
  * It should be installed in the default location for your OS (`C:\Program Files\SciTools\` for Windows or
`/Applications/Understand.app` on MacOS); if it is not in the default location, you can modify the paths at 
the top of both `understandapi.py` and `understandcli.py`.
2. GetSmells: 
  *  You must have [GetSmells](https://github.com/tdresearchgroup/GetSmells/) to run the MLTDVT.
  *  Put the folder of GetSmells under the project root folder (see [Project structure](#Project-structure-on-directory-level))
  *  Add the path of GetSmells in PYTHONPATH
3. Python: 
  * Python 3.6+ is required 
  * [NumPy](https://docs.scipy.org/doc/numpy/index.html) is required: `pip3 install numpy`

4. Node.js and npm
  * You need to install Node.js; npm is distributed with Node.js- which means that when you download Node.js, you automatically get npm installed on your computer.

# Project structure on directory level
```
multi-level-technical-debt-visualization
├─detailedClass: detailed view - class level visualization
│   ├──treemap.js: treemap that visualizes class level smells
│   ├──viewClass.html: detailed view - class level page
├─detailedMethod: detailed view - class level visualization
│   ├──treemap.js: treemap that visualizes method level smells
│   ├──viewMethod.html: detailed view - method level page
├─detailedPackage: detailed view - package level visualization
│   ├──treemap.js: treemap that visualizes package level smells
│   ├──viewPackage.html: detailed view - package level page
├─GetSmells: The code smell detection tool
├─overview: overview for code smells
│   ├──chart.js: pie chart and bar chart
│   ├──overview.html: overview page
└─preProcessing
    ├──getSmell.js: code for executing setconfig.py, executing getsmell.sh and executing processData.py
    ├──getsmell.sh: shell script for executing GetSmells
    ├──processData.py: python script for process code smells data 
    ├──setconfig.py: python script for setting Java source code path for the execution of GetSmells
``` 

# Usage
## Under the project root directory, do the following commands
Under the MLTDVT project root folder, executing these following commands: <br/>
npm install <br/>
npm start <br/>
![usage](https://user-images.githubusercontent.com/51433033/115074904-8f945980-9eb7-11eb-8ab7-b611d5070670.png)

