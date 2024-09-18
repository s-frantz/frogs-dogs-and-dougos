ATHLETE_OPEN = "<span class='athlete-name'>"
ATHLETE_CLOSE = "</span>"


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


if __name__ == '__main__':

    html = """

<li class='nav-item drop-down-menu user-menu accessible-nav-dropdown'>
<a class='nav-link selection accessible-nav-link' href='/athletes/64465567'>
<div class='avatar avatar-athlete'>
<img alt="Silas" class="avatar-img" src="https://dgalywyr863hv.cloudfront.net/pictures/athletes/64465567/16175984/7/medium.jpg" />
</div>
<span class='athlete-name'>
Silas Frantz
</span>
</a>
<button aria-haspopup class='selection nav-link accessible-nav-arrow' data-toggle='dropdown ' id='dashboard-dropdown-arrow' title='Expand profile menu'>
<span class="app-icon-wrapper  "><span class="app-icon icon-caret-down icon-dark"></span></span>
</button>
<ul class='options'>
<li class='featured'>
<link rel="preload" href="https://web-assets.strava.com/assets/federated/find-and-invite-friends/remoteEntry.js?t=2024-09-18T02:47:56+00:00" as="script">
<div data-is-published='' data-react-class='Microfrontend' data-react-props='{&quot;url&quot;:&quot;https://web-assets.strava.com/assets/federated/find-and-invite-friends/remoteEntry.js?t=2024-09-18T02:47:56+00:00&quot;,&quot;scope&quot;:&quot;strava_find_and_invite_friends&quot;,&quot;component&quot;:&quot;./FindAndInviteFriends&quot;,&quot;appContext&quot;:{&quot;source&quot;:&quot;header_menu&quot;,&quot;googleClientId&quot;:&quot;541588808765.apps.googleusercontent.com&quot;,&quot;fbAppId&quot;:284597785309,&quot;fbVersion&quot;:&quot;v7.0&quot;,&quot;currentAthlete&quot;:{&quot;email&quot;:&quot;silas.frantz@gmail.com&quot;,&quot;id&quot;:64465567},&quot;mocked&quot;:false,&quot;defaultTabIndex&quot;:0,&quot;locale&quot;:&quot;en-US&quot;},&quot;experiments&quot;:{}}'></div>

    """

    assert get_athlete_from_html(html) == "Silas Frantz", f"ribbit, test(s) failed"

    print(f"bork, test(s) passed!")