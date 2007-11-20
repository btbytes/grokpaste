from setuptools import setup, find_packages

version = '0.1'

setup(name='GrokPaste',
      version=version,
      description="Pastebin Application using Grok",
      long_description="""\
      GrokPaste is a standalone application which implements a Pastebin application similar to one in http://dpaste.com
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], 
      keywords="grok, zope3, pastebin",
      author="Pradeep Kishore Gowda",
      author_email="pradeep@btbytes.com",
      url="http://www.btbytes.com",
      license="MIT",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        # Add extra requirements here
                        ],
      entry_points="""
      # Add entry points here
      """,
      )
