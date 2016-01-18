#!/usr/bin/env python3

import re

print("// auto-generated by timings.py from ../icefuzz/timings_*.txt")

def timings_to_c(chip, f):
    print("")
    print("double get_delay_%s(std::string cell_type, std::string in_port, std::string out_port)" % chip)
    print("{")

    in_cell = False

    for line in f:
        fields = line.split()
        if len(fields) == 0:
            continue

        if fields[0] == "CELL":
            if in_cell:
                print("  }")
            print("  if (cell_type == \"%s\") {" % fields[1])
            in_cell = True

        if fields[0] == "SETUP":
            inport = fields[1].split(":")[1]
            delay = max([0 if s == "*" else float(s) / 1000 for s in fields[3].split(":")])
            print("    if (in_port == \"%s\" && out_port == \"*setup*\") return %.5f;" % (inport, delay))

        if fields[0] == "IOPATH":
            if fields[1].startswith("posedge:") or fields[1].startswith("negedge:"):
                fields[1] = "*clkedge*"
            delay = max([0 if s == "*" else float(s) / 1000 for s in fields[3].split(":") + fields[4].split(":")])
            print("    if (in_port == \"%s\" && out_port == \"%s\") return %.5f;" % (fields[1], fields[2], delay))


    if in_cell:
        print("  }")
    print("  if (in_port == \"*clkedge*\"|| out_port == \"*setup*\") return 0;")
    print("  fprintf(stderr, \"Unable to resolve delay for path %s -> %s in cell type %s!\\n\", in_port.c_str(), out_port.c_str(), cell_type.c_str());")
    print("  exit(1);")
    print("}")

with open("../icefuzz/timings_1k.txt", "r") as f:
    timings_to_c("1k", f);

with open("../icefuzz/timings_8k.txt", "r") as f:
    timings_to_c("8k", f);

