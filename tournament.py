#!/usr/bin/env python
#
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def commit_st(func):
    """ Cusror func. With this function we shouldn`t write commit every time  """
    def wrapper(*args, **kwargs):
        conn = connect()
        cursor = conn.cursor()
        fun = func(cursor, *args, **kwargs)
        conn.commit()
        conn.close()
        return fun
    return wrapper


@commit_st
def deleteMatches(cursor):
    """Remove all the match records from the database."""
    query = "DELETE FROM matches"
    cursor.execute(query)


@commit_st
def deletePlayers(cursor):
    """Remove all the player records from the database."""
    query = "DELETE FROM players"
    cursor.execute(query)


@commit_st
def countPlayers(cursor):
    """Returns the number of players currently registered."""
    query = "SELECT count(*) as players_num FROM players;"
    cursor.execute(query)
    results = cursor.fetchall()
    return results[0][0]


@commit_st
def registerPlayer(cursor, name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    query = "INSERT INTO players VALUES (%s)"
    cursor.execute(query, (name,))


@commit_st
def playerStandings(cursor):
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = ("SELECT players.id, name, wins, matches FROM players "
             "JOIN wins ON players.id = wins.id "
             "JOIN matches_played ON players.id = matches_played.id "
             "ORDER BY wins DESC")
    cursor.execute(query)
    return cursor.fetchall()


@commit_st
def reportMatch(cursor, winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "INSERT INTO matches VALUES(%s, %s)"
    cursor.execute(query, (winner, loser))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    player_standings = playerStandings()
    pairing_list = []
    start = 0
    for i in range(2, len(player_standings) + 1, 2):
        player1, player2 = player_standings[start:i]
        start = i
        players = (player1[0], player1[1], player2[0], player2[1])
        pairing_list.append(players)
    return pairing_list