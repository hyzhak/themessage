from setuptools import find_packages, setup

setup(
    name='themessage',
    version='0.1',
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
        themessage=themessage.main:cli
    ''',
)
