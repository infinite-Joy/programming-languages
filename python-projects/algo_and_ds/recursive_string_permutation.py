def rec_permute(so_far, rest):
    """Recursively permute

    Args:
        param so_far:gs
    :rest: TODO
    :returns: TODO

    """
    if rest == "":
        print(so_far)
    else:
        for i in range(len(rest)):
            next_char = so_far + rest[i]
            remaining = rest[:i] + rest[i+1:]
            rec_permute(next_char, remaining)


def list_permutations(s):
    rec_permute("", s)

print(list_permutations("ab"))
print(list_permutations("abc"))
