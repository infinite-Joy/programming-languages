library(nycflights13)
library(tidyverse)

flights

jan <- filter(flights, month == 1, day == 1)

jan

(dec25 <- filter(flights, month == 12, day == 25))

df <- tibble(x = c(1, NA, 3))

df

filter(df, x > 1)

filter(df, is.na(x) | x > 1)

flights

filter(flights, arr_time - sched_arr_time >= 200)

filter(flights, dest == "IAH" | dest == "HOU")

1 + x != 1

x

head(flights)

filter(flights,
       abs(dep_delay) < 60 & arr_delay > 200)

filter(flights,
       abs(dep_delay) > 59 & arr_delay < 30)

count(filter(flights,
       abs(dep_delay) > 59 & arr_delay < 30))

# filter_cond <- dep_time >= 0 & dep_time <=600
filter(flights, dep_time >= 0 & dep_time <= 600)

count(filter(flights, dep_time >= 0 & dep_time <= 600))

filter(flights, is.na(dep_time))

count(filter(flights, is.na(dep_time)))

dd <- filter(flights, carrier == "EV" & flight == 4308)
dd[with(dd, order(year, month, day)), ]

dd <- filter(flights, carrier == "AA" & flight == 791)
dd[with(dd, order(year, month, day)), ]

filter(flights, carrier == "AA" & flight == 791 & is.na(dep_time))


