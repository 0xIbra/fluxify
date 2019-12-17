# Fluxify
> A micro python library that retrieves and organizes data from a yaml mapping.

####  Required packages
- **pandas**

## Installation
```bash
pip install fluxify
```

## Usage
Retrieve data from a simple CSV file
```csv
id,brand,price
938,Xaomi,390.90
04593,iPhone,1299.90
```
#### Implementation
```python
from fluxify.mapper import Mapper
import yaml

yamlmapping = """
brand:
    col: 1
price:
    col: 2
"""

Map = yaml.load(yamlmapping, Loader=yaml.FullLoader)
mapper = Mapper()
data = mapper.map('path/to/csvfile.csv', Map)
print(data)
```
**Output**
```python
[
    {
        'brand': 'Xaomi',
        'price': '390.90'
    },
    {
        'brand': 'iPhone',
        'price': '1299.90'
    }
]
```