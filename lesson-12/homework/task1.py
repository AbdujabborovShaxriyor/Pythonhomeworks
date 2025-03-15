from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>"""

soup = BeautifulSoup(html,"html.parser")
body = soup.body
for tr in body:
    print(soup.td.text)
conditions = {}
temperature = {}
tr_elements = soup.find_all("tr")
for tr in tr_elements[1:]:
    td_elements = tr.find_all("td")
    if len(td_elements)>2:
        temperature[td_elements[0]]=[(td_elements[1].text.replace("°C",""))]
        conditions[td_elements[2].text]=[td_elements[0]]
for condition,day in conditions.items():
    if condition.lower()=="sunny":
        print(day)
temps = []
for temp in temperature.values():
    temps.append(temp)
biggest = max(temps)
if biggest in temperature.values():
    print(temp[biggest])
sum=0
for temp in temperature.key():
    sum+=temp
print(f"Average value of temperature is: {sum/len(temperature)}")