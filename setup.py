import setuptools
from pkgUdit.version import __version__

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="pkgUdit",
    version=__version__,
    author="Udit Sharma",
    description="A sample package",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'pkgUdit': ['data/*.csv']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)