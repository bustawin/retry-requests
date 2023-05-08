from pathlib import Path

from setuptools import find_packages, setup

test_requires = ["pytest"]

setup(
    name="retry-requests",
    version="2.0.0",
    url="https://github.com/bustawin/retry-requests",
    project_urls={
        "Documentation": "https://github.com/bustawin/retry-requests",
        "Code": "https://github.com/bustawin/retry-requests",
        "Issue tracker": "https://github.com/bustawin/retry-requests/issues",
    },
    license="GPLv3+",
    author="Xavier Bustamante Talavera",
    author_email="xavier@bustawin.com",
    description="Make requests's sessions auto-retry on failure.",
    packages=find_packages(),
    python_requires=">=3.6",
    long_description=Path("README.rst").read_text("utf8"),
    install_requires=["requests", "urllib3>=1.26"],
    extras_require={"test": test_requires},
    tests_require=test_requires,
    setup_requires=["pytest-runner"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
