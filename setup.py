from setuptools import setup

with open("README.md", "r") as fp:
    LONG_DESCRIPTION = fp.read()

REQUIREMENTS = ["numpy", "pandas"]

setup(
    name="pyLHCO",
    version="0.1",
    description="LHCO reader for python.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Martin de los Rios",
    author_email=" martindelosrios13@gmail.com ",
    url=" https://github.com/martindelosrios/CADDENA",
    py_modules=["ez_setup"],
    packages=["dataset"],
    #    exclude_package_data={"": ["tests"]},
    include_package_data=True,  # < - - - - - -- solo si hay datos
    license="The MIT License",
    install_requires=REQUIREMENTS,
    keywords=["pyLHCO", "LHCO"],
    classifiers=[
        " Development Status :: 4 - Beta",
        " Intended Audience :: Education",
        " Intended Audience :: Science/Research",
        " License :: OSI Approved :: MIT License",
        " Operating System :: OS Independent",
        " Programming Language :: Python",
        " Topic :: Scientific/Engineering",
    ],
)
