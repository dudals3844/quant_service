from setuptools import setup, find_packages


setup(
    name='quant_service',
    version='0.0.3',
    url='https://github.com/dudals3844/quant_service',
    author='ChoiYoungMin',
    author_email='dudals3844@gmail.com',
    description='Quant Service',
    packages=find_packages(exclude=['test']),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['pandas', 'pymysql', 'sqlalchemy'],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ]
)