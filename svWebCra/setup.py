from setuptools import setup, find_packages

setup(
    name='svWebCra',
    version='0.1',
    packages=find_packages(),
    # package_data={'source': ['source/*']},
    include_package_data=True,
    install_requires=[
        'selenium',
        'openpyxl',
        'requests',
    ],
    author='xdsun777',
    author_email='charmgo@qq.com',
    description='pc',
    url='https://github.com/xdsun777',
)
