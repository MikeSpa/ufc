# UFC Fighter Data

## Scraping

Using BeautifulSoup we scrape the fighter data from the [UFCStats](http://ufcstats.com/statistics/fighters) website:

### Fighter record
The record of every fighter who fought in the UFC.
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
### Events record
The fight data since UFC2.
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
### Fights data
Fights' data with betting odds and most statistics about each fight (event's data, finishing's data, stiking, takedown, submission attemps' data, ...).
```
                R_fighter        B_fighter  R_odds  B_odds        R_ev        B_ev        date  ... total_fight_time_secs r_dec_odds b_dec_odds  r_sub_odds b_sub_odds r_ko_odds  b_ko_odds
0           Thiago Santos    Johnny Walker  -150.0     130   66.666667  130.000000  2021-10-02  ...                1500.0      800.0      900.0      2000.0     1600.0    -110.0      175.0
1           Alex Oliveira       Niko Price   170.0    -200  170.000000   50.000000  2021-10-02  ...                 900.0      450.0      350.0       700.0     1100.0     550.0      120.0
2          Misha Cirkunov  Krzysztof Jotko   110.0    -130  110.000000   76.923077  2021-10-02  ...                 900.0      550.0      275.0       275.0     1400.0     600.0      185.0
3     Alexander Hernandez     Mike Breeden  -675.0     475   14.814815  475.000000  2021-10-02  ...                  80.0      175.0      900.0       500.0     3500.0     110.0     1100.0
4             Joe Solecki     Jared Gordon  -135.0     115   74.074074  115.000000  2021-10-02  ...                 900.0      165.0      200.0       400.0     1200.0     900.0      600.0
...                   ...              ...     ...     ...         ...         ...         ...  ...                   ...        ...        ...         ...        ...       ...        ...
4891         Duane Ludwig    Darren Elkins  -155.0     135   64.516129  135.000000   3/21/2010  ...                  44.0        NaN        NaN         NaN        NaN       NaN        NaN
4892          John Howard   Daniel Roberts  -210.0     175   47.619048  175.000000   3/21/2010  ...                 121.0        NaN        NaN         NaN        NaN       NaN        NaN
4893       Brendan Schaub    Chase Gormley  -260.0     220   38.461538  220.000000   3/21/2010  ...                  47.0        NaN        NaN         NaN        NaN       NaN        NaN
4894          Mike Pierce    Julio Paulino  -420.0     335   23.809524  335.000000   3/21/2010  ...                 900.0        NaN        NaN         NaN        NaN       NaN        NaN
4895         Eric Schafer      Jason Brilz   140.0    -160  140.000000   62.500000   3/21/2010  ...                 900.0        NaN        NaN         NaN        NaN       NaN        NaN

[4896 rows x 119 columns]
```

## Visualisation

Several notebooks explore and visualize interesting patterns in the data

## Fight prediction

Machine learning to predict winner of future fights.  
`fight-prediction-baseline-model.ipynb` contains a simple baseline model to predict the winner of a fight: 58% accuracy.
`fight-prediction-random-forest-log-regression-model.ipynb` contains two classification models to predict the winner of a fight with a 66% accuracy.

