from setuptools import find_namespace_packages, setup

test_packages = ["pytest==7.1.2", "pytest-cov==2.10.1", "great-expectations==0.15.15"]

setup(
    name="py-projext",
    version=0.1,
    description="testing github workflows",
    author="Ram Chander",
    author_email="ram.chander@capillarytech.com",
    python_requires=">=3.7",
    extras_require={
        "test": test_packages,
    },
)