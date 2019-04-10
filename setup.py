from setuptools import setup, find_packages

setup(
    name='uceasy',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'click',
        'pandas',
        'jinja2'
    ],
    entry_points='''
        [console_scripts]
        uceasy=cli.uceasy_cli:uceasy
    '''
)
