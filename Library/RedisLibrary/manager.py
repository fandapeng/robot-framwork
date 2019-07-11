# -*- coding: utf-8 -*-
# coding: utf-8

import redis

from robot.libraries.BuiltIn import BuiltIn


class RedisManager(object):

    def __init__(self):

        self._builtin = BuiltIn()
        self._redisconnection = None

    def connect_to_redis(self, connect_string):

        """
        
        连接redis

        | connect to redis | host=172.16.23.206, port=6379, db=4 , password=password | 
        | connect to redis | host=172.16.23.206, port=6379, db=4 | 

        """

        connect = 'redis.ConnectionPool(%s)' % connect_string
        pool = eval(connect)
        self._redisconnection = redis.Redis(connection_pool=pool)

    def get_from_redis(self, key):
        """
        通过key来获取value

        | get from redis | USER_LOGIN_ERR_TIMES_1380000111 |

        """

        value = self._redisconnection.get(key)
        self._builtin.log("GET {0} ---> {1}".format(key,value))
        return value

    def delete_from_redis(self, key):
        """
        删除key

        | delete from redis | USER_LOGIN_ERR_TIMES_1380000111 |
        """
        if self._redisconnection.delete(key):
            self._builtin.log("DEL {0} Success".format(key))
        else:
            self._builtin.log("DEL {0} Fail or No key".format(key))

    def disconnect_from_redis(self):
        """
        断开redis连接

        | disconnect_from_redis |
        """
        self._redisconnection = None


if __name__ == '__main__':

    a = RedisManager()
    a.connect_to_redis("host='172.16.23.206', port=6379, db=4 , password='sider'")
    v = a.get_from_redis('JLT_CONTRACT_NO_INCREMENT')
    print v

