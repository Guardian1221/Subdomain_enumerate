import socket
from unittest.mock import patch

from src import core


def test_resolve_subdomain_returns_ip():
    """
    Проверяет успешный DNS-резолв поддомена.
    """
    with patch("socket.gethostbyname", return_value="1.2.3.4"):
        assert core.resolve_subdomain("example.com", "api.") == "1.2.3.4"


def test_resolve_subdomain_returns_na_on_error():
    """
    Проверяет возврат N/A при недоступном DNS-имени.
    """
    with patch("socket.gethostbyname", side_effect=socket.gaierror):
        assert core.resolve_subdomain("example.com", "missing.") == "N/A"


def test_result_collection_builds_mapping_from_prefixes():
    """
    Проверяет результат только по переданным префиксам.
    """
    prefixes = ["api.", "www."]
    with patch("src.core.resolve_subdomain", side_effect=["1.1.1.1", "2.2.2.2"]):
        result = core.result_collection("example.com", prefixes)

    assert result == {"api.example.com": "1.1.1.1", "www.example.com": "2.2.2.2"}
