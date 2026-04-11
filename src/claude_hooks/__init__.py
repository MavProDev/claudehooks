"""claude-hooks: Add Claude as middleware to any Python app with a single decorator."""
from .router import HookRouter
from .context import HookContext
from .types import FallbackStrategy, HookConfig, HookStatus
from .providers.base import LLMProvider, LLMResponse
from .providers.claude import ClaudeProvider
from .exceptions import (
    HookError,
    HookTimeoutError,
    HookBudgetError,
    HookValidationError,
    HookProviderError,
)

__version__ = "0.1.0"

__all__ = [
    # Core
    "HookRouter",
    "HookContext",
    # Types
    "FallbackStrategy",
    "HookConfig",
    "HookStatus",
    # Providers
    "LLMProvider",
    "LLMResponse",
    "ClaudeProvider",
    # Exceptions
    "HookError",
    "HookTimeoutError",
    "HookBudgetError",
    "HookValidationError",
    "HookProviderError",
]
