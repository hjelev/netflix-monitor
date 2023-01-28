# Netflix Browser Monitor

Python script to check if you are watching Netflix in Chrome browser and send a MQTT status message. 

The script is running constantly and checking every 10 seconds (this value is configurable in config.py) if you have a browser tab with netflix site opened.

The monitor sends a message with configurable prefix and name netflix. The message is None if no browser is started, False if there is a browser but no netflix is discovered and True if you are watching Netflix in the browser.

## Installation

1. Clone this repository.

2. Copy config.py.example as config.py and update your mqtt credentials.

3. Create a shortcut of netflix.pyw in `shell:startup`

4. Add sensor to Home Assistant.

5. Restart your computer.

## Add sensor to Home Assistant

If you want to use this as mqtt sendor in Home Assistant add this to your configuration.yaml file.

```
mqtt:
  sensor:
  - unique_id: netflix
    state_topic: "netflix_monior/netflix"
```