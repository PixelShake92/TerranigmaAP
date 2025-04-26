from setuptools import setup, find_packages

setup(
    name="terranigma-randomizer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'terranigma-randomizer=terranigma_randomizer.__main__:main',
        ],
        'gui_scripts': [
            'terranigma-randomizer-gui=terranigma_randomizer.gui:main',
        ],
    },
    description="A randomizer for the SNES game Terranigma",
    author="Terranigma Randomizer Team",
    author_email="",
    url="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)