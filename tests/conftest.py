"""Pytest fixtures for the Django project.

This module provides reusable pytest fixtures for testing purposes,
including user creation, article creation, category creation, and
client setup.
"""

from typing import Optional

import pytest
from django.contrib.auth.models import User
from django.test import Client
from myapp.models import Article, Category


@pytest.fixture
def create_user():
  """Fixture to create a user instance."""
  def _create_user(
    username: str = "testuser",
    email: str = "testuser@example.com",
    password: str = "password123",
    is_staff: bool = False,
    is_superuser: bool = False
  ) -> User:
    return User.objects.create_user(
      username=username,
      email=email,
      password=password,
      is_staff=is_staff,
      is_superuser=is_superuser
    )
  return _create_user


@pytest.fixture
def create_category():
    """Fixture to create a category instance."""
    def _create_category(
        name: str = "Default Category",
        description: Optional[str] = None
    ) -> Category:
        return Category.objects.create(
            name=name,
            description=description
        )
    return _create_category


@pytest.fixture
def create_article(create_user, create_category):
    """Fixture to create an article instance."""
    def _create_article(
        title: str = "Sample Article",
        content: str = "This is a sample article content.",
        author: Optional[User] = None,
        category: Optional[Category] = None,
        is_published: bool = True
    ) -> Article:
        if author is None:
            author = create_user()
        if category is None:
            category = create_category()
        return Article.objects.create(
            title=title,
            content=content,
            author=author,
            category=category,
            is_published=is_published
        )
    return _create_article


@pytest.fixture
def client():
    """Fixture to provide a Django test client."""
    return Client()