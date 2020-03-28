import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fluxify',
    version='0.0.6',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    maintainer='Ibragim Abubakarov',
    maintainer_email='ibragim.ai95@gmail.com',
    description='A Python package that eases the process of retrieving, organizing and altering data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ibragim64/fluxify',
    packages=[
        'fluxify',
        'fluxify.handler',
        'fluxify.helper',
        'fluxify.transformers'
        ],
    install_requires=['pandas', 'PyYAML', 'imperium', 'ijson'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ]
)
