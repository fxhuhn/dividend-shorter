# dividend-shorter

bet on falling prices on payday

## Signale

| Ticker   |   Divid Rate |   Close |   Volume |   last_close_volume |   Divid % | 5_Days_pos   | above_SMA_50   |
|:---------|-------------:|--------:|---------:|--------------------:|----------:|:-------------|:---------------|
| FLNG     |         0.75 |   25.75 |   422400 |            10876800 |      2.91 | False        | True           |

## FLNG

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0   |       0.1 |       0.2 |       0.5 |       0.4 |        21 |
| mit  |       0.2 |       0.3 |       0.6 |       1   |       0.5 |         4 |

### Ohne Filter
![image info](./data/FLNG_box_all.png)
![image info](./data/FLNG_median_all.png)

### Mit Filter
![image info](./data/FLNG_box_filtered.png)
![image info](./data/FLNG_median_filtered.png)

