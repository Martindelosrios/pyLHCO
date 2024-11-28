# pyLHCO package
<!-- README.md -->
## Installation

As this is a dev version for installing pyLHCO package you have to download the source doing:

`git clone https://github.com/Martindelosrios/pyLHCO.git`

Then, in the pyLHCO directory just do

`pip install .`

or just 
```python
from pyLHCO.pylhco import read_lhco

# Read file_name as a pandas data frame
df = read_lhco(file_name, outputType = 'df')

or as a numpy array

arr = read_lhco(file_name, outputType = 'array')

or as a dictionary

dict = read_lhco(file_name, outputType = 'dict')
```
`pip install git+https://github.com/Martindelosrios/pyLHCO.git`


Soon you will be able to do

`pip install pyLHCO`


## Tutorial
In [Examples](https://github.com/Martindelosrios/pyLHCO/tree/master/EXAMPLES) you can find some examples to start playing with pyLHCO, but is very simple!

Just 



## Developed by:

Martín de los Rios [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0003-2190-2196) 
<a href="https://martindelosrios.netlify.app/">
<img src=".badges/website.jpeg" alt="" width="20" height="20">
</a> (martindelosrios13@gmail.com)

