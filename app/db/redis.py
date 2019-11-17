class RedisConnection():
    """
    Class follow a Singleton pattern to get 
    Redis client asyn connection
    
    Arguments:
        object {[type]} -- [description]
    """

    def __new__(self):
        if self.connector == None:
            self.connector = redis.client()

    def connected(self):
        return True


