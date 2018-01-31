from setuptools import find_packages, setup

version = 'unknown'
with open('./themessage/version.txt') as f:
    version = f.read()

setup(
    name='themessage',
    version=version,
    py_modules=find_packages(),
    install_requires=[
        'Click==6.7',
        'medium==0.3.0',
        'PyJWT==1.5.3',
        'pytest==3.3.2',
        'pytest-cov==2.5.1',
        'requests==2.18.4',
    ],
    entry_points='''
        [console_scripts]
        themessage=themessage.cli:cli
    ''',
)
