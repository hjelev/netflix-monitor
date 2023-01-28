# Netflix Browser Monitor

Python script to check if you are watching Netflix in Chrome browser and send a MQTT status message. 

The script is running constantly and checking every 10 seconds if you have a browser tab with netflix site opened. If such tab is discovered a mqtt massage is send to the broker.

The monitor sends a message with configurable prefix and name netflix. The message is None if no browser is started, False if there is a browser but no netflix is discovered and True if you are watching Netflix in the browser.

## Installation
Copy config.py.example as config.py and update your mqtt credentials.

Create a shortcut of netflix.pyw in `shell:startup`

Restart your computer.

## Add sensor to Home Assistant

If you want to use this as mqtt sendor in Home Assistant add this to your configuration.yaml file.

```
mqtt:
  sensor:
  - unique_id: netflix
    state_topic: "netflix_monior/netflix"
```