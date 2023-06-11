from setuptools import setup, find_packages

from vila import constants

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
setup(
    name=constants.NAME,
    version=constants.VERSION,
    author='DancingSnow',
    author_email='1121149616@qq.com',
    description='A SDK for miyoushe vila',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=constants.GITHUB_URL,
    project_urls={
        'Bug Tracker': constants.GITHUB_URL + "/issues",
    },
    classifiers=[
        # https://pypi.org/classifiers/
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
