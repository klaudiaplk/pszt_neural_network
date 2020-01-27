from setuptools import setup, find_packages

setup(
    name='pszt_neural_network',
    version=1.0,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'neural_network = pszt_neural_network.main:main'
        ]
    },
)