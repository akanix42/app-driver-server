from setuptools import setup

setup(name='appdriverserver',
      version='0.1',
      description='Server for communicating with app driver clients',
      url='http://github.com/nathantreid/app-driver-server',
      author='Nathan Reid',
      author_email='nathan-code@nathantreid.com',
      license='MIT',
      packages=['autobahn'],
      install_requires=[
          'autobahn', 'twisted'
      ],
      zip_safe=False)