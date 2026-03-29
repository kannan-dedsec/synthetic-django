```markdown
# Django Project Coding Guidelines

This document outlines coding guidelines for maintaining clean, consistent, and readable code in Django projects.

---

## 1. Code Style

- Follow **PEP 8** for Python code style.
- Use 4 spaces per indentation level (no tabs).
- Limit all lines to a maximum of **79 characters**.
- Use blank lines to separate logical sections of code:
  - 2 blank lines before class definitions.
  - 1 blank line between methods within a class.
- Use single quotes (`'`) or double quotes (`"`) consistently for strings. Pick one style and stick with it throughout the project.
- Use f-strings (`f"..."`) for string interpolation, unless the string is static.

---

## 2. Import Organization

- Organize imports into three sections, separated by a blank line:
  1. **Standard library imports** (e.g., `import os`).
  2. **Third-party imports** (e.g., `from django.db import models`).
  3. **Local application imports** (e.g., `from .models import MyModel`).
- Within each section, sort imports alphabetically.
- Use absolute imports unless relative imports are more appropriate for local modules.
- Avoid wildcard imports (`from module import *`).

Example:
```python
import os
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from myapp.models import CustomModel
```

---

## 3. Naming Conventions

- Use **snake_case** for variables, functions, and method names.
- Use **PascalCase** for class names.
- Use **UPPER_SNAKE_CASE** for constants.
- Use singular names for models (e.g., `User`, `Order`).
- Use descriptive names for variables and methods. Avoid single-letter names except for counters or indices (e.g., `i`, `j`).
- Prefix private methods or variables with a single underscore (e.g., `_private_method`).

---

## 4. Documentation

- Use **docstrings** for all public modules, classes, and methods.
- Follow the **Google-style docstring** format for clarity.

Example:
```python
def create_user(username: str, email: str) -> User:
    """
    Create and return a new user.

    Args:
        username (str): The username for the new user.
        email (str): The email address for the new user.

    Returns:
        User: The created user instance.
    """
    pass
```

- Use comments sparingly and only when the code's intent is not obvious.

---

## 5. Common Pitfalls

### Avoid Mutable Defaults
- Never use mutable default arguments (e.g., lists, dictionaries) in function definitions. Use `None` instead and initialize inside the function.

Bad:
```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Good:
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Query Performance
- Use `select_related` and `prefetch_related` to optimize database queries and avoid the "N+1 query problem."
- Avoid making queries inside loops.

### Avoid Hardcoding
- Use Django's settings for configurable values (e.g., `settings.MEDIA_URL`).
- Use `reverse()` or `reverse_lazy()` for URL resolution instead of hardcoding URLs.

---

## 6. Indentation Rules

- Use 4 spaces for all indentation.
- Align wrapped lines with the opening delimiter for better readability.

Example:
```python
queryset = MyModel.objects.filter(
    field_one=value_one,
    field_two=value_two,
).order_by('-created_at')
```

- For function arguments that span multiple lines, use hanging indents:

Example:
```python
def my_function(
    arg1: str,
    arg2: int,
    arg3: Optional[bool] = None,
) -> None:
    pass
```

---

## 7. Testing

- Write unit tests for all critical functionality.
- Use Django's built-in `TestCase` for testing models, views, and forms.
- Follow the **Arrange-Act-Assert (AAA)** pattern in test methods.

Example:
```python
def test_user_creation(self):
    # Arrange
    username = "testuser"
    email = "test@example.com"

    # Act
    user = User.objects.create(username=username, email=email)

    # Assert
    self.assertEqual(user.username, username)
    self.assertEqual(user.email, email)
```

---

By following these guidelines, we ensure our Django codebase remains clean, maintainable, and consistent.
```