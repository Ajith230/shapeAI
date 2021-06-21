from datetime import datetime

import requests as rqst

api_key = "7ee7893ed223a4cbe2a3001ddefceb96"
degree_sign = '\u00b0'
city_name = input("Enter your City name : ")
def connect_to_wether_api():
    api_connect = rqst.get("http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key)
    return api_connect
def fetch_weather_data(weather_data):
    city_temp = round(float(((weather_data['main']['temp']) - 273.15)), 2)
    city_temp_real_feal = round(float(((weather_data['main']['feels_like']) - 273.15)), 2)
    weather_desc = (weather_data['weather'][0]['description'])
    humidity = (weather_data['main']['humidity'])
    wind_speed = str((weather_data['wind']['speed'])) + " Kmph"
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
    formatted_output = ""
    formatted_output += '\n Current Timestamp : '+timestampStr
    formatted_output += '\n City Name : '+ city_name
    formatted_output += '\n Current   Temparture : ' + str(city_temp)+degree_sign+'C'
    formatted_output += '\n Real feal Temparture : ' + str(city_temp_real_feal) + degree_sign + 'C'
    formatted_output += '\n Weather Description  : ' + weather_desc
    formatted_output += '\n Humiidty   : ' + str(humidity)
    formatted_output += '\n Wind Speed : ' + wind_speed
    return formatted_output


weather_data = connect_to_wether_api().json()
weather_data_formatted = fetch_weather_data(weather_data)
print(weather_data_formatted)
file_write = open("weatherinfo.txt","w")
file_write.write(weather_data_formatted)