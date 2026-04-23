import argparse
import json

from src.core import DOMAIN_PREFIXES, result_collection


def build_parser() -> argparse.ArgumentParser:
    """
    Builds an argument parser for the CLI.

    Returns:
        argparse.ArgumentParser: The argument parser.
    """
    parser = argparse.ArgumentParser(description="Subdomain enumerates.")
    parser.add_argument("domain", type=str, help="Строка-домен")
    parser.add_argument("-j", "--json", dest="json", action="store_true", help="вывод в json формате")
    parser.add_argument("-f", "--file", dest="file", action="store_true", help="вывод в файл")
    return parser


def render_output(domain: str, as_json: bool) -> str:
    result = result_collection(domain, DOMAIN_PREFIXES)
    if as_json:
        return json.dumps(result, ensure_ascii=False, indent=2)
    return "\n".join(f"{key}: {value}" for key, value in result.items())
