from setuptools import setup, find_packages

version = '0.0'

setup(name='GrokPaste',
      version=version,
      description="",
      long_description="""\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], 
      keywords="",
      author="",
      author_email="",
      url="",
      license="",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        # Add extra requirements here
                        'zc.catalog==1.2b',
                        'hurry.query',
                        'hurry.workflow',
                        ],
      entry_points="""
      # Add entry points here
      """,
      )