import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xrimtf",
    version="0.0.1",
    author="Brandon Nelson and Andrew Vercnoke",
    author_email="nelson.brandon@mayo.edu, Vercnocke.Andrew@mayo.edu",
    description="Tools for calculating MTF from line profiles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://rohaslrailgit.mayo.edu/ctcic/mct-developement/xri-mtf",
    project_urls={
        "Bug Tracker": "https://rohaslrailgit.mayo.edu/ctcic/mct-developement/xri-mtf/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        'scipy',
        'pandas',
        'pyinstaller',
        'pytest',
        'Gooey',
        'numpy',
    ],
    entry_points={
    'console_scripts': ['mtf=xri_mtf.mtf:cli'],
    'gui_scripts': ['mtf_gui=xri_mtf.mtf:main']
    }
)