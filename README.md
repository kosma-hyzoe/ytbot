# Kantar interview task

## How to run

1. Install requirements from `requirements.txt`
1. Modify configuration in `config.py` if needed
1. Run `python3 core.py`

## Task description

* Implement a browser automation application. The automation should perform the following steps.
* Open Chrome browser installed on the hosting system
* Browse to https://www.youtube.com
* Search for “Python” and select the first video in the resulting list
* Wait until a potential pre-roll ad has been shown
* Drag the video slidebar to aprox. the middle of the video
* Play the video
* Mute the video
* Read the following info from the website and write it to standard out:
    * title of the video
    * duration of the video
    * name of the channel
    * amount of views
    * date of upload
    * amount of likes and amount of dislikes
* Switch to the first video in the “next video” panel on the right
* Play this video until it reaches 10 seconds and pause it afterwards

## Todo

### Urgent

### Important

### Other

* better locator for "accept all button"
* move config to json if the project scales