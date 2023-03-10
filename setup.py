from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in prpoerty_managment/__init__.py
from prpoerty_managment import __version__ as version

setup(
	name="prpoerty_managment",
	version=version,
	description="desc",
	author="y@gmail.com",
	author_email="y@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
