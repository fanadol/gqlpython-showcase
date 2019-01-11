# graphql-python showcase

This directory contain graphql-python example and simple REST API using `DJANGO REST FRAMEWORK`

## Get Started

**Clone the repository**

**Install Dependencies**

```sh
pip install -r requirements.txt
```

**Make Migration**

```sh
python manage.py migrate
```

**Load Initial Data**

```sh
python manage.py loaddata data.json
```

**Run It !**

```
python manage.py runserver
```


## Testing

Open your browser at localhost:8000/graphql

**Query Example**
```graphql
{
    people{
        id
        fullName
        email
        }
    }
}
```

The server returns the following response:
```json
{
  "data": {
    "people": [
      {
        "id": 1,
        "fullName": "Michael Suyama",
        "email": "suyama@wp.co"
      },
      {
        "id": 2,
        "fullName": "Nancy DaVolio",
        "email": "davolio@wp.co"
      },
      {
        "id": 3,
        "fullName": "David Buchanan",
        "email": "buchanan@wp.co"
      }
    ]
  }
}
```

**REST API:**

We can also do a `GET` request to `localhost:8000/posts/` and `localhost:8000/people/`

The server returns the following response:

![alt text](https://imgur.com/a/0AtDU1j)