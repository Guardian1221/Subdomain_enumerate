import json
import sys
from unittest.mock import patch

import main as app_main
from src import cli


def test_render_output_as_text():
    """
    Проверяет текстовый формат вывода CLI.
    """
    fake_data = {"api.example.com": "1.2.3.4"}
    with patch("src.cli.result_collection", return_value=fake_data):
        output = cli.render_output("example.com", as_json=False)

    assert output == "api.example.com: 1.2.3.4"


def test_render_output_as_json():
    """
    Проверяет JSON-формат вывода CLI.
    """
    fake_data = {"api.example.com": "N/A"}
    with patch("src.cli.result_collection", return_value=fake_data):
        output = cli.render_output("example.com", as_json=True)

    assert json.loads(output) == fake_data


def test_main_writes_json_file(monkeypatch, tmp_path, capsys):
    """Проверяет запись результата в файл при флаге --file.

    Args:
        monkeypatch: Фикстура pytest для подмены окружения.
        tmp_path: Временная директория для файлов теста.
        capsys: Фикстура для захвата stdout/stderr.
    """

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["main.py", "example.com", "--json", "--file"])

    with patch("main.render_output", return_value='{"api.example.com": "1.2.3.4"}'):
        app_main.main()

    stdout = capsys.readouterr().out
    output_path = tmp_path / "example.com_result.json"
    assert output_path.exists()
    assert json.loads(output_path.read_text(encoding="utf-8")) == {"api.example.com": "1.2.3.4"}
    assert json.loads(stdout) == {"api.example.com": "1.2.3.4"}
