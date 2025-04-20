from setuptools import setup, find_packages

setup(
    name="crules",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0.0",
        "pyyaml>=6.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=4.0.0",
            "mypy>=0.900",
        ],
    },
    entry_points={
        "console_scripts": [
            "crules=cli.interface:main",
        ],
    },
    python_requires=">=3.9",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for efficient project rule management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/crules",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
) 