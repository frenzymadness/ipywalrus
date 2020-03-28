from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ipywalrus',
      version='0.1',
      description=('IPython extension which allows assignment expressions (:=)',
                   'at the top level of an expression statement'),
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/frenzymadness/ipywalrus',
      author='Lumír Balhar',
      author_email='frenzy.madness@gmail.com',
      license='MIT',
      py_modules=['ipywalrus'],
      zip_safe=False,
      python_requires='>=3.8')
