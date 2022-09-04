
import mysql.connector
from tabulate import tabulate


db = mysql.connector.connect(host="localhost", user="root", passwd="root",database = "handson")
mc = db.cursor()


def sc():
    while True:
        mc.execute("select * from scores")
        # db.commit()
        results = mc.fetchall()

    print(tabulate(results, headers=['gID', 'UserName', 'No_of_GamesPlayed', 'Player_Score', 'AI_Score', 'No_of_Draws',
                                     'Overall_PlayerWinorLose'], tablefmt='psql'))