from setuptools import setup, find_packages
from xstatic.pkg import dagre_d3 as xs

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page.
long_description = open('README.rst').read()

setup(
    name=xs.PACKAGE_NAME,
    version=xs.PACKAGE_VERSION,
    description=xs.DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=xs.CLASSIFIERS,
    keywords=xs.KEYWORDS,
    maintainer=xs.MAINTAINER,
    maintainer_email=xs.MAINTAINER_EMAIL,
    license=xs.LICENSE,
    url=xs.HOMEPAGE,
    platforms=xs.PLATFORMS,
    packages=find_packages(),
    namespace_packages=['xstatic', 'xstatic.pkg'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
