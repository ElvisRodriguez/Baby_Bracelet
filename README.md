# Atawear

## Product Information for Atawear (baby bracelet)

### User Story:
As a parent/guardian, I want to make sure my infant's heart rate is normal without manually reading their heartbeat. I want to be able to ensure this while being away from my infant, on my phone, work desk, etc.

### Demographic:
Infants of or under 2 years of age.

### Product Description:
Users will use their phone to set up the bracelet's connection to their wifi and can view the infant's heart rate information on our website or through an app on their phone. Users will receive a notification (similar to an amber alert) to notify them of an abnormal change in heart rate.

### Product Design:

### Hardware:
#### Raspberry Pi Zero-W:
- 1GHz, Single-core CPU
- 512MB RAM
- Mini HDMI and USB On-The-Go ports
- Micro USB power
- HAT-compatible 40-pin header
- Composite video and reset headers
- CSI camera connector
- 802.11n wireless LAN
- Bluetooth 4.0

#### Pulse Sensor (Heart Rate Sensor):
- Analog output
- Size: 0.625”(Diameter) and 0.125”(Thick)
- Designed for Plug and Play
- Works with any MCU with an ADC
- Input voltages: 3.3V-5V
- Supply current: 3-4mA

#### Analog to Digital Converter(ADS1015 12-Bit ADC):			           
- Input voltages: 2.0V-5.5V
- Size:(2mm x 1.5mm x 0.4mm)
- Operating temperature: (-40°C)-(+125°C)
- 4 Single-ended or two differential inputs
- 12-Bit noise-free resolution
- Low current consumption: 150mA
- Programmable data rate: (128SPS)-(3.3kSPS)

### Software:
#### Android Application:
- Webview of application hosted at (elvisrodriguez.pythonanywhere.com).
- Amber Alert-like alerts for abnormal changes in heart rate.
- Interface for connecting hardware (pi zero) to user's wifi.

#### Web Application:
- Graph Representation of heart rate data, showing readings along with a timestamp of when they were read.
- Listens for data from pi zero, uses the most recent 30 readings for graph display, and the most recent 100 for data analysis (explained below).
- Application implemented using Python's Flask and Dash frameworks.

#### Data Analytics:
- Heart Rate data read by Pulse Sensor, data is transformed by python script by averaging the interbeat intervals of heartbeats (the time between two heartbeats) to produce a more accurate heart rate reading. Data is then streamed to a web server, formatted into a string along with a timestamp of when it arrived and displayed in a graph.
- In addition to displaying heartbeat data, the data is also used to detect severe spikes or drops in heart rate, notifying the user thereafter. Detection is calculated by taking the most recent 100 readings and computing the deviation from the average.
- Atrial Fibrillation is an irregular heartbeat that can lead to blood clots, stroke, heart failure among other complications. Due to already computing the interbeat interval, our application can also detect an episode of Atrial Fibrillation by computing the standard deviation of a collection of intebeat intervals.
