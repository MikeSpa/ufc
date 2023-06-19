import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


def get_event_urls():
    url = "http://ufcstats.com/statistics/events/completed?page=all"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    event_links = [a["href"] for a in soup.select("td.b-statistics__table-col a")]
    return event_links[1:]  # the first link is the next event


def scrape_fight_data(event_url):
    response = requests.get(event_url)
    soup = BeautifulSoup(response.content, "html.parser")
    fights = []

    event_name = soup.find("h2", class_="b-content__title").text.strip()
    event_date = (
        soup.find("li", class_="b-list__box-list-item")
        .text.strip()
        .split("\n")[-1]
        .strip()
    )

    fight_table = soup.find("table", class_="b-fight-details__table")
    rows = fight_table.find_all("tr", class_="b-fight-details__table-row")[1:]

    # each row is a fight
    for row in rows:
        cols = row.find_all("td", recursive=False)
        result = cols[0].find("i", class_="b-flag__inner").text.strip()
        result = " ".join(result.split())
        fighters = cols[1].find_all("a")
        fighter1 = fighters[0].text.strip()
        fighter2 = fighters[1].text.strip()

        kd = cols[2].text.strip().replace("\n", "")
        kd_f1 = kd.split(" ")[0]
        kd_f2 = kd[-3:].replace(" ", "")
        strike = cols[3].text.strip().replace("\n", "")
        strike_f1 = strike.split(" ")[0]
        strike_f2 = strike[-3:].replace(" ", "")
        td = cols[4].text.strip().replace("\n", "")
        td_f1 = td.split(" ")[0]
        td_f2 = td[-3:].replace(" ", "")
        sub = cols[5].text.strip().replace("\n", "")
        sub_f1 = sub.split(" ")[0]
        sub_f2 = sub[-3:].replace(" ", "")
        weight_class = cols[6].text.strip()
        method = cols[7].text.strip().replace("\n", "")
        how = method.split(" ")[0]
        finish = method[-19:].replace(" ", "")
        round_ = cols[8].text.strip()
        time = cols[9].text.strip()

        # todo
        if result == "win":
            winner = fighter1
        elif result == "draw":
            winner = "Draw"
        else:
            winner = np.nan

        fights.append(
            [
                event_name,
                event_date,
                winner,
                fighter1,
                fighter2,
                kd_f1,
                kd_f2,
                strike_f1,
                strike_f2,
                td_f1,
                td_f2,
                sub_f1,
                sub_f2,
                weight_class,
                how,
                finish,
                round_,
                time,
            ]
        )
    return fights


def create_df():
    """ """
    all_fights = []
    for event in get_event_urls():
        event_fights = scrape_fight_data(event)
        all_fights = all_fights + event_fights
        print(event_fights[0][0])

    df = pd.DataFrame(
        all_fights,
        columns=[
            "Event",
            "Date",
            "Winner",
            "Fighter 1",
            "Fighter 2",
            "F1 Knockdown",
            "F2 Knockdown",
            "F1 Stike",
            "F2 Strike",
            "F1 Takedown",
            "F2 Takedown",
            "F1 Submission",
            "F2 Submission",
            "Weightclass",
            "Result",
            "Method",
            "Round",
            "Time",
        ],
    )
    print(df)
    return df


def main():
    df = create_df()
    df.to_csv("events.csv", sep=",")


if __name__ == "__main__":
    main()
