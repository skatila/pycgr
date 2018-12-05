"""Helper functions for pycgr"""
import re


def slugify(value):
	"""Purge bad char from given string based on
	django's slugify (template/defaultfilters.py)
	"""
	#value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
	value = re.sub(r'[^\w\s-]', '', value).strip()
	value = re.sub(r'[-\s]+', '-', value)
	return value
