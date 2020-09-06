import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jp2tiff", # Replace with your own username
    version="0.0.1",
    author="Saif Aati",
    author_email="saif@caltech.edu, saifaati@gmail.com",
    description="convert jp2 raster to tiff raster ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SaifAati/JP2toTiff.git",
    package_dir = {'':'jp2tiff'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE V3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    # install_requieres=["datetime","matplotlib","dateutil","geojson","requests"],
)