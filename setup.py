from setuptools import setup
from Cython.Build import cythonize
from setuptools import Extension


extensions = [
    Extension(
        "*",
        ["*.pyx"],
        extra_compile_args=["-std=c++17"],
    ),
]

setup(
    name='reproduce memleaks',
    ext_modules=cythonize("req.pyx", compiler_directives={"embedsignature": True}),
    zip_safe=False,
)


