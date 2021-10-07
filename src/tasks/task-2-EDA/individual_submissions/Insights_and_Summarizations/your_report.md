Toggle navigation

[Pandas Profiling Report](#top)

-   [Overview](#overview)
-   [Variables](#variables)
-   [Interactions](#interactions)
-   [Correlations](#correlations)
-   [Missing values](#missing)
-   [Sample](#sample)

Overview {.page-header}
========

-   [Overview](#overview-dataset_overview)
-   [Warnings 24](#overview-warnings)
-   [Reproduction](#overview-reproduction)

Dataset statistics

Number of variables

7

Number of observations

254

Missing cells

0

Missing cells (%)

0.0%

Duplicate rows

0

Duplicate rows (%)

0.0%

Total size in memory

27.8 KiB

Average record size in memory

112.2 B

Variable types

Categorical

1

Numeric

6

Warnings

[`County`](#pp_var_6356815418641180077) has a high cardinality: 254
distinct values

High cardinality

[`Per Capita Income`](#pp_var_-9086053598153151805) is highly correlated
with `Median Household Income` and 2 other fields

High correlation

[`Median Household Income`](#pp_var_-522231352695086008) is highly
correlated with `Per Capita Income` and 2 other fields

High correlation

[`% of Population in Poverty`](#pp_var_8928108172586727098) is highly
correlated with `Per Capita Income` and 2 other fields

High correlation

[`% of Population Under 18 in Poverty`](#pp_var_2314277592537816524) is
highly correlated with `Per Capita Income` and 2 other fields

High correlation

[`Per Capita Income`](#pp_var_-9086053598153151805) is highly correlated
with `Median Household Income` and 2 other fields

High correlation

[`Median Household Income`](#pp_var_-522231352695086008) is highly
correlated with `Per Capita Income` and 3 other fields

High correlation

[`Average Annual Pay`](#pp_var_3119362176841245447) is highly correlated
with `Median Household Income`

High correlation

[`% of Population in Poverty`](#pp_var_8928108172586727098) is highly
correlated with `Per Capita Income` and 2 other fields

High correlation

[`% of Population Under 18 in Poverty`](#pp_var_2314277592537816524) is
highly correlated with `Per Capita Income` and 2 other fields

High correlation

[`Median Household Income`](#pp_var_-522231352695086008) is highly
correlated with `% of Population in Poverty` and 1 other fields

High correlation

[`% of Population in Poverty`](#pp_var_8928108172586727098) is highly
correlated with `Median Household Income` and 1 other fields

High correlation

[`% of Population Under 18 in Poverty`](#pp_var_2314277592537816524) is
highly correlated with `Median Household Income` and 1 other fields

High correlation

[`Per Capita Income`](#pp_var_-9086053598153151805) is highly correlated
with `Total Personal Income` and 4 other fields

High correlation

[`Total Personal Income`](#pp_var_3463410218962846340) is highly
correlated with `Per Capita Income`

High correlation

[`Average Annual Pay`](#pp_var_3119362176841245447) is highly correlated
with `Per Capita Income` and 2 other fields

High correlation

[`Median Household Income`](#pp_var_-522231352695086008) is highly
correlated with `Per Capita Income` and 3 other fields

High correlation

[`% of Population in Poverty`](#pp_var_8928108172586727098) is highly
correlated with `Per Capita Income` and 2 other fields

High correlation

[`% of Population Under 18 in Poverty`](#pp_var_2314277592537816524) is
highly correlated with `Per Capita Income` and 3 other fields

High correlation

[`County`](#pp_var_6356815418641180077) is uniformly distributed

Uniform

[`County`](#pp_var_6356815418641180077) has unique values

Unique

[`Total Personal Income`](#pp_var_3463410218962846340) has unique values

Unique

[`Median Household Income`](#pp_var_-522231352695086008) has unique
values

Unique

[`Average Annual Pay`](#pp_var_3119362176841245447) has unique values

Unique

Reproduction

Analysis started

2021-10-07 14:01:45.196303

Analysis finished

2021-10-07 14:02:06.158566

Duration

20.96 seconds

Software version

[pandas-profiling
v3.0.0](https://github.com/pandas-profiling/pandas-profiling)

Download configuration

[config.json](data:text/plain;charset=utf-8,%7B%22title%22%3A%20%22Pandas%20Profiling%20Report%22%2C%20%22dataset%22%3A%20%7B%22description%22%3A%20%22%22%2C%20%22creator%22%3A%20%22%22%2C%20%22author%22%3A%20%22%22%2C%20%22copyright_holder%22%3A%20%22%22%2C%20%22copyright_year%22%3A%20%22%22%2C%20%22url%22%3A%20%22%22%7D%2C%20%22variables%22%3A%20%7B%22descriptions%22%3A%20%7B%7D%7D%2C%20%22infer_dtypes%22%3A%20true%2C%20%22show_variable_description%22%3A%20true%2C%20%22pool_size%22%3A%200%2C%20%22progress_bar%22%3A%20true%2C%20%22vars%22%3A%20%7B%22num%22%3A%20%7B%22quantiles%22%3A%20%5B0.05%2C%200.25%2C%200.5%2C%200.75%2C%200.95%5D%2C%20%22skewness_threshold%22%3A%2020%2C%20%22low_categorical_threshold%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%7D%2C%20%22cat%22%3A%20%7B%22length%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22cardinality_threshold%22%3A%2050%2C%20%22n_obs%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%2C%20%22coerce_str_to_date%22%3A%20false%2C%20%22redact%22%3A%20false%2C%20%22histogram_largest%22%3A%2050%7D%2C%20%22image%22%3A%20%7B%22active%22%3A%20true%2C%20%22exif%22%3A%20true%2C%20%22hash%22%3A%20true%7D%2C%20%22bool%22%3A%20%7B%22n_obs%22%3A%203%2C%20%22mappings%22%3A%20%7B%22t%22%3A%20true%2C%20%22f%22%3A%20false%2C%20%22yes%22%3A%20true%2C%20%22no%22%3A%20false%2C%20%22y%22%3A%20true%2C%20%22n%22%3A%20false%2C%20%22true%22%3A%20true%2C%20%22false%22%3A%20false%7D%7D%2C%20%22path%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22file%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22url%22%3A%20%7B%22active%22%3A%20true%7D%7D%2C%20%22sort%22%3A%20null%2C%20%22missing_diagrams%22%3A%20%7B%22bar%22%3A%20true%2C%20%22matrix%22%3A%20true%2C%20%22dendrogram%22%3A%20true%2C%20%22heatmap%22%3A%20true%7D%2C%20%22correlations%22%3A%20%7B%22spearman%22%3A%20%7B%22key%22%3A%20%22spearman%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%7D%2C%20%22pearson%22%3A%20%7B%22key%22%3A%20%22pearson%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%7D%2C%20%22kendall%22%3A%20%7B%22key%22%3A%20%22kendall%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%7D%2C%20%22cramers%22%3A%20%7B%22key%22%3A%20%22cramers%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%7D%2C%20%22phi_k%22%3A%20%7B%22key%22%3A%20%22phi_k%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%7D%7D%2C%20%22interactions%22%3A%20%7B%22continuous%22%3A%20true%2C%20%22targets%22%3A%20%5B%5D%7D%2C%20%22categorical_maximum_correlation_distinct%22%3A%20100%2C%20%22memory_deep%22%3A%20true%2C%20%22plot%22%3A%20%7B%22missing%22%3A%20%7B%22force_labels%22%3A%20true%2C%20%22cmap%22%3A%20%22RdBu%22%7D%2C%20%22image_format%22%3A%20%22svg%22%2C%20%22correlation%22%3A%20%7B%22cmap%22%3A%20%22RdBu%22%2C%20%22bad%22%3A%20%22%23000000%22%7D%2C%20%22dpi%22%3A%20800%2C%20%22histogram%22%3A%20%7B%22bins%22%3A%2050%2C%20%22max_bins%22%3A%20250%2C%20%22x_axis_labels%22%3A%20true%7D%2C%20%22scatter_threshold%22%3A%201000%2C%20%22pie%22%3A%20%7B%22max_unique%22%3A%2010%7D%7D%2C%20%22duplicates%22%3A%20%7B%22head%22%3A%2010%2C%20%22key%22%3A%20%22%23%20duplicates%22%7D%2C%20%22samples%22%3A%20%7B%22head%22%3A%2010%2C%20%22tail%22%3A%2010%2C%20%22random%22%3A%200%7D%2C%20%22reject_variables%22%3A%20true%2C%20%22n_obs_unique%22%3A%2010%2C%20%22n_freq_table_max%22%3A%2010%2C%20%22n_extreme_obs%22%3A%2010%2C%20%22report%22%3A%20%7B%22precision%22%3A%2010%7D%2C%20%22html%22%3A%20%7B%22style%22%3A%20%7B%22primary_color%22%3A%20%22%23337ab7%22%2C%20%22logo%22%3A%20%22%22%2C%20%22theme%22%3A%20null%7D%2C%20%22navbar_show%22%3A%20true%2C%20%22minify_html%22%3A%20true%2C%20%22use_local_assets%22%3A%20true%2C%20%22inline%22%3A%20true%2C%20%22assets_prefix%22%3A%20null%2C%20%22assets_path%22%3A%20null%2C%20%22full_width%22%3A%20false%7D%2C%20%22notebook%22%3A%20%7B%22iframe%22%3A%20%7B%22height%22%3A%20%22800px%22%2C%20%22width%22%3A%20%22100%25%22%2C%20%22attribute%22%3A%20%22srcdoc%22%7D%7D%7D)

Variables {.page-header}
=========

[County](#pp_var_6356815418641180077)\
Categorical

`HIGH CARDINALITY`\
`UNIFORM`\
`UNIQUE`\

Distinct

254

Distinct (%)

100.0%

Missing

0

Missing (%)

0.0%

Memory size

15.9 KiB

Anderson

 

1

Navarro

 

1

McMullen

 

1

Medina

 

1

Menard

 

1

Other values (249)

249 

Toggle details

-   [Overview](#6356815418641180077bottom-6356815418641180077overview)
-   [Categories](#6356815418641180077bottom-6356815418641180077string)
-   [Words](#6356815418641180077bottom-6356815418641180077word)
-   [Characters](#6356815418641180077bottom-6356815418641180077characters)

Length

Max length

13

Median length

6

Mean length

6.669291339

Min length

3

Characters and Unicode

Total characters

1694

Distinct characters

50

Distinct categories

3
[?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)")

Distinct scripts

2
[?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)")

Distinct blocks

1
[?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)")

The Unicode Standard assigns character properties to each code point,
which can be used to analyse textual variables.

Unique

Unique

254 ?

Unique (%)

100.0%

Sample

1st row

Anderson

2nd row

Andrews

3rd row

Angelina

4th row

Aransas

5th row

Archer

#### Common Values

Value

Count

Frequency (%)

Anderson

1

 

0.4%

Navarro

1

 

0.4%

McMullen

1

 

0.4%

Medina

1

 

0.4%

Menard

1

 

0.4%

Midland

1

 

0.4%

Milam

1

 

0.4%

Mills

1

 

0.4%

Mitchell

1

 

0.4%

Montague

1

 

0.4%

Other values (244)

244

96.1%

#### Length

2021-10-07T19:32:06.870416image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Histogram of lengths of the category

Value

Count

Frequency (%)

san

4

 

1.5%

smith

2

 

0.7%

jim

2

 

0.7%

anderson

1

 

0.4%

navarro

1

 

0.4%

nacogdoches

1

 

0.4%

motley

1

 

0.4%

morris

1

 

0.4%

moore

1

 

0.4%

montgomery

1

 

0.4%

Other values (256)

256

94.5%

-   [Characters](#6356815418641180077unicode-6356815418641180077characters)
-   [Categories](#6356815418641180077unicode-6356815418641180077categories)
-   [Scripts](#6356815418641180077unicode-6356815418641180077scripts)
-   [Blocks](#6356815418641180077unicode-6356815418641180077blocks)

#### Most occurring characters

Value

Count

Frequency (%)

a

167

 

9.9%

e

153

 

9.0%

o

133

 

7.9%

n

126

 

7.4%

r

126

 

7.4%

l

119

 

7.0%

s

89

 

5.3%

i

87

 

5.1%

t

69

 

4.1%

d

42

 

2.5%

Other values (40)

583

34.4%

#### Most occurring categories

Value

Count

Frequency (%)

Lowercase Letter

1402

82.8%

Uppercase Letter

275

 

16.2%

Space Separator

17

 

1.0%

#### Most frequent character per category

##### *Lowercase Letter*

Value

Count

Frequency (%)

a

167

11.9%

e

153

10.9%

o

133

9.5%

n

126

9.0%

r

126

9.0%

l

119

8.5%

s

89

 

6.3%

i

87

 

6.2%

t

69

 

4.9%

d

42

 

3.0%

Other values (15)

291

20.8%

##### *Uppercase Letter*

Value

Count

Frequency (%)

C

29

 

10.5%

H

24

 

8.7%

S

21

 

7.6%

M

21

 

7.6%

B

20

 

7.3%

W

17

 

6.2%

L

16

 

5.8%

G

13

 

4.7%

R

13

 

4.7%

D

12

 

4.4%

Other values (14)

89

32.4%

##### *Space Separator*

Value

Count

Frequency (%)

17

100.0%

#### Most occurring scripts

Value

Count

Frequency (%)

Latin

1677

99.0%

Common

17

 

1.0%

#### Most frequent character per script

##### *Latin*

Value

Count

Frequency (%)

a

167

 

10.0%

e

153

 

9.1%

o

133

 

7.9%

n

126

 

7.5%

r

126

 

7.5%

l

119

 

7.1%

s

89

 

5.3%

i

87

 

5.2%

t

69

 

4.1%

d

42

 

2.5%

Other values (39)

566

33.8%

##### *Common*

Value

Count

Frequency (%)

17

100.0%

#### Most occurring blocks

Value

Count

Frequency (%)

ASCII

1694

100.0%

#### Most frequent character per block

##### *ASCII*

Value

Count

Frequency (%)

a

167

 

9.9%

e

153

 

9.0%

o

133

 

7.9%

n

126

 

7.4%

r

126

 

7.4%

l

119

 

7.0%

s

89

 

5.3%

i

87

 

5.1%

t

69

 

4.1%

d

42

 

2.5%

Other values (40)

583

34.4%

[Per Capita Income](#pp_var_-9086053598153151805)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`HIGH CORRELATION`\
`HIGH CORRELATION`\

Distinct

253

Distinct (%)

99.6%

Missing

0

Missing (%)

0.0%

Infinite

0

Infinite (%)

0.0%

Mean

46478.92126

Minimum

23569

Maximum

130983

Zeros

0

Zeros (%)

0.0%

Negative

0

Negative (%)

0.0%

Memory size

2.1 KiB

2021-10-07T19:32:07.139937image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#-9086053598153151805bottom--9086053598153151805statistics)
-   [Histogram](#-9086053598153151805bottom--9086053598153151805histogram)
-   [Common
    values](#-9086053598153151805bottom--9086053598153151805common_values)
-   [Extreme
    values](#-9086053598153151805bottom--9086053598153151805extreme_values)

Quantile statistics

Minimum

23569

5-th percentile

32379.55

Q1

39609

median

44302

Q3

50715.25

95-th percentile

65278

Maximum

130983

Range

107414

Interquartile range (IQR)

11106.25

Descriptive statistics

Standard deviation

12719.55435

Coefficient of variation (CV)

0.2736628562

Kurtosis

10.89917252

Mean

46478.92126

Median Absolute Deviation (MAD)

5408.5

Skewness

2.466599132

Sum

11805646

Variance

161787062.8

Monotonicity

Not monotonic

2021-10-07T19:32:07.453462image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

39609

2

 

0.8%

36027

1

 

0.4%

38569

1

 

0.4%

42159

1

 

0.4%

65250

1

 

0.4%

41095

1

 

0.4%

37218

1

 

0.4%

130983

1

 

0.4%

37238

1

 

0.4%

39334

1

 

0.4%

Other values (243)

243

95.7%

-   [Minimum 5
    values](#-9086053598153151805extreme_values--9086053598153151805firstn)
-   [Maximum 5
    values](#-9086053598153151805extreme_values--9086053598153151805lastn)

Value

Count

Frequency (%)

23569

1

0.4%

27415

1

0.4%

27584

1

0.4%

27713

1

0.4%

28936

1

0.4%

29792

1

0.4%

29838

1

0.4%

29928

1

0.4%

30223

1

0.4%

30731

1

0.4%

Value

Count

Frequency (%)

130983

1

0.4%

113163

1

0.4%

97002

1

0.4%

84623

1

0.4%

81882

1

0.4%

81238

1

0.4%

78849

1

0.4%

78826

1

0.4%

77810

1

0.4%

72177

1

0.4%

[Total Personal Income](#pp_var_3463410218962846340)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`UNIQUE`\

Distinct

254

Distinct (%)

100.0%

Missing

0

Missing (%)

0.0%

Infinite

0

Infinite (%)

0.0%

Mean

6028923063

Minimum

9081000

Maximum

2.82809166 × 10^11^

Zeros

0

Zeros (%)

0.0%

Negative

0

Negative (%)

0.0%

Memory size

2.1 KiB

2021-10-07T19:32:07.830743image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#3463410218962846340bottom-3463410218962846340statistics)
-   [Histogram](#3463410218962846340bottom-3463410218962846340histogram)
-   [Common
    values](#3463410218962846340bottom-3463410218962846340common_values)
-   [Extreme
    values](#3463410218962846340bottom-3463410218962846340extreme_values)

Quantile statistics

Minimum

9081000

5-th percentile

77558600

Q1

310971750

median

842369000

Q3

2169747000

95-th percentile

2.01714424 × 10^10^

Maximum

2.82809166 × 10^11^

Range

2.82800085 × 10^11^

Interquartile range (IQR)

1858775250

Descriptive statistics

Standard deviation

2.404490496 × 10^10^

Coefficient of variation (CV)

3.988258717

Kurtosis

79.14480708

Mean

6028923063

Median Absolute Deviation (MAD)

669098000

Skewness

8.109233359

Sum

1.531346458 × 10^12^

Variance

5.781574545 × 10^20^

Monotonicity

Not monotonic

2021-10-07T19:32:08.134769image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

2080020000

1

 

0.4%

1987095000

1

 

0.4%

48481000

1

 

0.4%

2119867000

1

 

0.4%

79573000

1

 

0.4%

2.3161978 × 10^10^

1

 

0.4%

924367000

1

 

0.4%

191673000

1

 

0.4%

287052000

1

 

0.4%

836915000

1

 

0.4%

Other values (244)

244

96.1%

-   [Minimum 5
    values](#3463410218962846340extreme_values-3463410218962846340firstn)
-   [Maximum 5
    values](#3463410218962846340extreme_values-3463410218962846340lastn)

Value

Count

Frequency (%)

9081000

1

0.4%

17074000

1

0.4%

21447000

1

0.4%

38483000

1

0.4%

39585000

1

0.4%

40082000

1

0.4%

41286000

1

0.4%

41628000

1

0.4%

48481000

1

0.4%

51854000

1

0.4%

Value

Count

Frequency (%)

2.82809166 × 10^11^

1

0.4%

1.65463378 × 10^11^

1

0.4%

1.1204659 × 10^11^

1

0.4%

9.5829678 × 10^10^

1

0.4%

9.1299737 × 10^10^

1

0.4%

7.0852208 × 10^10^

1

0.4%

5.2712796 × 10^10^

1

0.4%

4.8419712 × 10^10^

1

0.4%

3.8523113 × 10^10^

1

0.4%

3.1651549 × 10^10^

1

0.4%

[Median Household Income](#pp_var_-522231352695086008)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`HIGH CORRELATION`\
`HIGH CORRELATION`\
`HIGH CORRELATION`\
`UNIQUE`\

Distinct

254

Distinct (%)

100.0%

Missing

0

Missing (%)

0.0%

Infinite

0

Infinite (%)

0.0%

Mean

54958.17717

Minimum

31410

Maximum

105763

Zeros

0

Zeros (%)

0.0%

Negative

0

Negative (%)

0.0%

Memory size

2.1 KiB

2021-10-07T19:32:08.423605image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#-522231352695086008bottom--522231352695086008statistics)
-   [Histogram](#-522231352695086008bottom--522231352695086008histogram)
-   [Common
    values](#-522231352695086008bottom--522231352695086008common_values)
-   [Extreme
    values](#-522231352695086008bottom--522231352695086008extreme_values)

Quantile statistics

Minimum

31410

5-th percentile

38841.95

Q1

45775.25

median

52703

Q3

61343.5

95-th percentile

82922.05

Maximum

105763

Range

74353

Interquartile range (IQR)

15568.25

Descriptive statistics

Standard deviation

13348.13172

Coefficient of variation (CV)

0.242877992

Kurtosis

1.735484309

Mean

54958.17717

Median Absolute Deviation (MAD)

7775

Skewness

1.203584869

Sum

13959377

Variance

178172620.3

Monotonicity

Not monotonic

2021-10-07T19:32:08.710634image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

48461

1

 

0.4%

48649

1

 

0.4%

68349

1

 

0.4%

60695

1

 

0.4%

38425

1

 

0.4%

85811

1

 

0.4%

48989

1

 

0.4%

46876

1

 

0.4%

44457

1

 

0.4%

53649

1

 

0.4%

Other values (244)

244

96.1%

-   [Minimum 5
    values](#-522231352695086008extreme_values--522231352695086008firstn)
-   [Maximum 5
    values](#-522231352695086008extreme_values--522231352695086008lastn)

Value

Count

Frequency (%)

31410

1

0.4%

32516

1

0.4%

32538

1

0.4%

33499

1

0.4%

35821

1

0.4%

35940

1

0.4%

36069

1

0.4%

37100

1

0.4%

37876

1

0.4%

38425

1

0.4%

Value

Count

Frequency (%)

105763

1

0.4%

101361

1

0.4%

96847

1

0.4%

94899

1

0.4%

93759

1

0.4%

93351

1

0.4%

92661

1

0.4%

90910

1

0.4%

88833

1

0.4%

88487

1

0.4%

[Average Annual Pay](#pp_var_3119362176841245447)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`HIGH CORRELATION`\
`UNIQUE`\

Distinct

254

Distinct (%)

100.0%

Missing

0

Missing (%)

0.0%

Infinite

0

Infinite (%)

0.0%

Mean

46160.9252

Minimum

27058

Maximum

85618

Zeros

0

Zeros (%)

0.0%

Negative

0

Negative (%)

0.0%

Memory size

2.1 KiB

2021-10-07T19:32:09.033822image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#3119362176841245447bottom-3119362176841245447statistics)
-   [Histogram](#3119362176841245447bottom-3119362176841245447histogram)
-   [Common
    values](#3119362176841245447bottom-3119362176841245447common_values)
-   [Extreme
    values](#3119362176841245447bottom-3119362176841245447extreme_values)

Quantile statistics

Minimum

27058

5-th percentile

33202.5

Q1

39325

median

43509.5

Q3

50284

95-th percentile

68729.65

Maximum

85618

Range

58560

Interquartile range (IQR)

10959

Descriptive statistics

Standard deviation

10428.14809

Coefficient of variation (CV)

0.225908559

Kurtosis

1.327597289

Mean

46160.9252

Median Absolute Deviation (MAD)

5109.5

Skewness

1.154970257

Sum

11724875

Variance

108746272.7

Monotonicity

Not monotonic

2021-10-07T19:32:09.408674image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

45799

1

 

0.4%

39829

1

 

0.4%

56402

1

 

0.4%

38571

1

 

0.4%

28428

1

 

0.4%

78610

1

 

0.4%

41661

1

 

0.4%

34735

1

 

0.4%

43530

1

 

0.4%

42035

1

 

0.4%

Other values (244)

244

96.1%

-   [Minimum 5
    values](#3119362176841245447extreme_values-3119362176841245447firstn)
-   [Maximum 5
    values](#3119362176841245447extreme_values-3119362176841245447lastn)

Value

Count

Frequency (%)

27058

1

0.4%

27178

1

0.4%

28428

1

0.4%

29765

1

0.4%

29981

1

0.4%

30348

1

0.4%

31200

1

0.4%

31251

1

0.4%

31965

1

0.4%

32043

1

0.4%

Value

Count

Frequency (%)

85618

1

0.4%

78995

1

0.4%

78610

1

0.4%

78135

1

0.4%

73895

1

0.4%

72710

1

0.4%

71990

1

0.4%

71084

1

0.4%

71047

1

0.4%

69953

1

0.4%

[% of Population in Poverty](#pp_var_8928108172586727098)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`HIGH CORRELATION`\
`HIGH CORRELATION`\
`HIGH CORRELATION`\

Distinct

131

Distinct (%)

51.6%

Missing

0

Missing (%)

0.0%

Infinite

0

Infinite (%)

0.0%

Mean

15.45629921

Minimum

4.8

Maximum

32.5

Zeros

0

Zeros (%)

0.0%

Negative

0

Negative (%)

0.0%

Memory size

2.1 KiB

2021-10-07T19:32:09.757766image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#8928108172586727098bottom-8928108172586727098statistics)
-   [Histogram](#8928108172586727098bottom-8928108172586727098histogram)
-   [Common
    values](#8928108172586727098bottom-8928108172586727098common_values)
-   [Extreme
    values](#8928108172586727098bottom-8928108172586727098extreme_values)

Quantile statistics

Minimum

4.8

5-th percentile

8.265

Q1

11.95

median

14.85

Q3

18.325

95-th percentile

24.585

Maximum

32.5

Range

27.7

Interquartile range (IQR)

6.375

Descriptive statistics

Standard deviation

5.036932736

Coefficient of variation (CV)

0.3258821964

Kurtosis

0.5581172773

Mean

15.45629921

Median Absolute Deviation (MAD)

3.15

Skewness

0.6259388151

Sum

3925.9

Variance

25.37069139

Monotonicity

Not monotonic

2021-10-07T19:32:10.063508image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

13.1

5

 

2.0%

20.7

5

 

2.0%

14.4

5

 

2.0%

13.8

5

 

2.0%

17

5

 

2.0%

14.3

4

 

1.6%

16.5

4

 

1.6%

7.4

4

 

1.6%

12.1

4

 

1.6%

8.6

4

 

1.6%

Other values (121)

209

82.3%

-   [Minimum 5
    values](#8928108172586727098extreme_values-8928108172586727098firstn)
-   [Maximum 5
    values](#8928108172586727098extreme_values-8928108172586727098lastn)

Value

Count

Frequency (%)

4.8

1

 

0.4%

5.4

1

 

0.4%

6.1

1

 

0.4%

6.5

1

 

0.4%

6.6

1

 

0.4%

6.7

1

 

0.4%

7.1

1

 

0.4%

7.4

4

1.6%

7.9

1

 

0.4%

8.2

1

 

0.4%

Value

Count

Frequency (%)

32.5

1

0.4%

30.5

1

0.4%

30.1

1

0.4%

29.6

2

0.8%

28

1

0.4%

27.7

1

0.4%

26.9

2

0.8%

26.6

1

0.4%

25.5

1

0.4%

25.4

1

0.4%

[% of Population Under 18 in Poverty](#pp_var_2314277592537816524)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`HIGH CORRELATION`\
`HIGH CORRELATION`\
`HIGH CORRELATION`\

Distinct

171

Distinct (%)

67.3%

Missing

0

Missing (%)

0.0%

Infinite

0

Infinite (%)

0.0%

Mean

22.24291339

Minimum

6.5

Maximum

44.4

Zeros

0

Zeros (%)

0.0%

Negative

0

Negative (%)

0.0%

Memory size

2.1 KiB

2021-10-07T19:32:10.372640image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#2314277592537816524bottom-2314277592537816524statistics)
-   [Histogram](#2314277592537816524bottom-2314277592537816524histogram)
-   [Common
    values](#2314277592537816524bottom-2314277592537816524common_values)
-   [Extreme
    values](#2314277592537816524bottom-2314277592537816524extreme_values)

Quantile statistics

Minimum

6.5

5-th percentile

10.965

Q1

17.4

median

22.05

Q3

26.6

95-th percentile

35.54

Maximum

44.4

Range

37.9

Interquartile range (IQR)

9.2

Descriptive statistics

Standard deviation

7.512877546

Coefficient of variation (CV)

0.3377649958

Kurtosis

0.1383133651

Mean

22.24291339

Median Absolute Deviation (MAD)

4.65

Skewness

0.4135450362

Sum

5649.7

Variance

56.44332903

Monotonicity

Not monotonic

2021-10-07T19:32:10.675898image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

26.2

5

 

2.0%

22.6

4

 

1.6%

20.4

4

 

1.6%

29

3

 

1.2%

23.4

3

 

1.2%

19.5

3

 

1.2%

11.7

3

 

1.2%

27

3

 

1.2%

22.2

3

 

1.2%

19.4

3

 

1.2%

Other values (161)

220

86.6%

-   [Minimum 5
    values](#2314277592537816524extreme_values-2314277592537816524firstn)
-   [Maximum 5
    values](#2314277592537816524extreme_values-2314277592537816524lastn)

Value

Count

Frequency (%)

6.5

2

0.8%

6.8

1

0.4%

7.1

1

0.4%

7.4

1

0.4%

8.3

1

0.4%

9

1

0.4%

9.3

1

0.4%

9.4

1

0.4%

10.2

1

0.4%

10.4

1

0.4%

Value

Count

Frequency (%)

44.4

1

0.4%

43.7

1

0.4%

43.2

1

0.4%

41.2

1

0.4%

40.5

1

0.4%

40.4

1

0.4%

40.3

1

0.4%

39

1

0.4%

38.1

1

0.4%

37.4

1

0.4%

Interactions {.page-header}
============

-   [Per Capita Income](#interactions-interactions_per-capita-income)
-   [Total Personal
    Income](#interactions-interactions_total-personal-income)
-   [Median Household
    Income](#interactions-interactions_median-household-income)
-   [Average Annual Pay](#interactions-interactions_average-annual-pay)
-   [% of Population in
    Poverty](#interactions-interactions_of-population-in-poverty)
-   [% of Population Under 18 in
    Poverty](#interactions-interactions_of-population-under-18-in-poverty)

-   [Per Capita
    Income](#interactions_per-capita-income-interactions_per-capita-income_per-capita-income)
-   [Total Personal
    Income](#interactions_per-capita-income-interactions_per-capita-income_total-personal-income)
-   [Median Household
    Income](#interactions_per-capita-income-interactions_per-capita-income_median-household-income)
-   [Average Annual
    Pay](#interactions_per-capita-income-interactions_per-capita-income_average-annual-pay)
-   [% of Population in
    Poverty](#interactions_per-capita-income-interactions_per-capita-income_of-population-in-poverty)
-   [% of Population Under 18 in
    Poverty](#interactions_per-capita-income-interactions_per-capita-income_of-population-under-18-in-poverty)

2021-10-07T19:31:54.836642image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:55.305599image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:55.535795image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:55.732796image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:55.983407image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:56.350482image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

-   [Per Capita
    Income](#interactions_total-personal-income-interactions_total-personal-income_per-capita-income)
-   [Total Personal
    Income](#interactions_total-personal-income-interactions_total-personal-income_total-personal-income)
-   [Median Household
    Income](#interactions_total-personal-income-interactions_total-personal-income_median-household-income)
-   [Average Annual
    Pay](#interactions_total-personal-income-interactions_total-personal-income_average-annual-pay)
-   [% of Population in
    Poverty](#interactions_total-personal-income-interactions_total-personal-income_of-population-in-poverty)
-   [% of Population Under 18 in
    Poverty](#interactions_total-personal-income-interactions_total-personal-income_of-population-under-18-in-poverty)

2021-10-07T19:31:56.592055image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:56.824927image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:57.038513image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:57.271560image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:57.548688image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:57.850936image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

-   [Per Capita
    Income](#interactions_median-household-income-interactions_median-household-income_per-capita-income)
-   [Total Personal
    Income](#interactions_median-household-income-interactions_median-household-income_total-personal-income)
-   [Median Household
    Income](#interactions_median-household-income-interactions_median-household-income_median-household-income)
-   [Average Annual
    Pay](#interactions_median-household-income-interactions_median-household-income_average-annual-pay)
-   [% of Population in
    Poverty](#interactions_median-household-income-interactions_median-household-income_of-population-in-poverty)
-   [% of Population Under 18 in
    Poverty](#interactions_median-household-income-interactions_median-household-income_of-population-under-18-in-poverty)

2021-10-07T19:31:58.052964image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:58.442281image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:58.779725image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:59.235539image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:59.481628image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:31:59.731831image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

-   [Per Capita
    Income](#interactions_average-annual-pay-interactions_average-annual-pay_per-capita-income)
-   [Total Personal
    Income](#interactions_average-annual-pay-interactions_average-annual-pay_total-personal-income)
-   [Median Household
    Income](#interactions_average-annual-pay-interactions_average-annual-pay_median-household-income)
-   [Average Annual
    Pay](#interactions_average-annual-pay-interactions_average-annual-pay_average-annual-pay)
-   [% of Population in
    Poverty](#interactions_average-annual-pay-interactions_average-annual-pay_of-population-in-poverty)
-   [% of Population Under 18 in
    Poverty](#interactions_average-annual-pay-interactions_average-annual-pay_of-population-under-18-in-poverty)

2021-10-07T19:32:00.232667image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:00.530640image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:00.850674image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:01.090392image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:01.333737image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:01.589500image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

-   [Per Capita
    Income](#interactions_of-population-in-poverty-interactions_of-population-in-poverty_per-capita-income)
-   [Total Personal
    Income](#interactions_of-population-in-poverty-interactions_of-population-in-poverty_total-personal-income)
-   [Median Household
    Income](#interactions_of-population-in-poverty-interactions_of-population-in-poverty_median-household-income)
-   [Average Annual
    Pay](#interactions_of-population-in-poverty-interactions_of-population-in-poverty_average-annual-pay)
-   [% of Population in
    Poverty](#interactions_of-population-in-poverty-interactions_of-population-in-poverty_of-population-in-poverty)
-   [% of Population Under 18 in
    Poverty](#interactions_of-population-in-poverty-interactions_of-population-in-poverty_of-population-under-18-in-poverty)

2021-10-07T19:32:01.817861image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:02.027642image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:02.311696image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:02.491586image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:02.648699image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:02.950188image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

-   [Per Capita
    Income](#interactions_of-population-under-18-in-poverty-interactions_of-population-under-18-in-poverty_per-capita-income)
-   [Total Personal
    Income](#interactions_of-population-under-18-in-poverty-interactions_of-population-under-18-in-poverty_total-personal-income)
-   [Median Household
    Income](#interactions_of-population-under-18-in-poverty-interactions_of-population-under-18-in-poverty_median-household-income)
-   [Average Annual
    Pay](#interactions_of-population-under-18-in-poverty-interactions_of-population-under-18-in-poverty_average-annual-pay)
-   [% of Population in
    Poverty](#interactions_of-population-under-18-in-poverty-interactions_of-population-under-18-in-poverty_of-population-in-poverty)
-   [% of Population Under 18 in
    Poverty](#interactions_of-population-under-18-in-poverty-interactions_of-population-under-18-in-poverty_of-population-under-18-in-poverty)

2021-10-07T19:32:03.206366image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:03.472905image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:03.709452image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:03.984725image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:04.333757image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

2021-10-07T19:32:04.678513image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Correlations {.page-header}
============

Toggle correlation descriptions

-   [Pearson's r](#correlations_tab-pearson)
-   [Spearman's ρ](#correlations_tab-spearman)
-   [Kendall's τ](#correlations_tab-kendall)
-   [Phik (φk)](#correlations_tab-phi_k)

2021-10-07T19:32:10.943631image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

### Pearson's r

The Pearson's correlation coefficient (*r*) is a measure of linear
correlation between two variables. It's value lies between -1 and +1, -1
indicating total negative linear correlation, 0 indicating no linear
correlation and 1 indicating total positive linear correlation.
Furthermore, *r* is invariant under separate changes in location and
scale of the two variables, implying that for a linear function the
angle to the x-axis does not affect *r*.\
\
To calculate *r* for two variables *X* and *Y*, one divides the
covariance of *X* and *Y* by the product of their standard deviations.

2021-10-07T19:32:11.269117image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

### Spearman's ρ

The Spearman's rank correlation coefficient (*ρ*) is a measure of
monotonic correlation between two variables, and is therefore better in
catching nonlinear monotonic correlations than Pearson's *r*. It's value
lies between -1 and +1, -1 indicating total negative monotonic
correlation, 0 indicating no monotonic correlation and 1 indicating
total positive monotonic correlation.\
\
To calculate *ρ* for two variables *X* and *Y*, one divides the
covariance of the rank variables of *X* and *Y* by the product of their
standard deviations.

2021-10-07T19:32:11.608565image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

### Kendall's τ

Similarly to Spearman's rank correlation coefficient, the Kendall rank
correlation coefficient (*τ*) measures ordinal association between two
variables. It's value lies between -1 and +1, -1 indicating total
negative correlation, 0 indicating no correlation and 1 indicating total
positive correlation. \
\
To calculate *τ* for two variables *X* and *Y*, one determines the
number of concordant and discordant pairs of observations. *τ* is given
by the number of concordant pairs minus the discordant pairs divided by
the total number of pairs.

2021-10-07T19:32:11.941779image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

### Phik (φk)

Phik (φk) is a new and practical correlation coefficient that works
consistently between categorical, ordinal and interval variables,
captures non-linear dependency and reverts to the Pearson correlation
coefficient in case of a bivariate normal input distribution. There is
extensive documentation available
[here](https://phik.readthedocs.io/en/latest/index.html).

Missing values {.page-header}
==============

-   [Count](#missing-bar)
-   [Matrix](#missing-matrix)

2021-10-07T19:32:05.217470image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

A simple visualization of nullity by column.

2021-10-07T19:32:05.979011image/svg+xmlMatplotlib v3.4.2,
https://matplotlib.org/

Nullity matrix is a data-dense display which lets you quickly visually
pick out patterns in data completion.

Sample {.page-header}
======

First rows {.indent}
----------

County

Per Capita Income

Total Personal Income

Median Household Income

Average Annual Pay

% of Population in Poverty

% of Population Under 18 in Poverty

0

Anderson

36027

2080020000

48461

45799

19.8

23.8

1

Andrews

51769

968334000

74918

69845

10.2

12.7

2

Angelina

39644

3437761000

51750

40974

15.6

22.6

3

Aransas

51614

1213451000

53085

39316

18.7

32.1

4

Archer

52335

447617000

63731

38006

10.3

12.8

5

Armstrong

53422

100807000

64424

42240

10.6

16.7

6

Atascosa

37644

1925578000

57309

55264

14.7

19.0

7

Austin

51118

1535171000

68311

49650

11.1

17.0

8

Bailey

44665

312657000

46174

39542

15.9

25.8

9

Bandera

44925

1038296000

59604

37215

12.9

23.6

Last rows {.indent}
---------

County

Per Capita Income

Total Personal Income

Median Household Income

Average Annual Pay

% of Population in Poverty

% of Population Under 18 in Poverty

244

Willacy

27584

589147000

35821

37959

30.5

38.1

245

Williamson

53145

31384616000

92661

61857

5.4

6.5

246

Wilson

46448

2372083000

76905

41496

8.3

11.7

247

Winkler

63667

509969000

64894

69953

12.5

17.9

248

Wise

44870

3140164000

70468

48240

8.3

11.7

249

Wood

39803

1812585000

56945

38780

14.3

22.3

250

Yoakum

44932

391489000

62636

65683

10.6

14.9

251

Young

50732

913684000

52643

43489

13.6

20.4

252

Zapata

28936

410289000

36069

52913

30.1

43.7

253

Zavala

30779

364421000

32538

39689

29.6

40.4

Report generated with
[pandas-profiling](https://github.com/pandas-profiling/pandas-profiling).
