import platform
import sys
from pathlib import Path

from setuptools import find_packages, setup


def read_version(fname="moonshine/version.py"):
    ns = {}
    exec(compile(open(fname, encoding="utf-8").read(), fname, "exec"), ns)
    return ns["__version__"]

setup(
    name="useful-moonshine",
    py_modules=["moonshine"],
    version=read_version(),
    description="Speech Recognition for Live Transcription and Voice Commands",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires=">=3.8",
    author="Useful Sensors",
    url="https://github.com/usefulesensors/moonshine",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        line.strip()
        for line in Path(__file__).with_name("requirements.txt").open()
        if line.strip() and not line.startswith("#")
    ],
    extras_require={
        "tensorflow": ["tensorflow==2.17.0"],
        "jax": ["jax==0.4.34", "keras==3.6.0"],
        "jax-cuda": ["jax[cuda12]", "keras==3.6.0"],
    },
    include_package_data=True,
)
