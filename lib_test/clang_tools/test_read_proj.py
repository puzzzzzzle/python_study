import json
from clang.cindex import *
from clang_tools.clang_utils import *

PROJ_PATH = "/root/core_develop/build_turbo_debug/compile_commands.json"
with open(PROJ_PATH, encoding="utf-8") as f:
    cmpInfos = json.load(f)

for item in cmpInfos:
    if item['file'].count("BlockToTowerModuleRegister.cpp") != 0:
        curr_info = item
        break

file = curr_info['file']
cmd_str = curr_info['command']  # type: str
cmd = [x for x in cmd_str.split(" ")]

index = Index.create()
tu = index.parse(None, cmd,
                 options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)

root_cursor = tu if isinstance(tu, Cursor) else tu.cursor


def test_find(path: str, target_kind=None, func=find_with_ns):
    print(f"finding {path} {target_kind}")
    for cursor in func([root_cursor], path, target_kind):  # type:Cursor
        print(f"\t - {fully_qualified(cursor)} {cursor.kind} {cursor.location} {cursor.linkage}")


def find_only(path: str, target_kind=None):
    print(f"finding {path} {target_kind}")
    cursors = find_with_ns([root_cursor], path, target_kind)
    assert len(cursors) == 1
    return cursors[0]


test_find("SWITCH_FEATURE", None, fuzzy_search)

test_find("BigWorld/BlockToTowerModule", CursorKind.CLASS_DECL)
test_find("BigWorld/BlockToTowerModuleRegister/RegisterAll", CursorKind.CXX_METHOD)

test_find("BigWorld/BlockToTowerModule")
test_find("BigWorld/BlockToTowerModuleRegister/RegisterAll")

ms = find_with_ns_single([root_cursor], "BigWorld/BlockToTowerModule/Init")

test_find("SWITCH_FEATURE", None, fuzzy_search)

pass
