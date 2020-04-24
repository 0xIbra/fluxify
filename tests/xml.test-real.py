from fluxify.mapper import Mapper
import yaml, json

with open('./fluxify/examples/xml.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper(_type='xml', save_unmatched=False)
data = mapper.map('./fluxify/examples/agency-2348325.xml', Map, item_node='annonce')

print(data[0])

