ACTIVITY_OPEN = "<a class='minimal' href='/activities/"
ACTIVITY_CLOSE = "'>"


def get_activities_from_html(html: str) -> list:
    """
    Provided page source html, extract a list of activities on the page.
    """

    # intialize return list
    activities = []

    # if no activities on page, return the empty list
    if ACTIVITY_OPEN not in html or ACTIVITY_CLOSE not in html:
        return activities

    # otherwise extract and return
    for html_activity in html.split(ACTIVITY_OPEN)[1:]:
        activity_str = html_activity.split(ACTIVITY_CLOSE)[0]
        activities.append(activity_str)

    return activities


if __name__ == '__main__':

    # TEST

    html = """

<ul class='recent-activities'>
<li>
<span class="app-icon-wrapper  "><span class="app-icon icon-run icon-dark icon-sm">Run</span></span>
<a class='minimal' href='/activities/12429464990'>Lunch Run</a>
</li>
<li>
<span class="app-icon-wrapper  "><span class="app-icon icon-run icon-dark icon-sm">Run</span></span>
<a class='minimal' href='/activities/12419842701'>LR</a>
</li>
<li>
<span class="app-icon-wrapper  "><span class="app-icon icon-run icon-dark icon-sm">Run</span></span>
<a class='minimal' href='/activities/12410435514'>W: 4 x 5min on / 1min off</a>
</li>
<li>
<span class="app-icon-wrapper  "><span class="app-icon icon-run icon-dark icon-sm">Run</span></span>
<a class='minimal' href='/activities/12402849066'>Morning Run</a>
</li>
<li>
<span class="app-icon-wrapper  "><span class="app-icon icon-run icon-dark icon-sm">Run</span></span>
<a class='minimal' href='/activities/12402848492'>Morning Run</a>
</li>
</ul>
</div>
<div class='promo col-md-4 border-left js-channel-footer-center'>

"""

    activities = [
        '12429464990',
        '12419842701',
        '12410435514',
        '12402849066',
        '12402848492',
    ]

    assert get_activities_from_html(html) == activities

    print(f"bork, test(s) passed")
