import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
                 name="nii2png",
                 version="0.2.7",
                 author="Alexander Laurence",
                 author_email="alexander.adamlaurence@gmail.com",
                 description="A lightweight neuroimaging .nii to .png converter",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/alexlaurence/NIfTI-Image-Converter",
                 packages=setuptools.find_packages(),
                 classifiers=[
                              "Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                              ],
                 )
