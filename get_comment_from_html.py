from utils.get_milesplits_from_html import get_milesplits_from_html
from utils.get_comment_from_milesplits import get_comment_from_milesplits


if __name__ == '__main__':

    with open("scratch/mark_002.html", "r") as f:
        html = f.read()

    milesplits = get_milesplits_from_html(html)
    comment = get_comment_from_milesplits(milesplits)

    print(comment)
