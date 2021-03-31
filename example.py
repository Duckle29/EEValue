#!/usr/bin/env python3

from EEValue import EEValue as EEV

supply_voltage = 5.0
forward_voltage = 2.35
current = 150E-3

R = EEV((supply_voltage - forward_voltage) / current)

print(R)

for series in [3, 6, 12, 24, 48, 96, 192]:
    print(f"R = {R.E(series):.2f}  # E{series}")
