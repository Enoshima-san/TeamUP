```python
"""
Module for authentication-related functionality.

This module provides an authentication router and a function to retrieve the current user.
"""

from ..di import get_current_user
from .auth import auth_router

__all__ = ["auth_router", "get_current_user"]
```