from fluxify.mapper import Mapper
import yaml, json

with open('../fluxify/examples/xml.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper()
data = mapper.map('../fluxify/examples/flux.xml', Map, Type='xml', item_node='person')
print(json.dumps(data))