ACTIVITY_OPEN = '&quot;,&quot;id&quot;:&quot;'
ACTIVITY_CLOSE = '&quot;,&quot;ownedByCurrentAthlete&quot;'


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


# NOTE - tested in production from athlete page, via `html = driver.page_source`
