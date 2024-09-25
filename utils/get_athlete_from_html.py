ATHLETE_OPEN = '&quot;,&quot;ownerName&quot;:&quot;'
ATHLETE_CLOSE = '&quot;,&quot;ownerAvatarUrl&quot;:&quot;'


def get_athlete_from_html(html: str) -> list:
    """
    Provided page source html, extract a list of mile splits
    """

    # if no activities on page, return the empty list
    if ATHLETE_OPEN not in html or ATHLETE_CLOSE not in html:
        return None

    # otherwise extract and return
    athlete_html = html.split(ATHLETE_OPEN)[1]
    athlete_str = athlete_html.split(ATHLETE_CLOSE)[0]

    return athlete_str.replace("\n", "").strip()


# NOTE - tested in production from athlete page, via `html = driver.page_source`
