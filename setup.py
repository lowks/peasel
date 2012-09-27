import os.path
from setuptools import Extension, setup

try:
    from Cython.Distutils import build_ext
    has_cython = True
except ImportError:
    has_cython = False

compile_args = ['-std=gnu99', '-O3', '-fomit-frame-pointer',
                '-malign-double', '-fstrict-aliasing', '-msse2']

easel_c_src = [ 'easel.c', 'esl_alphabet.c', 'esl_sqio.c', 'esl_sqio_ascii.c',
'esl_sq.c', 'esl_msa.c', 'esl_sqio_ncbi.c', 'esl_wuss.c', 'esl_keyhash.c',
'esl_vectorops.c', 'esl_ssi.c', 'esl_stack.c', 'esl_random.c']
easel_c_src = [os.path.join('easel-src', i) for i in easel_c_src]
easel_c_src.sort()

if has_cython:
    extra = dict(ext_modules=[
        Extension("peasel.ceasel", ["peasel/easel.pyx"] + easel_c_src,
            include_dirs=['easel-src', 'peasel'],
            extra_compile_args=compile_args,
            language="c",),
        ], cmdclass={'build_ext': build_ext})
else:
    extra = dict(ext_modules=[
        Extension("peasel.ceasel", ["peasel/easel.c"] + easel_c_src,
            include_dirs=['easel-src', 'peasel'],
            extra_compile_args=compile_args,
            language="c",),
        ])


setup(
    name='peasel',
    packages=['peasel', 'peasel.test'],
    test_suite='peasel.test.suite',
    version='0.1.0',
    **extra)