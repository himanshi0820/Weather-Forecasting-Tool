# Weather-Forecasting-Tool

A command-line tool build using python that accepts a city's name and returns it's current weather forecast.

## Python Libraries

The following Python libraries were used in the development of the project.
- [requests](https://requests.readthedocs.io/en/latest/) - Used to request data.
- [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - Used to create ASCII texts.
- [argparse](https://docs.python.org/3/library/argparse.html) - Used to write user-friendly command-line interfaces.
- [simple chalk](https://pypi.org/project/simple-chalk/) - Used for terminal string styling

## Installation
- First install required python libraries using following commands.
```bash
  pip install requests
```
```bash
  pip install pyfiglet
```
```bash
  pip install argparse 
```
```bash
  pip install simple-chalk
```
- Next, obtain a free API key by signing up with [OpenWeatherMap](https://openweathermap.org/api). The free API key is limited to 1,000 calls per day.
- Clone this repository and create a local copy on your machine using this command:
```bash
  git clone https://github.com/Himanshigarg08/WeatherCLI.git
```
- Update variable ```API_KEY``` in ``` WeatherCLI\main.py``` and run the file.
