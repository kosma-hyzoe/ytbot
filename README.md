# Kantar interview task

## How to run

1. Install requirements from `requirements.txt`
1. Modify configuration in `ytbot/config.py` if needed
1. Run `python3 -m ytbot` in the repo directory

Test with `pytest`.

## Issues and limitations

pytest doesn't recognize the `humanfriendly` library well when
run from command line, works in an IDE though. I consider it
low-priority for now, but will try to fix it soon.

## Task description

Implement a browser automation application which performs
the following steps:

1. Open Chrome browser installed on the hosting system
1. Navigate to https://www.youtube.com
1. Search for 'Python' and select the first video from the results list
1. Wait until a potential pre-roll ad has been shown
1. Drag the video duration slider to approx. the middle of the video
1. Mute the video
1. Read the following info from the website and write it to standard out:
   * Title of the video
   * Duration of the video
   * Name of the channel
   * Amount of views
   * Date of upload
   * Amount of likes
   * Amount of dislikes
1. Switch to the first suggested video in the 'next' panel on the right
1. Play the video until 10 seconds of it have elapsed
1. Pause the video afterwards