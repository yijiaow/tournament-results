#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect(database_name='tournament'):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect('dbname={}'.format(database_name))
        c = db.cursor()
        print 'connect'
        return db, c
    except:
        print('<error message')

def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    c.execute('DELETE FROM matches;')
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    c.execute('DELETE FROM players;')
    db.commit()
    db.close()
    print 'deletePlayers'

def countPlayers():
    """Returns the number of players currently registered."""
    db, c = connect()
    c.execute('SELECT COUNT (id) AS num_of_players FROM players;')
    count = c.fetchone()[0]
    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    c.execute('INSERT INTO players(name) VALUES (%s);', (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    c.execute('SELECT * FROM standings;')
    player_standings = c.fetchall()
    return player_standings
    db.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    c.execute('INSERT INTO matches(winner, loser) VALUES (%s, %s);', (winner, loser,))
    db.commit()
    db.close()
 
 
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
    pairs = []
    for i in range(0, len(player_standings), 2):
        player1, player2 = player_standings[i], player_standings[i+1]
        pairs.append((player1[0], player1[1], player2[0], player2[1]))
    return pairs



