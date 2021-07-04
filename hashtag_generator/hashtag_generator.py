def generate_hashtag(s):
    # "This is super awesome!" -> "#ThisIsSuperAwesome!"
    res = "#" + "".join([i.capitalize() for i in s.split()])
    return res if 1 < len(res) < 140 else False