import requests
from bs4 import BeautifulSoup

import pandas as pd
import string


def scrape(to="fighters.csv"):
    """
    :param str to: The name of the csv file to store the data

    Scrape the ufcstats website to get data on all fighters and save the data to a csv file
    """
    # global table of all fighter
    fighters = []

    # iterate over all letters, get the page with the fighter table data, add the data to 'fighters'
    for char in string.ascii_lowercase:
        # get page for each letter
        url = f"http://ufcstats.com/statistics/fighters?char={char}&page=all"
        response = requests.get(url)
        print(f"{char} : {response}")
        soup = BeautifulSoup(response.content, "html.parser")

        # get the fighter table
        fighter_table = soup.find("table", class_="b-statistics__table")

        # only keep the fighter rows
        rows = fighter_table.find_all("tr")[2:]

        # each row is a fighter
        for row in rows:
            cols = row.find_all("td")
            fighters.append(
                [
                    cols[0].text.strip(),
                    cols[1].text.strip(),
                    cols[2].text.strip(),
                    cols[3].text.strip(),
                    cols[4].text.strip(),
                    cols[5].text.strip(),
                    cols[6].text.strip(),
                    cols[7].text.strip(),
                    cols[8].text.strip(),
                    cols[9].text.strip(),
                ]
            )

    # Create final Dataframe with header
    fighters_df = pd.DataFrame(
        fighters,
        columns=[
            "First Name",
            "Last Name",
            "Nickname",
            "Height",
            "Weight",
            "Reach",
            "Stance",
            "Wins",
            "Losses",
            "Draws",
        ],
    )
    print(fighters_df)
    # save
    fighters_df.to_csv(to, sep=",")


def main():
    scrape()


if __name__ == "__main__":
    main()
