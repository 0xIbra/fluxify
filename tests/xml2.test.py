from fluxify import Mapper, LazyMapper
import yaml


with open('./fluxify/examples/xml2.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)


def callback(data):
    print('\n')
    print('1 : ', data[0])
    exit()


mapper = LazyMapper(_type='xml', save_unmatched=False)
mapper.set_callback(callback)
data = mapper.map('./fluxify/examples/agency-2348325.xml', Map, item_node='annonce')
