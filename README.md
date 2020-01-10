# Fluxify
> A Python package that eases the process of retrieving, organizing and modifying data.

####  Required packages
- **pandas**
- **PyYAML==5.2**
- **imperium**

## Installation
```bash
pip install fluxify
```

## Usage
Retrieve data from a simple CSV file
```csv
id,brand,price,state,published_at
938,Xaomi,390.90,used,2020-01-03 12:32:29
04593,iPhone,1299.90,new,2020-01-02 09:48:12
```
#### Implementation
```python
from fluxify.mapper import Mapper
import yaml

# Could also be loaded from a file
yamlmapping = """
brand:
    col: 1
price:
    col: 2
state:
    col: 3
publish_date:
    col: 4
    transformations:
        - { transformer: 'date', in_format: '%Y-%m-%d %H:%M:%S', out_format: '%H:%M %d/%m/%Y' }
is_new:
    conditions:
        -
            condition: "subject['state'] == 'new'"
            returnOnSuccess: True
            returnOnFail: False
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
        'price': '390.90',
        'state': 'used',
        'published_date': '12:32 03/01/2020'
        'is_new': False
    },
    {
        'brand': 'iPhone',
        'price': '1299.90',
        'state': 'new',
        'published_date': '09:48 02/01/2020'
        'is_new': True
    }
]
```

### Supported formats

Format      | CSV | JSON | XML | TXT
------------|-----|------|-----|-----
Supported   | YES | YES  | YES | NO

## Transformers
Fluxify has built-in transformers that can alter/modify the data.

Function        | Arguments                         | Description
----------------|-----------------------------------|--------------
**number**      | stringvalue                       | Parses a string to an **integer** or **float** value
**split**       | delimiter, index                  | Splits a string into parts with a **delimiter** and returns the splitted result if the **index** argument is not defined.
**date**        | in_format, out_format             | Let's you format a date string to the desired format.
**replace**     | search, new                       | Replaces the **search** value with **new** value from string
**boolean**     | No arguments                      | Parses a string to Boolean if the string contains [true|false|1|0]
**equipments_from_string** | delimiter              | Custom usage
**options_from_string**    | delimiter              | Custom usage