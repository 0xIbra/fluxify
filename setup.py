import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fluxify',
    version='0.0.1',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    description='A micro python package that can retrieve and flow control data from almost any type of file.',
    long_description=long_description,
    url='https://github.com/ibragim64/fluxify',
    packages=['fluxify'],
    install_requires=['pandas', 'PyYAML'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)