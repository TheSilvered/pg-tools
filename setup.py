from setuptools import setup

with open("README.md") as f:
    long_desc = f.read()

setup(
    name="pg-tools",
    version="0.1.0",
    description="Tools to make using pygame easier",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Davide Taffarello - TheSilvered",
    packages=["pgt"],
    license="MIT",
    install_requres=["pygame>=2.0.0"],
    keywords=["pygame", "game", "video-game"],
    url="https://github.com/TheSilvered/pg-tools",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ]
)
