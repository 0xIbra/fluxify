import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fluxify',
    version='0.0.1',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    description='A Python package that eases the process of retrieving, organizing and modifying data.',
    long_description=long_description,
    url='https://github.com/ibragim64/fluxify',
    packages=['fluxify', 'fluxify.handler', 'fluxify.helper', 'fluxify.transformers'],
    install_requires=['pandas', 'PyYAML', 'imperium'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)