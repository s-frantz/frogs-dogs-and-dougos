DATE_OPEN = "<time>"
DATE_CLOSE = "</time>"
WEEKDAY_OPEN = "M on "
WEEKDAY_CLOSE = ", "


def get_weekday_from_html(html: str) -> list:
    """
    Provided page source html, extract a list of mile splits
    """

    # if no activities on page, return the empty list
    if DATE_OPEN not in html or DATE_CLOSE not in html:
        return None

    # otherwise extract date
    date_html = html.split(DATE_OPEN)[1]
    date_str = date_html.split(DATE_CLOSE)[0].replace("\n", "").strip()

    # extract weekday from date
    weekday_html = date_str.split(WEEKDAY_OPEN)[1]
    weekday_str = weekday_html.split(WEEKDAY_CLOSE)[0]

    return weekday_str


if __name__ == '__main__':

    html = """

<div class="row no-margins activity-summary-container">
  <div class="spans8 activity-summary mt-md mb-md">
  <div class="details-container">
  <a class="avatar avatar-athlete" href="/athletes/64465567"><img alt="Silas" src="https://dgalywyr863hv.cloudfront.net/pictures/athletes/64465567/16175984/7/large.jpg">
  </a><div class="details">
  <time>
  11:32 AM on Sunday, September 15, 2024
  </time>
  <span class="location">San Luis Obispo County, California</span>
  <h1 class="text-title1 marginless activity-name">LR</h1>

"""

    assert get_weekday_from_html(html) == "Sunday", f"ribbit, test(s) failed"

    print(f"bork, test(s) passed!")
