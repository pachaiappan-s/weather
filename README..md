
# Weather App 🌦️

## 📌 Purpose
This project is a simple **Weather App** written in Python.  
It fetches real-time weather information for any city or ZIP code using the **OpenWeatherMap API**.

---

## ⚙️ How It Works
1. User enters a **city name** or **ZIP code**.  
2. The program sends a request to the **OpenWeatherMap API**.  
3. Weather data is retrieved and displayed, including:  
   - City & Country  
   - Temperature (°C)  
   - Humidity (%)  
   - Weather Condition  

---

## 🔑 Requirements
- Python 3.x  
- `requests` library  
- An API key from [OpenWeatherMap](https://openweathermap.org/api)  

Install dependencies:
```bash
pip install requests
```

---

## 🚀 Usage
Run the program with:
```bash
python weather.py
```

Enter a city name (e.g., `London`) or a ZIP code (e.g., `10001`).  

---

## 📊 Example Run
**Input:**  
```
Enter city name or ZIP code: London
```

**Output:**  
```
--- Current Weather ---
Location: London, GB
Temperature: 15°C
Humidity: 82%
Condition: Cloudy
-----------------------
```

---

## 📝 Notes
- Replace the placeholder API key in the code with your own OpenWeatherMap API key.  
- If the location is invalid, an error message will be displayed.  

---
