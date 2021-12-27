import redis

r = redis.Redis(host='localhost', port='6379', db=0, password='Buixuantoan@916263')
r.ping()