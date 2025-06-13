from setuptools import setup, find_packages
import os, sys


def readme():
    with open("README.rst") as f:
        return f.read()

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "isochrones", "version.py")
    with open(version_file) as f:
        code = compile(f.read(), version_file, "exec")
        version_ns = {}
        exec(code, version_ns)
        return version_ns["__version__"]

version = get_version()


# Publish the library to PyPI.
if "publish" in sys.argv[-1]:
    os.system("python setup.py sdist upload")
    sys.exit()

# Push a new tag to GitHub.
if "tag" in sys.argv:
    os.system("git tag -a {0} -m 'version {0}'".format(version))
    os.system("git push --tags")
    sys.exit()

setup(
    name="isochrones",
    version=version,
    description="Defines objects for interpolating stellar model grids.",
    long_description=readme(),
    author="Timothy D. Morton",
    author_email="tim.morton@gmail.com",
    url="https://github.com/timothydmorton/isochrones",
    packages=find_packages(),
    package_data={"isochrones": ["data/*", "tests/star*/*.ini"]},
    scripts=[
        "scripts/starfit",
        "scripts/batch_starfit",
        "scripts/starmodel-select",
        "scripts/starfit-summarize",
        "scripts/isochrones-dartmouth_write_tri",
        "scripts/mist-initialize.py",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    install_requires=[
        "pandas>=0.14",
        "astropy>=0.3",
        "emcee>=2.0",
        "numpy>=1.9",
        "tables>=3.0",
        "scipy>=0.19",
        "asciitree",
        "corner",
        "astroquery",
        #"configobj",
        "tqdm",
    ],
    zip_safe=False,
)
