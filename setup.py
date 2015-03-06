from setuptools import setup


readme = open('README.rst').read()

setup(
    name='venn-places',
    version='0.0.1',
    description='Get normalized place data from Foursquare, Yelp, Facebook, Google, and Factual.',
    long_description=readme,
    author='Bryon Meinka',
    author_email='b.meinka@gmail.com',
    url='http://github.com/vennhq/venn-places-python',
    packages=['venn'],
    install_requires=['requests >=2.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
