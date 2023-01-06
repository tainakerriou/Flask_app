from pytrends.request import TrendReq
from flask import Flask
from datetime import datetime
import time
import collections
app = Flask(__name__)



def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

@log_execution_time
def foo():
    # function code goes here
    time.sleep(1)

foo()



def count_words_dict(text):
    word_count = {}
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def count_words_counter(text):
    words = text.split()
  
  # Utilisez la fonction Counter pour compter le nombre d'apparitions de chaque mot
    word_counts = collections.Counter(words)
  
  # Renvoyez le dictionnaire des comptes de mots
    return word_counts
   # return collections.Counter(text.split())

with open('t8.shakespeare.txt', 'r') as f:

  text = f.read()

text2="ok ok ok ok ok"

def measure_time(func1, func2, text):
  # Mesurez le temps d'exécution de la première fonction
  start = time.time()
  func1(text)
  end = time.time()
  time1 = end - start
  
  # Mesurez le temps d'exécution de la deuxième fonction
  start = time.time()
  func2(text)
  end = time.time()
  time2 = end - start
  
  # Affichez les temps d'exécution des deux fonctions
  print(f'Function 1 took {time1:.6f} seconds')
  print(f'Function 2 took {time2:.6f} seconds')


measure_time(count_words_dict, count_words_counter, text)








@app.route('/trend', methods=["GET"])
def trend():

    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list=['avatar','streaming']
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
                    "borderColor": '#ff0000',
                    "fill": 'false',
                },
                {
                    "label": 'Inception',
                    "data": inception_data,
                    "borderColor": '#00ff00',
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