from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='behave-plain-color-formatter',
    version="0.0.1",
    packages=['behave_plain_color_formatter', ],
    url='https://github.com/msabramo/behave-plain-color-formatter',
    license='MIT',
    author='Marc Abramowitz',
    author_email='msabramo@gmail.com',
    description='Formatter for behave that uses color but not fancy terminal repositioning',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["behave>=1.2.5,<=1.3"],
    keywords=['testing', 'behave', 'teamcity', 'formatter', 'report'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities"
    ],
)
