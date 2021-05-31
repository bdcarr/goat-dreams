## What is it
Just a script to run [Big Sleep](https://github.com/lucidrains/big-sleep) with a list of inputs and save the results in subfolders.

## Example
input.txt:
```
raw fish stays raw for ages
Keep wishing bot. You will never win!
an alien moon eating the ocean
```

In your terminal:
```sh
py goat_dreams.py input.txt
```

Result:
```
output/
    raw-fish-stays-raw-for-ages/
        raw_fish_stays_raw_for_ages.0.png
        ...
        raw_fish_stays_raw_for_ages.89.png
        raw_fish_stays_raw_for_ages.best.png
        raw_fish_stays_raw_for_ages.png
    keep-wishing-bot-you-will-never-win/
        ...
    an-alien-moon-eating-the-ocean/
        ...
input.txt
goat_dreams.py
README.md
```

## Prerequisites
* [Big Sleep](https://github.com/lucidrains/big-sleep)
* Whatever you need to run Big Sleep