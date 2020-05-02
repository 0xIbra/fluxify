from fluxify.mapper import Mapper
import yaml

with open('./tests/examples/xml.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper(_type='xml', save_unmatched=False)
data = mapper.map('./tests/examples/flux.xml', Map, item_node='person')
print('DATA : ', data)
print('\n')
print('STATS : ', mapper.get_stats())
