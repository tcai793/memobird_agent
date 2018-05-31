from setuptools import setup
import memobird_agent

setup(name='memobird_agent',
      version=memobird_agent.__version__,
      description='Print document on memobird from python using official API',
      url='http://github.com/tcai793/memobird_agent',
      author='Tong Cai',
      author_email='tong.cai.793@outlook.com',
      license='MIT',
      packages=['memobird_agent'],
      install_requires=[
          'pillow',
          'requests',
          'pycryptodome',
          'pillow'
      ],
      zip_safe=False)
