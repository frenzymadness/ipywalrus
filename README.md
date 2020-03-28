# IPyWalrus

IPyWalrus is a simple IPython (Jupyter) extension which enables you to use the walrus
operator ([PEP 572 - Assignment Expressions](https://www.python.org/dev/peps/pep-0572/)) `:=`
for usual assignments in IPython or Jupyter.

This part of the PEP:

```
There are a few places where assignment expressions are not allowed, in order to avoid ambiguities or user confusion:

Unparenthesized assignment expressions are prohibited at the top level of an expression statement. Example:

y := f(x)  # INVALID
(y := f(x))  # Valid, though not recommended

This rule is included to simplify the choice for the user between an assignment statement and an assignment expression -- there is no syntactic position where both are valid.

```

is completely valid but my IPython sessions of Jupyter notebooks are full of cells like this one:

![images/standard.png](standard)

and because it does not work in pure Python

![images/error.png](error)

I've prepared a small extension which makes it work:

![images/ipywalrus.png](ipywalrus)

## Usage

Install the extension from pip or download the ipywalrus.py and put it somewhere in `PYTHONPATH`:

```
# pip install ipywalrus
```

and load it in IPython or Jupyter

```
%load_ext ipywalrus
```

## License

MIT
