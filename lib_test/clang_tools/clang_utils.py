from clang.cindex import CursorKind


def fully_qualified(c):
    """
    获取打印用的完整路径
    :param c:
    :return:
    """
    if c is None:
        return ''
    elif c.kind == CursorKind.TRANSLATION_UNIT:
        return ''
    else:
        res = fully_qualified(c.semantic_parent)
        if res != '':
            return res + '::' + c.spelling
    return c.spelling


def find_in_cursors(cursors, spelling: str, kinds=None):
    """
    在给出的游标的children中找符合目标spelling和kinds的子游标, 如果kinds为None, 则不判断类型
    :param kinds:
    :param cursors:
    :param spelling:
    :return:
    """
    result = []
    for curr_cursor in cursors:
        for child_cursor in curr_cursor.get_children():  # type:
            # if spelling == child_cursor.spelling:
            #     print(f"same name {fully_qualified(child_cursor)} {child_cursor.kind}")
            if kinds is not None and child_cursor.kind not in kinds:
                continue
            if spelling == child_cursor.spelling:
                result.append(child_cursor)
    return result


def find_with_ns(cursors, path: str, target_kind=None):
    """

    按照指定的命名空间查找目标游标
    eg:
        find_with_ns([root_cursor], "ns1::ns2::class_def", CursorKind.CLASS_DECL)
        find_with_ns([root_cursor], "ns1::ns2::class_def::func_def", CursorKind.CXX_METHOD)

    :param cursors:
    :param path:
    :param target_kind:
    :return:
    """
    name = path.strip().split("/")
    spelling = name[len(name) - 1]
    ns = name[:len(name) - 1]
    possible_ns = cursors
    if target_kind is None:
        kinds = None
    else:
        kinds = [target_kind]
    for cns in ns:
        possible_ns = find_in_cursors(possible_ns, cns,
                                      [CursorKind.NAMESPACE, CursorKind.CLASS_DECL, CursorKind.STRUCT_DECL])
    return find_in_cursors(possible_ns, spelling, kinds)


def find_with_ns_single(cursors, path: str, target_kind=None):
    """
    查找只有一个游标的简化调用
    :param cursors:
    :param path:
    :param target_kind:
    :return:
    """
    find_cursors = find_with_ns(cursors, path, target_kind)
    if len(find_cursors) != 1:
        raise Exception(f"find num != 1 {path} {len(find_cursors)}")
    return find_cursors[0]


def fuzzy_search(cursors, spelling, kinds=None):
    result = []
    for curr_cursor in cursors:
        for child_cursor in curr_cursor.get_children():  # type:
            if kinds is not None and child_cursor.kind not in kinds:
                continue
            if spelling == child_cursor.spelling:
                result.append(child_cursor)
    return result


def fuzzy_match(cursors, spelling, kinds=None):
    result = []
    for curr_cursor in cursors:
        for child_cursor in curr_cursor.get_children():  # type:
            if kinds is not None and child_cursor.kind not in kinds:
                continue
            if spelling in child_cursor.spelling:
                result.append(child_cursor)
    return result
