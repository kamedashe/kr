import os
import pytest

if not os.environ.get("DISPLAY") and os.name != "nt":
    pytest.skip("Skipping GUI tests on headless", allow_module_level=True)
