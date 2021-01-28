from setuptools import setup


setup(
    name="numerical_algorithms",
    version="1.0.0",
    url="https://github.com/gwyddie/numerical-algorithms",
    packages=["numerical_algorithms"],
    package_dir={"": "."},
    author="Daniel Omiya",
    author_email="danielomiya@gmail.com",
    description="A bunch of numerical algorithms",
    license="GPLv3",
    platforms=["darwin", "linux", "win32", "win64"],
    python_requires=">=3.6",
)
