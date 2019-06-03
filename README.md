# messenger-stats
Script to compute metrics for your messenger conversations

## Instructions

### Step 1
Go to https://www.facebook.com/dyi/ to download your information (make sure you download it in json format).
This may take a while.


### Step 2
Clone this repo
```
$ git@github.com:Atyansh/messenger-stats.git
```

### Step 3
You're going to need to install `wordcloud`. You may want to do this in a virtual environment but that's entirely up to you.
```
$ virtualenv msg_stats
$ pip install wordcloud
```

### Step 4
* Open `constants.py` in your favorite editor.
* Edit the `FILENAME` variable to point to whichever messenger conversation you want to work with.
* Change the constants `PRINT_STATS` or `GENERATE_WORDCLOUD` to your liking.

### Step 5
```
$ python parse.py
```
