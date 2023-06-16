# UFC Fighter Data

## Scraping

Using BeautifulSoup we scrape the fighter data from the [UFCStats](http://ufcstats.com/statistics/fighters) website:

```
     First Name   Last Name      Nickname  Height    Weight  Reach    Stance Wins Losses Draws
0           Tom       Aaron                    --  155 lbs.     --              5      3     0
1         Danny      Abbadi  The Assassin  5' 11"  155 lbs.     --  Orthodox    4      6     0
2       Nariman     Abbasov     Bayraktar   5' 8"  155 lbs.  66.0"  Orthodox   28      4     0
3         David      Abbott          Tank   6' 0"  265 lbs.     --    Switch   10     15     0
4         Hamdy  Abdelwahab    The Hammer   6' 2"  264 lbs.  72.0"  Southpaw    5      0     0
...         ...         ...           ...     ...       ...    ...       ...  ...    ...   ...
4035       Dave    Zitanick                    --  170 lbs.     --              5      7     0
4036       Alex      Zuniga                    --  145 lbs.     --              6      3     0
4037     George      Zuniga                 5' 9"  185 lbs.     --              3      1     0
4038      Allan      Zuniga         Tigre   5' 7"  155 lbs.  70.0"  Orthodox   13      1     0
4039     Virgil     Zwicker        RezDog   6' 2"  205 lbs.  74.0"             15      6     1

[4040 rows x 10 columns]
```

## Data Pre-processing

We clean the data, convert US unit to metric, remove fighter with no weight and one outlier.

## Visualisation

We use matplotlib to visualize our data