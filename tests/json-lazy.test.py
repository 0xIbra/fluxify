from fluxify.lazy_mapper import LazyMapper
import yaml, json

with open('./fluxify/examples/json.yaml', 'r') as fh:
    jsonmap = yaml.load(fh.read(), Loader=yaml.FullLoader)


def test_function(results):
    print(results)


mapper = LazyMapper(_type=LazyMapper.JSON_FORMAT, error_tolerance=True, bulksize=20)
mapper.set_callback(test_function)

mapper.map('./fluxify/examples/flux-large.json', jsonmap)