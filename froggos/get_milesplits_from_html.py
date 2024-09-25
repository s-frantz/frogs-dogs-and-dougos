MILESPLIT_OPEN = '<td>'
MILESPLIT_CLOSE = ' <abbr class="unit short" title="minutes per mile">'


def get_milesplits_from_html(html: str) -> list:
    """
    Provided page source html, extract a list of mile splits
    """

    # intialize return list
    milesplits = []

    # if no activities on page, return the empty list
    if MILESPLIT_OPEN not in html or MILESPLIT_CLOSE not in html:
        return milesplits

    # otherwise extract and return
    for html_milesplit in html.split(MILESPLIT_OPEN)[1:]:
        if ':' not in html_milesplit:
            continue
        milesplit_str = html_milesplit.split(MILESPLIT_CLOSE)[0].replace('\n', '').replace(' ', '')
        milesplits.append(milesplit_str)

    return milesplits


if __name__ == '__main__':

    html = """

    <div class="mile-splits no-gap scrollable-table">
    <table class="dense hoverable">
        <thead>
        <tr>
            <th class="centered">Mile</th>
            <th>
            <span class="glossary-link run-version" data-glossary-term="definition-moving-time">
                Pace
            </span>
            </th>
            <th>Elev</th>
        </tr>
        </thead>
        <tbody id="contents" height="360px"><tr class=""><td class="centered">1</td>
    <td>
    8:41 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>10 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">2</td>
    <td>
    8:20 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>-13 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">3</td>
    <td>
    8:06 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>18 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">4</td>
    <td>
    8:30 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>2 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">5</td>
    <td>
    6:02 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>-9 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">6</td>
    <td>
    5:59 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>66 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">7</td>
    <td>
    5:58 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>73 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">8</td>
    <td>
    5:45 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>72 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">9</td>
    <td>
    5:44 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>100 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">10</td>
    <td>
    5:28 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>-84 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">11</td>
    <td>
    5:23 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>-64 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr class=""><td class="centered">12</td>
    <td>
    5:13 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>-89 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr><td class="centered">13</td>
    <td>
    5:05 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>-70 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr><td class="centered">14</td>
    <td>
    5:12 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>8 <abbr class="unit short" title="feet">ft</abbr></td></tr><tr><td class="centered">0.60</td>
    <td>
    7:22 <abbr class="unit short" title="minutes per mile">/mi</abbr>
    </td>
    <td>-19 <abbr class="unit short" title="feet">ft</abbr></td></tr></tbody>
    </table>
    </div>

    """

    assert get_milesplits_from_html(html) == [
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
    ], f"ribbit, test(s) failed"

    print(f"bork, test(s) passed!")
