# Fluxify
> A Python package that eases the process of retrieving, organizing and altering data.

####  Required packages
- **pandas**
- **imperium**
- **ijson**

## Installation
```bash
pip install fluxify
```

## Main classes
#####  `fluxify.mapper.Mapper`
This class is used read and processing fast files with small amounts of data that can be loaded into memory.

##### `fluxify.lazy_mapper.LazyMapper`
You've probable guessed it, this class is used to iterate on large files of data wether it is of format CSV,
JSON or XML. 

## Usage
Retrieve data from a simple CSV file
```csv
id,brand,price,state,published_at
938,Xaomi,390.90,used,2020-01-03 12:32:29
04593,iPhone,1299.90,new,2020-01-02 09:48:12
```
#### Mapper implementation
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
mapper = Mapper(_type='csv')
data = mapper.map('path/to/csvfile.csv', Map)
print(data)
```
**Output**
```bash
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

#### LazyMapper implementation
The `LazyMapper` does not return all the mapped data at the end,  
instead it maps the data in small sizes that you can specify in order to not max out the memory.

```python
from fluxify.lazy_mapper import LazyMapper
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
mapper = LazyMapper(_type='csv', error_tolerance=True, bulksize=500)
mapper.map('path/to/csvfile.csv', Map)

def some_callback(results):
    for item in results:
        pass # Perform some action

mapper.set_callback(some_callback)

mapper.map('path/to/csvfile.csv', Map)
```
As you can see, in this example the mapper will call the callback function every time it accumulates 500 mapped items.

### Mapping settings
`col` key is used to specify the column number or attribute name from where the value must be retrieved.  
If you want to specify the input data as the retrieved value use `_all_` as the value of `col`

`transformations` key is used to apply transformations to the retrieved value.  Available transformers are listed below.

`conditions` key is used to apply conditions and alter the retrieved value.  
These conditions are in Python syntax, but you may not use all of Python's native functions.  
Available functions are listed below.

`default` is used to define a default value for when a retrieved value is **null**.  
**Warning**: If the `default` key is defined with a value, it will be applied before applying transformations
and conditions.

##### Special cases for JSON and XML
**XML**  
Set the `multiple` to `true` if you want to retrieve data from multiple XML tags with the same name.  
Use the `index` key with `multiple: true` if you wish to retrieve only one value from a number of XML tags.  

When retrieving a XML value, the default behaviour is to retrieve the `.text` value of the tag.  
If you wish to change this, to retrieve a tag containing many other tags, use `raw` key and set it to `false`.  
This will return you an object of type `xml.etree.Element`, you could later apply transformations on this object to alter,
 organize and retrieve the data.

**JSON**  
Use `index` key to retrieve a specific value from an array.  
Of course, it only works if the retrieved value is of type **array**.

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

## Exceptions
Fluxify has different Exception classes for different reasons
They reside in the **exceptions** sub-package ```fluxify.exceptions```

Class                                   | Arguments             | Description
----------------------------------------|-----------------------|-------------
**ArgumentNotFoundException**           | message               | This exception is raised whenever a argument is not found.
**InvalidArgumentException**            | message               | This exception is raised when a passed parameter/argument is invalid.
**ConditionNotFoundException**          | message               | This exception is raised when the "condition" key is not defined in the mapping.
**UnsupportedTransformerException**     | message               | This exception is raised when a transformer other than the ones defined above, is used.