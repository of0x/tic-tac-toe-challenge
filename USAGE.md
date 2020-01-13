# How to Setup and Run the Tic Tac Toe Service

## Installation and Starting the Server
To install the dependencies, run 
`pip install -r requirements.txt`, 
then run
```buildoutcfg
chmod +x run_server.py
./run_server.py
```
to start the server, running on localhost.

## APIs
Here are [cURL](https://curl.haxx.se/) commands for localhost for the APIs specified in the [README.md](README.md)
* GET

    `curl -X GET http://127.0.0.1:5000/api/games`
 
 returns a json list:
 ```
     [
      {
        "board": "_,_,_,_,_,_,_,_,_",
        "firstPlayer": null,
        "id": 1,
        "secondPlayer": null
      },
      {
        "board": "0,_,_,_,_,_,_,_,1",
        "firstPlayer": "alice",
        "id": 2,
        "secondPlayer": "bob"
      }
    ]

```
 
* POST 
```
    curl -X POST \
      http://127.0.0.1:5000/api/games \
      -H 'Content-Type: application/json' \
      -H 'Host: 127.0.0.1:5000' \
      -d '{
        "board": "0,_,_,_,_,_,_,_,1",
        "firstPlayer": "alice",
        "secondPlayer": "bob"
    }'
```

   returns
    
```
    {
      "board": "0,_,_,_,_,_,_,_,1", 
      "firstPlayer": "alice", 
      "id": 3, 
      "secondPlayer": "bob"
    }
```

* GET for a specific id
```
    curl -X GET \
      http://127.0.0.1:5000/api/games/3
```
returns
```
    {
      "board": "0,_,_,_,_,_,_,_,1", 
      "firstPlayer": "alice", 
      "id": 3, 
      "secondPlayer": "bob"
    }
```

* POST for a specific id with a specific field:
```
curl -X POST \
  http://127.0.0.1:5000/api/games/3 \
  -H 'Content-Type: application/json' \
  -d '{
    "board": "0,0,1,_,_,_,_,_,1"
}'
```

returns

```
    {
      "board": "0,0,1,_,_,_,_,_,1", 
      "firstPlayer": "alice", 
      "id": 3, 
      "secondPlayer": "bob"
    }

```

Both GET and POST for specific ids that are not found return HTTP Status 404.

There is one API not specified in the README, but added for completeness.

* DELETE
```
curl -X DELETE \
  http://127.0.0.1:5000/api/games/1
```
returns
```
    {}
```
with a 200 status on success and a HTTP status 404 if the id is not found.

## Tests
Any usable, enduring software must have tests. This solution includes tests for the [model](./tictactoe/test_models.py) (the games DB) and the [views](./tictactoe/test_views.py) (in flask, views are the various URL routes)
