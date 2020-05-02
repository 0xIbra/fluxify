from fluxify.lazy_mapper import LazyMapper
import yaml

with open('./tests/examples/xml.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)


def callback(results):
    print(f'Count: {len(results)}', 'Result callback', results[0])

    exit()


mapper = LazyMapper(_type='xml')
mapper.set_callback(callback)
mapper.set_bulksize(200)

mapper.map('./tests/examples/flux-large.xml', Map, root_node='people', item_node='person')
