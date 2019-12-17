from mapper import Mapper
import yaml

yamlmapping = """
maker.original:
    col: 1
model.original:
    col: 2
generation.original:
    col: 3
gearbox.original:
    col: 4
"""

Map = yaml.load(yamlmapping, Loader=yaml.FullLoader)

mapper = Mapper()
data = mapper.map('./examples/flux1.csv', Map)