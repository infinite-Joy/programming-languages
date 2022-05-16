def count_and_say(n):
    if n == 1:
        return "1"
    if n == 2:
        return "21"

    curr = "21"
    for i in range(3, n):
        build = []
        prev = curr[0]
        count = 1
        for ch in curr[1:]:
            # print(ch, prev)
            if ch == prev:
                count += 1
            else:
                build.append(str(count))
                build.append(str(prev))
                count = 1
                prev = ch
        # print(build)
        build.append(str(count))
        build.append(str(ch))
        curr = "".join(build)
        build = []
        # print(curr)
    
    return curr


print(count_and_say(4))