"""
	Let's set things up!!!
"""
from setuptools import setup
setup(
	name="pycgr",
	version="0.01",# Extract from git ?
	author="Sabin Katila",
	author_email="sabin@sabink.org",
	description="Create Chaos Game Representation from given fasta",
	license="GPLv3",
	url="www.sabink.org",
	#packages = find_packages(),
	packages=['pycgr'],
	install_requires=['biopython', 'matplotlib'],
	long_description="Chaos Game Representation of DNA sequence",
	classifiers=[
		"Development Status :: 0.01 - Alpha",
	],

)
