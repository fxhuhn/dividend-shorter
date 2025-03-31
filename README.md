# dividend-shorter

bet on falling prices on payday **2025-03-31**.

## Signale

| Ticker   |   Divid Rate |   Close |           Volume |   last_close_volume |   Divid % | 5_Days_pos   | above_SMA_50   |
|:---------|-------------:|--------:|-----------------:|--------------------:|----------:|:-------------|:---------------|
| UPMMY    |         0.77 |   28.01 |  57000           |             1596570 |      2.76 | False        | False          |
| TRIN     |         0.51 |   15.83 | 792200           |            12540526 |      3.22 | False        | True           |
| SUNS     |         0.3  |   11.21 | 154300           |             1729703 |      2.68 | False        | False          |
| SCMWY    |         2.48 |   61.03 |   9200           |              561476 |      4.06 | True         | True           |
| RWAY     |         0.33 |   10.75 | 880500           |             9465375 |      3.07 | True         | False          |
| REFI     |         0.47 |   15.3  | 179200           |             2741760 |      3.07 | False        | False          |
| RC       |         0.12 |    4.97 |      4.1939e+06  |            20843683 |      2.52 | False        | False          |
| RANJY    |         0.84 |   22.42 |  15600           |              349752 |      3.76 | True         | True           |
| NYMT     |         0.2  |    6.5  | 600600           |             3903900 |      3.08 | False        | True           |
| NLY      |         0.7  |   20.66 |      1.23905e+07 |           255987730 |      3.39 | False        | False          |
| NLCP     |         0.43 |   15.15 |  30300           |              459045 |      2.84 | True         | False          |
| NCDL     |         0.45 |   17.3  | 370000           |             6401000 |      2.6  | True         | True           |
| MSD      |         0.22 |    8.09 |  92700           |              749943 |      2.72 | False        | False          |
| MITT     |         0.2  |    7.49 | 264400           |             1980356 |      2.67 | False        | True           |
| MFA      |         0.36 |   10.56 |      1.3428e+06  |            14179968 |      3.41 | False        | False          |
| LFT      |         0.08 |    2.68 | 168800           |              452384 |      2.99 | False        | False          |
| IIPR     |         1.9  |   63.75 | 360400           |            22975500 |      2.98 | False        | False          |
| GSBD     |         0.32 |   12.11 |      1.1321e+06  |            13709731 |      2.64 | False        | False          |
| GHI      |         0.37 |   12.76 |  34000           |              433840 |      2.9  | False        | True           |
| FBRT     |         0.36 |   12.98 | 454200           |             5895516 |      2.73 | False        | False          |
| EDD      |         0.16 |    4.84 | 185500           |              897820 |      3.31 | True         | True           |
| CIM      |         0.37 |   13.1  |      1.0512e+06  |            13770720 |      2.82 | False        | False          |
| CIB      |         3.81 |   43.79 | 562200           |            24618738 |      8.71 | True         | True           |
| CHMI     |         0.15 |    3.44 | 565800           |             1946352 |      4.36 | False        | True           |
| BRSP     |         0.16 |    5.68 | 672000           |             3816960 |      2.82 | False        | False          |
| BGS      |         0.19 |    6.63 |      2.5602e+06  |            16974126 |      2.87 | False        | False          |
| ARI      |         0.25 |    9.66 |      1.0172e+06  |             9826152 |      2.59 | False        | True           |
| AFCG     |         0.23 |    6.09 | 298000           |             1814820 |      3.78 | False        | False          |
| ACRE     |         0.15 |    4.7  | 816800           |             3838960 |      3.19 | False        | False          |

## UPMMY

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0   |       0.2 |      -0   |      -0.2 |      -0.2 |         7 |
| mit  |       0.1 |       0.6 |       0.3 |       0.5 |       0.2 |         1 |

### Ohne Filter
![image info](./data/UPMMY_box_all.png)
![image info](./data/UPMMY_median_all.png)

### Mit Filter
![image info](./data/UPMMY_box_filtered.png)
![image info](./data/UPMMY_median_filtered.png)

## TRIN

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |        -0 |        -0 |      -0.2 |      -0.3 |      -0.1 |        22 |
| mit  |        -0 |         0 |      -0.2 |      -0.3 |      -0   |        11 |

### Ohne Filter
![image info](./data/TRIN_box_all.png)
![image info](./data/TRIN_median_all.png)

### Mit Filter
![image info](./data/TRIN_box_filtered.png)
![image info](./data/TRIN_median_filtered.png)

## SUNS

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.6 |       0.8 |       1.1 |       2.7 |       0.7 |         2 |
| mit  |     nan   |     nan   |     nan   |     nan   |     nan   |         0 |

### Ohne Filter
![image info](./data/SUNS_box_all.png)
![image info](./data/SUNS_median_all.png)

### Mit Filter
![image info](./data/SUNS_box_filtered.png)
![image info](./data/SUNS_median_filtered.png)

## SCMWY

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |        -0 |       0   |        -0 |      -0.1 |        -0 |        16 |
| mit  |         0 |       0.1 |        -0 |       0   |         0 |         3 |

### Ohne Filter
![image info](./data/SCMWY_box_all.png)
![image info](./data/SCMWY_median_all.png)

### Mit Filter
![image info](./data/SCMWY_box_filtered.png)
![image info](./data/SCMWY_median_filtered.png)

## RWAY

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.2 |      -0.1 |         0 |       0.1 |       0.1 |        20 |
| mit  |      -0.2 |      -0.2 |        -0 |      -0.2 |      -0.1 |         8 |

### Ohne Filter
![image info](./data/RWAY_box_all.png)
![image info](./data/RWAY_median_all.png)

### Mit Filter
![image info](./data/RWAY_box_filtered.png)
![image info](./data/RWAY_median_filtered.png)

## REFI

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0   |       0.2 |       0   |       0.1 |       0.2 |        15 |
| mit  |       0.1 |       0.2 |       0.3 |       0.2 |       0.3 |         6 |

### Ohne Filter
![image info](./data/REFI_box_all.png)
![image info](./data/REFI_median_all.png)

### Mit Filter
![image info](./data/REFI_box_filtered.png)
![image info](./data/REFI_median_filtered.png)

## RC

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0   |        -0 |      -0.1 |      -0.1 |      -0.1 |        51 |
| mit  |      -0.1 |        -0 |      -0.3 |      -0.3 |      -0.2 |        13 |

### Ohne Filter
![image info](./data/RC_box_all.png)
![image info](./data/RC_median_all.png)

### Mit Filter
![image info](./data/RC_box_filtered.png)
![image info](./data/RC_median_filtered.png)

## RANJY

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0   |       0   |       0   |       0.5 |       0.8 |        16 |
| mit  |      -0.2 |      -0.3 |      -0.5 |      -1   |      -0.8 |         1 |

### Ohne Filter
![image info](./data/RANJY_box_all.png)
![image info](./data/RANJY_median_all.png)

### Mit Filter
![image info](./data/RANJY_box_filtered.png)
![image info](./data/RANJY_median_filtered.png)

## NYMT

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0   |       0   |       0.1 |       0.2 |       0.1 |        67 |
| mit  |      -0.1 |       0.2 |       0.1 |       0.1 |       0.4 |         6 |

### Ohne Filter
![image info](./data/NYMT_box_all.png)
![image info](./data/NYMT_median_all.png)

### Mit Filter
![image info](./data/NYMT_box_filtered.png)
![image info](./data/NYMT_median_filtered.png)

## NLY

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0   |         0 |       0.1 |      -0   |      -0   |        88 |
| mit  |      -0.1 |        -0 |       0.3 |       0.1 |       0.3 |        10 |

### Ohne Filter
![image info](./data/NLY_box_all.png)
![image info](./data/NLY_median_all.png)

### Mit Filter
![image info](./data/NLY_box_filtered.png)
![image info](./data/NLY_median_filtered.png)

## NLCP

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |        -0 |      -0.3 |      -0.1 |      -0.4 |      -0.2 |        13 |
| mit  |       nan |     nan   |     nan   |     nan   |     nan   |         0 |

### Ohne Filter
![image info](./data/NLCP_box_all.png)
![image info](./data/NLCP_median_all.png)

### Mit Filter
![image info](./data/NLCP_box_filtered.png)
![image info](./data/NLCP_median_filtered.png)

## NCDL

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |        -0 |       0.1 |      -0.2 |      -0.3 |      -0.3 |         8 |
| mit  |       nan |     nan   |     nan   |     nan   |     nan   |         0 |

### Ohne Filter
![image info](./data/NCDL_box_all.png)
![image info](./data/NCDL_median_all.png)

### Mit Filter
![image info](./data/NCDL_box_filtered.png)
![image info](./data/NCDL_median_filtered.png)

## MSD

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.1 |       0.1 |       0   |      -0   |       0   |        73 |
| mit  |      -0   |      -0.1 |       0.2 |       0.4 |       0.4 |         2 |

### Ohne Filter
![image info](./data/MSD_box_all.png)
![image info](./data/MSD_median_all.png)

### Mit Filter
![image info](./data/MSD_box_filtered.png)
![image info](./data/MSD_median_filtered.png)

## MITT

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.1 |      -0.2 |      -0.2 |      -0.1 |        -0 |        54 |
| mit  |      -0.2 |      -0.1 |      -0.5 |      -0.2 |        -0 |         5 |

### Ohne Filter
![image info](./data/MITT_box_all.png)
![image info](./data/MITT_median_all.png)

### Mit Filter
![image info](./data/MITT_box_filtered.png)
![image info](./data/MITT_median_filtered.png)

## MFA

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.1 |       0.1 |      -0   |         0 |       0   |        87 |
| mit  |      -0.1 |       0   |      -0.2 |        -0 |       0.1 |        10 |

### Ohne Filter
![image info](./data/MFA_box_all.png)
![image info](./data/MFA_median_all.png)

### Mit Filter
![image info](./data/MFA_box_filtered.png)
![image info](./data/MFA_median_filtered.png)

## LFT

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.2 |       0.4 |       0.3 |       0.5 |       0.2 |        92 |
| mit  |      -0.2 |      -0.2 |      -0.1 |      -0.1 |      -0.1 |         1 |

### Ohne Filter
![image info](./data/LFT_box_all.png)
![image info](./data/LFT_median_all.png)

### Mit Filter
![image info](./data/LFT_box_filtered.png)
![image info](./data/LFT_median_filtered.png)

## IIPR

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.1 |       0.2 |       0.3 |       0.6 |       0.2 |        31 |
| mit  |      -0.4 |      -1   |      -1   |      -1   |      -1   |         1 |

### Ohne Filter
![image info](./data/IIPR_box_all.png)
![image info](./data/IIPR_median_all.png)

### Mit Filter
![image info](./data/IIPR_box_filtered.png)
![image info](./data/IIPR_median_filtered.png)

## GSBD

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.2 |       0.2 |       0.1 |       0.1 |       0.2 |        43 |
| mit  |       0.4 |       0.5 |       0.2 |       0.3 |       0.5 |        12 |

### Ohne Filter
![image info](./data/GSBD_box_all.png)
![image info](./data/GSBD_median_all.png)

### Mit Filter
![image info](./data/GSBD_box_filtered.png)
![image info](./data/GSBD_median_filtered.png)

## GHI

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.2 |      -0   |      -0.2 |      -0.1 |      -0.1 |        11 |
| mit  |      -0.1 |      -0.6 |      -1   |      -1   |      -1   |         1 |

### Ohne Filter
![image info](./data/GHI_box_all.png)
![image info](./data/GHI_median_all.png)

### Mit Filter
![image info](./data/GHI_box_filtered.png)
![image info](./data/GHI_median_filtered.png)

## FBRT

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.1 |       0.1 |      -0.2 |      -0.1 |       0.1 |        13 |
| mit  |      -0.1 |      -0.1 |      -0.6 |      -0.6 |      -0.5 |         4 |

### Ohne Filter
![image info](./data/FBRT_box_all.png)
![image info](./data/FBRT_median_all.png)

### Mit Filter
![image info](./data/FBRT_box_filtered.png)
![image info](./data/FBRT_median_filtered.png)

## EDD

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.1 |       0.1 |       0.1 |         0 |      -0.1 |        67 |
| mit  |       0.1 |       0.2 |       0.2 |         0 |      -0.1 |         8 |

### Ohne Filter
![image info](./data/EDD_box_all.png)
![image info](./data/EDD_median_all.png)

### Mit Filter
![image info](./data/EDD_box_filtered.png)
![image info](./data/EDD_median_filtered.png)

## CIM

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.1 |       0.2 |       0.1 |         0 |       0.2 |        71 |
| mit  |     nan   |     nan   |     nan   |       nan |     nan   |         0 |

### Ohne Filter
![image info](./data/CIM_box_all.png)
![image info](./data/CIM_median_all.png)

### Mit Filter
![image info](./data/CIM_box_filtered.png)
![image info](./data/CIM_median_filtered.png)

## CIB

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.1 |      -0.4 |      -0.5 |      -1   |      -1   |        88 |
| mit  |      -0.3 |      -0.7 |      -0.2 |       0.2 |       1.1 |         3 |

### Ohne Filter
![image info](./data/CIB_box_all.png)
![image info](./data/CIB_median_all.png)

### Mit Filter
![image info](./data/CIB_box_filtered.png)
![image info](./data/CIB_median_filtered.png)

## CHMI

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.1 |       0   |       0   |       0   |       0   |        47 |
| mit  |       0.1 |       0.1 |       0.4 |       0.5 |       0.5 |        17 |

### Ohne Filter
![image info](./data/CHMI_box_all.png)
![image info](./data/CHMI_median_all.png)

### Mit Filter
![image info](./data/CHMI_box_filtered.png)
![image info](./data/CHMI_median_filtered.png)

## BRSP

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.1 |      -0.2 |      -0.2 |      -0.5 |      -0.4 |        42 |
| mit  |      -0.2 |      -0.3 |       0.1 |      -0.4 |      -0.3 |         9 |

### Ohne Filter
![image info](./data/BRSP_box_all.png)
![image info](./data/BRSP_median_all.png)

### Mit Filter
![image info](./data/BRSP_box_filtered.png)
![image info](./data/BRSP_median_filtered.png)

## BGS

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.3 |       0.4 |       0.3 |       0.3 |       0.4 |        70 |
| mit  |      -0.5 |      -1   |      -1   |      -1   |      -1   |         1 |

### Ohne Filter
![image info](./data/BGS_box_all.png)
![image info](./data/BGS_median_all.png)

### Mit Filter
![image info](./data/BGS_box_filtered.png)
![image info](./data/BGS_median_filtered.png)

## ARI

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.1 |       0   |       0   |      -0.1 |      -0.1 |        60 |
| mit  |      -0.1 |      -0.1 |      -0.2 |      -0.1 |      -0   |        18 |

### Ohne Filter
![image info](./data/ARI_box_all.png)
![image info](./data/ARI_median_all.png)

### Mit Filter
![image info](./data/ARI_box_filtered.png)
![image info](./data/ARI_median_filtered.png)

## AFCG

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |       0.3 |       0.5 |       0.4 |       0.6 |       0.7 |        16 |
| mit  |       0.3 |       0.4 |       0.4 |       0.6 |       0.7 |        14 |

### Ohne Filter
![image info](./data/AFCG_box_all.png)
![image info](./data/AFCG_median_all.png)

### Mit Filter
![image info](./data/AFCG_box_filtered.png)
![image info](./data/AFCG_median_filtered.png)

## ACRE

### Erwartung in R
|      |   Day_r_0 |   Day_r_1 |   Day_r_2 |   Day_r_3 |   Day_r_4 |   Treffer |
|:-----|----------:|----------:|----------:|----------:|----------:|----------:|
| ohne |      -0.1 |      -0.1 |      -0.3 |      -0.2 |      -0.2 |        61 |
| mit  |      -0.1 |      -0.2 |       0   |      -0.1 |       0.2 |        13 |

### Ohne Filter
![image info](./data/ACRE_box_all.png)
![image info](./data/ACRE_median_all.png)

### Mit Filter
![image info](./data/ACRE_box_filtered.png)
![image info](./data/ACRE_median_filtered.png)

