"""
permissions.py

This module contains custom Django REST Framework (DRF) permissions for the project.

Classes:
- IsAuthorOrReadOnly: Grants read-only access to all users and write access only to the author of the object.
- IsAdminOrReadOnly: Grants read-only access to all users and write access only to admin users.
"""

from typing import Any

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to allow authors of an object to edit it.
    All other users have read-only access.
    """

    def has_object_permission(self, request: Any, view: Any, obj: Any) -> bool:
        """
        Check if the request has the appropriate permissions for the object.

        Args:
            request (Any): The HTTP request object.
            view (Any): The view being accessed.
            obj (Any): The object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in SAFE_METHODS:
            return True
        return hasattr(obj, 'author') and obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to edit objects.
    All other users have read-only access.
    """

    def has_object_permission(self, request: Any, view: Any, obj: Any) -> bool:
        """
        Check if the request has the appropriate permissions for the object.

        Args:
            request (Any): The HTTP request object.
            view (Any): The view being accessed.
            obj (Any): The object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff