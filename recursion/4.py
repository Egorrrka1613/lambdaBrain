def recursion(inner_str: str, start_index, end_index) -> bool:
    if start_index >= end_index:
        return True
    if inner_str[start_index] != inner_str[end_index]:
        return False
    return recursion(inner_str, start_index + 1, end_index - 1)


def is_palindrome(out_str: str) -> bool:
    format_str = out_str.lower().replace(" ", "")
    return recursion(format_str, 0, len(format_str) - 1)


def test():
    assert is_palindrome("a") is True
    assert is_palindrome("aaaa") is True
    assert is_palindrome("aabaaa") is False
    assert is_palindrome("abc") is False
    assert is_palindrome("Я иду с мечем судия") is True
    assert is_palindrome("Я иду с меем судия") is True
    assert is_palindrome("Я иду с мечом судия") is False
