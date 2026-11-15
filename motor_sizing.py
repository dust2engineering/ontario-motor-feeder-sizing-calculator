#!/usr/bin/env python3
"""Motor branch-circuit and feeder sizing (CEC Section 28, Table 44 / Table 29).
Single motor:
  python3 motor_sizing.py --hp 10 --volts 575 --device breaker
Feeder for a group (repeat --hp/--volts pairs as --motors HP@V,HP@V):
  python3 motor_sizing.py --motors 10@575,5@575,5@575 --device td-fuse
--device: ntd-fuse (300%), td-fuse (175%), breaker (250%)
"""
import argparse
FLC = {1:{200:4.8,208:4.6,230:4.2,460:2.1,575:1.7},1.5:{200:6.9,208:6.6,230:6.0,460:3.0,575:2.4},2:{200:7.8,208:7.5,230:6.8,460:3.4,575:2.7},3:{200:11.0,208:10.6,230:9.6,460:4.8,575:3.9},5:{200:17.5,208:16.7,230:15.2,460:7.6,575:6.1},7.5:{200:25.3,208:24.2,230:22,460:11,575:9},10:{200:32.2,208:30.8,230:28,460:14,575:11},15:{200:48.3,208:46.2,230:42,460:21,575:17},20:{200:62.1,208:59.4,230:54,460:27,575:22},25:{200:78.2,208:74.8,230:68,460:34,575:27},30:{200:92,208:88,230:80,460:40,575:32},40:{200:120,208:114,230:104,460:52,575:41},50:{200:150,208:143,230:130,460:65,575:52}}
PCT = {"ntd-fuse": 300, "td-fuse": 175, "breaker": 250}
STD = [15,20,25,30,35,40,45,50,60,70,80,90,100,110,125,150,175,200,225,250,300,350,400,450,500,600]
def down(x):
    ok = [s for s in STD if s <= x]; return ok[-1] if ok else None
def up(x):
    ok = [s for s in STD if s >= x]; return ok[0] if ok else None
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hp", type=float); ap.add_argument("--volts", type=int)
    ap.add_argument("--motors", help="comma list HP@VOLTS, e.g. 10@575,5@575")
    ap.add_argument("--device", choices=list(PCT), default="breaker")
    a = ap.parse_args()
    pct = PCT[a.device]
    if a.motors:
        flcs = []
        for part in a.motors.split(","):
            hp, v = part.split("@"); flcs.append(FLC[float(hp)][int(v)])
        largest = max(flcs); others = sum(flcs) - largest
        print(f"Motor FLCs: {flcs} A (Table 44)")
        print(f"Feeder conductors: min ampacity {largest*1.25 + others:.1f} A (125% of largest {largest} A + 100% of others {others:g} A)")
        mx = largest * pct / 100 + others
        print(f"Feeder overcurrent device: max {mx:.1f} A -> standard size {down(mx)} A (Rule 28-204, {pct}% of largest + sum of others)")
        return
    flc = FLC[a.hp][a.volts]
    print(f"Full-load current (Table 44): {flc} A")
    print(f"Branch conductors: min ampacity {flc*1.25:.1f} A (125% x FLC, Rule 28-106)")
    mx = flc * pct / 100
    print(f"Branch overcurrent device: max {mx:.1f} A ({pct}% x FLC, Table 29) -> standard size {down(mx)} A (round DOWN)")
    print(f"Disconnecting means: HP-rated switch >= {a.hp:g} HP, or switch/breaker rated >= {flc*1.15:.1f} A (115% x FLC) -> standard size {up(flc*1.15)} A")
    print("Overloads are sized from the motor nameplate (Rule 28-306): 125% if service factor >= 1.15, else 115%.")
if __name__ == "__main__":
    main()
