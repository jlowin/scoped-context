# Scoped Context Package

`scoped_context` is a Python package that provides a robust context management solution for managing application-level context variables in a scoped and thread-safe manner. By leveraging the power of `contextvars`, this package allows you to set temporary modifications to the application context that are automatically reverted upon exiting the context block.

## Features

- **Scoped Modifications**: Changes to the context are only valid within the block where they are set, ensuring that modifications do not leak across different parts of your application.
- **Asynchronous Support**: Works seamlessly with asynchronous code, managing context for async coroutines just as easily as synchronous functions.
- **Thread-Safety**: Built on top of `contextvars`, making it inherently thread-safe and suitable for use in multithreaded applications.
- **Easy to Use**: The package provides a simple API with a clear and intuitive usage pattern.

## Installation

Install the `scoped_context` package using pip:

```
pip install scoped_context
```

## Quick Start

To use the `scoped_context`, simply import the `scoped_context` singleton from the package and use it within either a `with` statement or an `async with` statement depending on your use case:

```python
from scoped_context import scoped_context

# Synchronous usage
with scoped_context(key='value'):
    # Context is modified here
    ...

# Asynchronous usage
async with scoped_context(key='value'):
    # Context is modified here
    ...
```

## Example

The following example demonstrates how to use the `scoped_context` both synchronously and asynchronously to temporarily alter the application context:

Refer to the `scoped_context_examples/examples.py` file for detailed examples.

## Contributing

Contributions to the `scoped_context` package are welcome! Feel free to report any issues or open pull requests on GitHub:

[https://github.com/jlowin/scoped-context](https://github.com/jlowin/scoped-context)

## License

Distributed under the MIT License. See `LICENSE` file for more information.
