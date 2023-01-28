from pywinauto import Application
import paho.mqtt.client as paho
import time
import config as c


def get_url():
    try:
        app = Application(backend='uia')
        app.connect(title_re=f".*{c.browser}.*")
        element_name="Address and search bar"
        dlg = app.top_window()
        url = dlg.child_window(title=element_name, control_type="Edit").get_value()
    except:
        return None

    if any(ext in url for ext in c.sites_to_check):
        url = True
    else:
        url = False

    return(url)


def send_message(url):
    try:
        client = paho.Client()
        client.username_pw_set(c.mqtt_user, c.mqtt_password)
        client.connect(c.mqtt_host, int(c.mqtt_port))
        client.publish(c.mqtt_topic_prefix + "/url", url, qos=1)
        client.disconnect()
    except:
        print("Coudln't sent MQTT message!")


if __name__ == '__main__':
    while True:
        url = get_url()
        send_message(url)
        time.sleep(10)