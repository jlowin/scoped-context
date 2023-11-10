import contextvars
from contextlib import contextmanager, asynccontextmanager

class ScopedContext:
    def __init__(self):
        self._context_storage = contextvars.ContextVar('scoped_context_storage', default={})

    def get(self, key, default=None):
        return self._context_storage.get().get(key, default)

    def set(self, **kwargs):
        ctx = self._context_storage.get()
        updated_ctx = {**ctx, **kwargs}
        self._context_storage.set(updated_ctx)

    @contextmanager
    def __call__(self, **kwargs):
        # Capture the current state
        current_context = self._context_storage.get().copy()
        # Update the context with new key-values
        self.set(**kwargs)
        try:
            yield
        finally:
            # Restore the previous state after the block exits
            self._context_storage.set(current_context)

    # Async contextmanager wrapper to utilize the same __call__ method
    @asynccontextmanager
    async def __aenter__(self, **kwargs):
        with self(**kwargs) as context:
            yield context

# The singleton that can be used across the application
scoped_context = ScopedContext()