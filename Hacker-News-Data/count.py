def count_words():
    import read
    import collections
    df = read.load_data()
    s = ""
    for x in df["headline"]:
        s += str(x).lower() + " "
    strings = s.split(" ")
    common = collections.Counter(strings)
    common_100 = common.most_common(100)
    return common.most_common(100)

print(count_words())
    