'''
pytz setup script
'''

import pytz
import os
import os.path

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    # TODO: pickup all packages
    find_packages = lambda: ["pytz"]

me = 'Stuart Bishop'
memail = 'stuart@stuartbishop.net'
packages = find_packages()
resources = ['zone.tab', 'locales/pytz.pot']
new_resources = {}
for dirpath, dirnames, filenames in os.walk(os.path.join('pytz', 'zoneinfo')):
    # remove the 'pytz' part of the path
    resource_list = [f for f in filenames if os.path.splitext(f)[1] not in [".py", ".pyc"]]
    if resource_list:
        new_resources[dirpath.replace(os.path.sep, ".")] = resource_list
    basepath = dirpath.split(os.path.sep, 1)[1]
    resources.extend([os.path.join(basepath, filename)
                     for filename in filenames])
package_data = {'pytz': resources}
package_data.update(new_resources)

assert len(resources) > 10, 'zoneinfo files not found!'

setup(
    name='pytz',
    version=pytz.VERSION,
    zip_safe=True,
    description='World timezone definitions, modern and historical',
    long_description=open('README.txt', 'r').read(),
    author=me,
    author_email=memail,
    maintainer=me,
    maintainer_email=memail,
    url='http://pythonhosted.org/pytz',
    license='MIT',
    keywords=['timezone', 'tzinfo', 'datetime', 'olson', 'time'],
    packages=packages,
    package_data=package_data,
    download_url='https://pypi.org/project/pytz/',
    platforms=['Independent'],
    classifiers = [
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
