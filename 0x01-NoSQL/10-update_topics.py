#!/usr/bin/env python3
'''Module.
'''


def update_topics(mongo_collection, name, topics):
    '''Function that changes all topics of a collection's document based on
        the name. the function updated the topics where the attribute name is
        specify
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
