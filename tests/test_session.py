from pathlib import Path

from pomodoro.session import SessionManager


def test_session_logging_and_count(tmp_path):
    log_path = tmp_path / "logs" / "sessions.log"
    sm = SessionManager(log_file=str(log_path))
    assert sm.get_session_count() == 0

    n1 = sm.log_session("Deep Work", success=True)
    assert n1 == 1
    assert log_path.exists()

    n2 = sm.log_session("Review", success=False)
    assert n2 == 2

    # New manager should read existing count from log
    sm2 = SessionManager(log_file=str(log_path))
    assert sm2.get_session_count() == 2


def test_daily_stats(tmp_path, monkeypatch):
    # Write two entries with today's date by using SessionManager
    log_path = tmp_path / "logs" / "sessions.log"
    sm = SessionManager(log_file=str(log_path))
    sm.log_session("A", success=True)
    sm.log_session("B", success=False)

    stats = sm.get_daily_stats()
    assert stats["count"] == 2
    # Focus areas include suffixed status; ensure entries exist
    assert any("A" in f for f in stats["focus_areas"]) or any("B" in f for f in stats["focus_areas"]) 

