import json
from pathlib import Path

from pomodoro.config import Config, DEFAULT_CONFIG


def test_default_creation(tmp_path):
    cfg_path = tmp_path / "conf" / "config.json"
    c = Config(config_path=str(cfg_path))
    assert cfg_path.exists()
    assert c.get_focus_period() == DEFAULT_CONFIG["timer"]["focus_period_minutes"]
    assert c.get_rest_period() == DEFAULT_CONFIG["timer"]["rest_period_minutes"]


def test_ensure_defaults_on_partial_config(tmp_path):
    cfg_dir = tmp_path / "partial"
    cfg_dir.mkdir(parents=True, exist_ok=True)
    cfg_path = cfg_dir / "config.json"

    partial = {"timer": {"focus_period_minutes": 10, "rest_period_minutes": 2}}
    cfg_path.write_text(json.dumps(partial))

    c = Config(config_path=str(cfg_path))
    # Should retain custom values and fill in missing sections
    assert c.get_focus_period() == 10
    assert c.get_rest_period() == 2
    assert "sounds" in c.config and "focus_end" in c.config["sounds"]


def test_setters_persist_values(tmp_path):
    cfg_path = tmp_path / "persist" / "config.json"
    c = Config(config_path=str(cfg_path))
    c.set_focus_period(30)
    c.set_rest_period(7)

    # Re-load to ensure values persisted to disk
    c2 = Config(config_path=str(cfg_path))
    assert c2.get_focus_period() == 30
    assert c2.get_rest_period() == 7

