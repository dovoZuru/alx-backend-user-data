#!/usr/bin/env python3
"""
3. Auth class
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Auth class.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public Method: require_auth
        """

        if not path or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        has_wildcard = any(x.endswith("*") for x in excluded_paths)
        if not has_wildcard:
            return path not in excluded_paths
        for e in excluded_paths:
            if path == e:
                return False
            if e.endswith("*"):
                if path.startswith(e[:-1]):
                    return False
        return True

    def authorization_header(self, request = None) -> str:
        """
        Public Method: authorization_header
        """

        if request:
            return request.headers.get("Authorization")

    def current_user(self, request = None) -> TypeVar('User'):
        """
        Public Method: curent_user
        """

        return None

    def session_cookie(self, request = None):
        """
        Method: session_cookie - returns a cookie value from a request.
        """

        if request:
            _my_session_id = getenv("SESSION_NAME")
            return request.cookies.get(_my_session_id, None)
