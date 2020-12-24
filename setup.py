import os

from setuptools import setup, find_packages


def _process_requirements():
    try:
        packages = open('requirements.txt').read().strip().split('\n')
    except FileNotFoundError as e:
        return []
    requires = []
    for pkg in packages:
        if pkg.startswith('git+ssh'):
            return_code = os.system('pip install {}'.format(pkg))
            assert return_code == 0, 'error, status_code is: {}, exit!'.format(return_code)
        else:
            requires.append(pkg)
    return requires


setup(
    name='foo',
    version='1.0.0',
    author='brown',
    description="just a test",
    packages=find_packages(),
    install_requires=_process_requirements()
)
