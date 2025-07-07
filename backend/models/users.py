"""Back-end users model for the expense tracker system"""

from dataclasses import dataclass
from enum import Enum
from typing import Union, Optional, List, Any


class UserRole(Enum):
    """Dedicated class for available user roles for the system."""
    ADMIN = "ADMIN"
    USER = "USER"
    VIEWER = "VIEWER"


@dataclass
class User:
    """Dedicated class to system user."""
    name: str
    role: UserRole = UserRole.VIEWER
    email: str
    password: str   #hashed and bstr methods processed in handler