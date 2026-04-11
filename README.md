# claude-hooks

Add Claude as middleware to any Python app with a single decorator.

## Installation

```bash
pip install claude-hooks
```

## Quick Start

```python
from claude_hooks import claude_middleware

@claude_middleware
def my_function(input_data):
    return process(input_data)
```

## Documentation

See [docs/](docs/) for full documentation.

## License

MIT License - Copyright (c) 2026 MavPro Group LLC
