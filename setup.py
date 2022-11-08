from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ileapp/__init__.py
from ileapp import __version__ as version

setup(
	name="ileapp",
	version=version,
	description="Application for registering and tracking owner devices",
	author="Technovalley",
	author_email="support@technovalley.co.ke",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
