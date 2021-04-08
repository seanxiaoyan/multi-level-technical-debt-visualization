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
  *  You must have the [GetSmells](https://github.com/tdresearchgroup/GetSmells/) to run the MLTDVT.
  *  Put the folder of GetSmells under the project root folder (see [Project structure](#Project-structure-on-directory-level))
3. Python: 
  * Python 3.6+ is required 
  * [NumPy](https://docs.scipy.org/doc/numpy/index.html) is required: `pip3 install numpy`
  * Add project GetSmells in PYTHONPATH

# Project structure on directory level
```
multi-level-technical-debt-visualization
├─detailedClass
├─detailedMethod
├─detailedPackage
├─GetSmells
├─overview
└─preProcessing
``` 

# Usage
## Under the project root directory, do the following commands
npm install <br/>
npm start <br/>

