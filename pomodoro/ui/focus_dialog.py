"""Dialog for starting a focus session with optional duration overrides."""
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QDialogButtonBox,
)


class FocusSessionDialog(QDialog):
    """Dialog asking what to focus on and allows changing durations."""

    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config

        self.setWindowTitle("Start Focus Session")

        layout = QVBoxLayout()
        form = QFormLayout()

        self.focus_edit = QLineEdit()
        form.addRow("Focus on:", self.focus_edit)

        self.focus_length = QSpinBox()
        self.focus_length.setRange(1, 120)
        self.focus_length.setValue(self.config.get_focus_period())
        self.focus_length.setSuffix(" min")
        form.addRow("Focus length:", self.focus_length)

        self.rest_length = QSpinBox()
        self.rest_length.setRange(1, 60)
        self.rest_length.setValue(self.config.get_rest_period())
        self.rest_length.setSuffix(" min")
        form.addRow("Rest length:", self.rest_length)

        layout.addLayout(form)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def get_values(self):
        """Return entered focus text and durations."""
        return (
            self.focus_edit.text(),
            self.focus_length.value(),
            self.rest_length.value(),
        )

