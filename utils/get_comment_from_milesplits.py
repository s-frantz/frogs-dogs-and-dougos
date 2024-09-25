FROG = '🐸'
DOG = '🐕'


def _linreg(values):
    """
    https://stackoverflow.com/a/10048844

    for a list of values, e.g., [12, 34, 29, 38, 34, 51], return m, b from y = mx + b
    such that root mean square distance between trend line and original points is minimized
    """

    # X and Y are swapped from standard notation
    X = range(len(values))
    Y = values

    N = len(X)

    Sx = Sy = Sxx = Syy = Sxy = 0.0

    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y

    det = Sxx * N - Sx * Sx
    
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det


def get_comment_from_milesplits(milesplits: list) -> str:
    """
    Generates a comment from the input list of milesplits
    Frog miles are under 7 mins, dog miles are 7 mins and over
    """

    # get each milesplit as an integer (seconds)
    milesplits_s = [
        int(m) * 60 + int(s)
        for m, s in [
            m_s.split(":") for m_s in milesplits
        ]
    ]

    # run a regression on the time in seconds, get the slope
    m, _ = _linreg(milesplits_s)

    # get each milesplit as an emoji
    milesplits_emojis = [
        FROG if milesplit_s < 7 * 60 else DOG
        for milesplit_s in milesplits_s
    ]

    # initialize comment list
    comment_list = []    

    # make a final comment on the ratio of dogs to frogs
    if milesplits_emojis.count(FROG) >= milesplits_emojis.count(DOG):
        comment_list.append(f" -> today you lived as a {FROG}")
        if m <= 0:
            comment_list.append(f", but negative split by {abs(round(m, 1))}s per mile")
            comment_list.append(f". rather impressive, for a {FROG}")
        else:
            comment_list.append(f", and positive split by {abs(round(m, 1))}s per mile.")
            comment_list.append(" may future runs heal you, so help you dog.")
    else:
        comment_list.append(f" -> you have lived as a {DOG}")
        if m <= 0:
            comment_list.append(f". your negative splits of {abs(round(m, 1))}s per mile bring honor to the pound. WWWWWOOOF!")
        else:
            comment_list.append(f", although as a dying {DOG}, you positive split by {abs(round(m, 1))}s per mile")        

    # bundle up emojis and final comments
    final_comment = "".join(milesplits_emojis + comment_list)

    return final_comment


if __name__ == '__main__':

    milesplits = [
        "8:41",
        "8:20",
        "8:06",
        "8:30",
        "6:02",
        "5:59",
        "5:58",
        "5:45",
        "5:44",
        "5:28",
        "5:23",
        "5:13",
        "5:05",
        "5:12",
        "7:22",
    ]

    print(get_comment_from_milesplits(milesplits))

    print("")

    milesplits = [
        "6:30",
        "7:40",
        "7:05",
        "6:45",
        "8:50"
    ]

    print(get_comment_from_milesplits(milesplits))
