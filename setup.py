# To upload to PyPi run python setup.py sdist upload -r pypi
from distutils.core import setup

setup(
    name='fibonoxy',
    version='0.0.1',
    author='Matthew Robinson',
    author_email='mthw.wm.robinson@gmail.com',
    packages=['fibonoxy'],
    url='https://github.com/MthwRobinson/fibonoxy',
    description='build a herd of oxen that grows according to a fibonocci seq',
    entry_points = {
        'console_scripts' : ['fibonoxy=fibonoxy.__main__:main']
    }
)
