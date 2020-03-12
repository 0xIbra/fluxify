from fluxify import LazyMapper
import yaml, json

with open('./fluxify/examples/json.yaml', 'r') as fh:
    jsonmap = yaml.load(fh.read(), Loader=yaml.FullLoader)


def test_function(results):
    print('COUNT: {}'.format(str(len(results))))
    js = json.dumps(results)
    with open('output.json', 'w') as fh:
        fh.write(js)

    print(js)
    exit()


mapper = LazyMapper(_type=LazyMapper.JSON_FORMAT, error_tolerance=True, bulksize=30)
mapper.set_callback(test_function)

mapper.map('./fluxify/examples/flux-large.json', jsonmap)