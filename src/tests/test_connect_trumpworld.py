#!/usr/bin/env python3
"""Test connecting to Buzzfeed's Trump World database on Neo4j"""

__copyright__ = 'Copyright (C) 2019, https://github.com/datapol. All rights reserved.'

# pylint: disable=superfluous-parens,import-error,undefined-loop-variable
import os
import xlsxwriter
from neo4j import GraphDatabase
from py2neo import Database
from py2neo import Graph
from muellerreport.organizations import ORGANIZATION2DESC
from muellerreport.persons import PERSON2DESC

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")


def test_connect():
    """Test connecting to Buzzfeed's Trump World database on Neo4j"""
    # :server status
    uri = 'bolt://ws-10-0-1-52-39706.neo4jsandbox.com:443'
    password ='Burf5Pink!'
    # gdbdr = GraphDatabase.driver(uri, auth=('neo4j', password))
    db = Database(uri)
    graph = Graph(uri)
    cypher = ('MATCH (o:Organization)-[r]-() '
              'RETURN o.name, count(*), collect(distinct type(r)) AS types '
              'ORDER BY count(*) DESC '
              'LIMIT 5')
    graph.evaluate(cypher)
    print(db)
    print(graph)


if __name__ == '__main__':
    test_connect()

# Copyright (C) 2019, https://github.com/datapol. All rights reserved.
