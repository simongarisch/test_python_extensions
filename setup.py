"""
A .pyx file is compiled by Cython to a .c file, containing the code of a Python extension module.
The .c file is compiled by a C compiler to a .so file (or .pyd on Windows) which can be import-ed directly into a Python session.

python setup.py build_ext --inplace
python setup.py install

There is also a way to run the build_ext --inplace automatically on install
-> you need this build_py class
-> a setup.cfg file that defaults inplace = True
"""
from setuptools import setup, find_packages
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext 

"""
from setuptools.command.build_py import build_py as _build_py


class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()
"""

extensions = cythonize([
    Extension(
        name="test_python_extensions.cyadd",
        sources = ["test_python_extensions/cyadd.pyx"],
    ),
])

setup(
    name="test_python_extensions",
    version="0.0.1",
    packages=find_packages(),
    ext_modules=extensions,
    install_requires=["Cython==0.29.14"],
    cmdclass = {"build_ext" : build_ext},
)
