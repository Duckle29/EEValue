#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from eevalue import EEValue as EEV  # noqa E402


def test_E_series():
    # These are hand-picked from the actual E series values, according to the selected mode
    series_values = {
        "round": [2.2, 3.3, 3.3, 3.0, 3.16, 3.09, 3.09],
        "floor": [2.2, 2.2, 2.7, 3.0, 3.01, 3.09, 3.09],
        "ceil": [4.7, 3.3, 3.3, 3.3, 3.16, 3.16, 3.12]
    }

    for idx, series in enumerate([3, 6, 12, 24, 48, 96, 192]):
        assert float(EEV(3.1, 2).E(series, 'round')) == series_values["round"][idx]
        assert float(EEV(3.1, 2).E(series, 'floor')) == series_values["floor"][idx]
        assert float(EEV(3.1, 2).E(series, 'ceil')) == series_values["ceil"][idx]


def test_si_prefixes():
    Si_prefixes = ('y', 'z', 'a', 'f', 'p', 'n', 'µ', 'm', '', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

    for factor in range(-24, 24 + 3, 3):
        assert str(EEV(3.1 * 10**factor, 2)) == "{:.2f} {}".format(3.1, Si_prefixes[factor // 3 + 8])

    assert str(EEV(3.1 * 10**-28, 5)) == "0.00031 y"
    assert str(EEV(3.1 * 10**28, 5)) == "31000.00000 Y"
