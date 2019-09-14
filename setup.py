from setuptools import setup


with open("README.md") as f:
    readme = f.read()


setup(
    name="mktree",
    version="0.3.1",
    description="Simple tool for creating directory trees in one shot",
    long_description=readme,
    long_description_content_type='text/markdown',
    license="MIT",
    author="Giacomo Comitti",
    author_email="dev@gcomit.com",
    url="https://github.com/gcmt/mktree",
    scripts=["mktree"],
    data_files=[("man/man1", ["mktree.1"])],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
)
