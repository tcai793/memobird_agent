from setuptools import setup
import memobird_agent

setup(
    name='memobird_agent',
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
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Printing',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='print memobird printer',
    zip_safe=False)
