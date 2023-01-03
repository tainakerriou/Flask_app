from pytrends.request import TrendReq
from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/trend', methods=["GET"])
def trend():

    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list=['avatar','inception']
    pytrends.build_payload(kw_list, timeframe='2022-01-09 2023-01-01', geo='US')
    df = pytrends.interest_over_time()
    avatar_data = df['avatar'].values.tolist()
    inception_data = df['inception'].values.tolist()
    dates = df.index.values.tolist()
    timestamp_in_seconds=[element/1e9 for element in dates]
    date= [datetime.fromtimestamp(element) for element in timestamp_in_seconds]
    days=[element.date() for element in date]
    months=[element.isoformat() for element in days]
    

    params = {
        "type": 'line',
            "data": {
                "labels": months,
                "datasets": [{
                    "label": 'Avatar',
                    "data": avatar_data,
                    "borderColor": '#3e95cd',
                    "fill": 'false',
                },
                {
                    "label": 'Inception',
                    "data": inception_data,
                    "borderColor": '#ffce56',
                    "fill": 'false',
                }
                ]
            },
            "options": {
                "title": {
                    "text": 'My Line Chart'
                },
                "scales": {
                    "yAxes": [{
                        "ticks": {
                            "beginAtZero": 'true'
                        }
                    }]
                }
            }
    }
    
    
    
    prefix_google = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>

    <canvas id="myChart" width="50" height="50"></canvas>""" + f"""
    <script>
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {params});
    </script>


    
    """

    return prefix_google

if __name__ == '__main__':
    app.run()