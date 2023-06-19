# Scraping

## Fighter
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

## Events
And the fight data since UFC2:
```
                          Event            Date                Winner             Loser Knockdown # W Knockdown # L  ... Submission # L           Weightclass  Result           Method Round   Time
0     UFC 289: Nunes vs. Aldana   June 10, 2023          Amanda Nunes      Irene Aldana             0             0  ...              0  Women's Bantamweight   U-DEC            U-DEC     5   5:00
1     UFC 289: Nunes vs. Aldana   June 10, 2023      Charles Oliveira    Beneil Dariush             1             0  ...              0           Lightweight  KO/TKO          Punches     1   4:10
2     UFC 289: Nunes vs. Aldana   June 10, 2023           Mike Malott       Adam Fugitt             1             0  ...              0          Welterweight     SUB  GuillotineChoke     2   1:06
3     UFC 289: Nunes vs. Aldana   June 10, 2023               Dan Ige     Nate Landwehr             1             0  ...              0         Featherweight   U-DEC            U-DEC     3   5:00
4     UFC 289: Nunes vs. Aldana   June 10, 2023  Marc-Andre Barriault       Eryk Anders             1             0  ...              0          Middleweight   U-DEC            U-DEC     3   5:00
...                         ...             ...                   ...               ...           ...           ...  ...            ...                   ...     ...              ...   ...    ...
7162          UFC 2: No Way Out  March 11, 1994          Orlando Wiet  Robert Lucarelli             0             0  ...              1           Open Weight  KO/TKO           KO/TKO     1   2:50
7163          UFC 2: No Way Out  March 11, 1994         Frank Hamaker   Thaddeus Luster             0             0  ...              0           Open Weight     SUB          Keylock     1   4:52
7164          UFC 2: No Way Out  March 11, 1994         Johnny Rhodes     David Levicki             0             0  ...              0           Open Weight  KO/TKO          Punches     1  12:13
7165          UFC 2: No Way Out  March 11, 1994         Patrick Smith        Ray Wizard             0             0  ...              0           Open Weight     SUB  GuillotineChoke     1   0:58
7166          UFC 2: No Way Out  March 11, 1994          Scott Morris    Sean Daugherty             0             0  ...              0           Open Weight     SUB  GuillotineChoke     1   0:20

[7167 rows x 17 columns]
```
