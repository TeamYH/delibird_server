# Delibird Server

## Members :blush:

| [asdeszqsc](https://github.com/asdeszqsc) | [baehaejin](https://github.com/baehaejin) | [hhhhjjjj96](https://github.com/hhhhjjjj96) | [hyunjun-cho](https://github.com/hyunjun-cho) | [SexyJiny](https://github.com/SexyJiny) |
| :---------------------------------------: | :---------------------------------------: | :-----------------------------------------: | :-------------------------------------------: | :-------------------------------------: |
|                  안윤회                   |                  배해진                   |                   박현진                    |                    조현준                     |                 정진희                  |
|                                           |                                           |                                             |                                               |
|              Frontend design              |              backend server               |           robot node programming            |          robot simulator programming          |             hardware Design             |

---

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/TeamYH/delibird_server.git
$ cd delibird_server
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd delibird_server
(env)$ python manage.py runserver
```

### Data URL
* Add counsel:
    * POST http://localhost:8000/superuser_db/counsel_list?customer=a&phonenum=b&email=c&comment=d
* Get Counsel List:
    * GET http://localhost:8000/superuser_db/counsel_list
* Add Store Table Data (Data with json request format):
    * POST http://localhost:8000/delibird_db/table_list
* Get Table List:
    * GET http://localhost:8000/delibird_db/table_list
