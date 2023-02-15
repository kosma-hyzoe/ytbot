# Kantar interview task

## How to run

1. Install requirements from `requirements.txt`
1. Modify configuration in `ytbot/config.py` if needed
1. Run `python3 -m ytbot` in the repo directory

To run tests, you can simply run `pytest` while in repo directory
or a directory containing the repo directory.

## Task description

Implement a browser automation application. The automation should perform
the following steps:

1. Open Chrome browser installed on the hosting system
1. Browse to https://www.youtube.com
1. Search for “Python” and select the first video in the resulting list
1. Wait until a potential pre-roll ad has been shown
1. Drag the video slidebar to aprox. the middle of the video
1. Play the video
1. Mute the video
1. Read the following info from the website and write it to standard out:
   * title of the video
   * duration of the video
   * name of the channel
   * amount of views
   * date of upload
   * amount of likes and amount of dislikes
1. Switch to the first video in the “next video” panel on the right
1. Play this video until it reaches 10 seconds and pause it afterwards