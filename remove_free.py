import json
import sys

def rem_frees(_code):
    for func_idx, func in enumerate(_code["functions"]):
        func_len = len(_code["functions"][func_idx]["instrs"])
        for instr_idx, instr in enumerate(reversed(_code["functions"][func_idx]["instrs"])):
            if "op" in instr:
                if instr["op"] == "free":
                    _code["functions"][func_idx]["instrs"].pop(func_len - 1 - instr_idx)
    return _code

if __name__ == "__main__":
    code = json.load(sys.stdin)
    code = rem_frees(code)
    json.dump(code, sys.stdout, indent=2, sort_keys=True)