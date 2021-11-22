import redis
from .conf import REDIS_HOST, REDIS_PORT, REDIS_NAME

redis_pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, max_connections=20)


class RedisOperator(object):
    def __init__(self):
        self.connection = redis.Redis(connection_pool=redis_pool)

    def _gets(self, total=1):
        tmp = self.connection.srandmember(REDIS_NAME, total)
        return [s.decode('utf-8') for s in tmp]

    def _puts(self, proxies):
        return self.connection.spop(REDIS_NAME, *proxies)

    def _pop(self):
        return self.connection.spop(REDIS_NAME).decode('utf-8')

    # 将方法变成属性调用
    @property
    def _size(self):
        return self.connection.scard(REDIS_NAME)

    def _flush(self):
        return self.connection.flushall()