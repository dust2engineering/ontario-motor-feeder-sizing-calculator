# Ontario Motor Feeder & Disconnect Sizing Calculator (CEC Section 28)

Motor circuit sizing under the Canadian Electrical Code, Section 28: full-load currents from Table 44 (1–50 HP at 200/208/230/460/575 V), branch-circuit conductors at 125%, branch overcurrent devices from Table 29 with the correct round-down rule, disconnect sizing at 115%, and group feeder sizing under Rule 28-204.

**Live web tool:** https://dust2engineering.github.io/ontario-motor-feeder-sizing-calculator/web/

## How it works

- Single motor: enter HP and rated voltage — conductors at 125% of Table 44 FLC (Rule 28-106), overcurrent device at the Table 29 percentage for the device type (NTD fuse 300%, TD fuse 175%, inverse-time breaker 250%), rounded DOWN to a standard rating.
- Disconnect: an HP-rated motor-circuit switch, or a moulded-case switch/breaker rated at least 115% of FLC (Rules 28-602/28-604).
- Feeder mode: conductor ampacity = 125% of the largest motor + 100% of the rest; feeder overcurrent device ≤ largest motor's Table 29 maximum + the other motors' FLCs (Rule 28-204).
- Overloads are deliberately NOT calculated from Table 44 — Rule 28-306 sizes them from the nameplate (125% at SF ≥ 1.15, else 115%).

## Data in this repository

- `motor-sizing-data.json` — the Table 44 subset, Table 29 percentages, the 28-200(4) starting-relief ceilings and the rule summaries as machine-readable JSON.
- Provenance, stated plainly: CSA C22.1 is paywalled, so the FLC values are assembled from manufacturer reproductions of Table 44 (Schneider Electric digest; ABB catalogue; Moeller chart) that agree on every cell of the 1–50 HP subset, with Canadian 309A course cross-checks. Rules verified from IAEI Magazine's Canadian column and CSA Group checklists.

## Command line

```bash
python3 motor_sizing.py --hp 10 --volts 575 --device breaker
```

## Worked examples

- [example-single-motor.txt](examples/example-single-motor.txt)
- [example-feeder.txt](examples/example-feeder.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Electrical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
