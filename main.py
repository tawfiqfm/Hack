import mysql.connector as mysql
from gui import gui_attributes


def main():
    db = mysql.connect(
        host="localhost",
        database="hack",
        user="fmoham3",
        passwd="f123",
        auth_plugin='mysql_native_password')
    print()
    print(gui_attributes())
    userData = gui_attributes()
    id = 1
    race1 = userData[0]
    gender1 = userData[1]
    history1 = userData[2]
    film1 = userData[3]
    sport1 = userData[4]
    insert_data(db, id, race1, gender1, history1, film1, sport1)
    # while True:
    #     s = input("If you would like to view data, press v\nIf you would like to insert data, press i\nOtherwise "
    #               "press x: ")
    #     if s[0] == 'v':
    #         view_data(db)
    #
    #     if s[0] == 'x':
    #         break


def insert_data(db, id, race, gender, history, film, sport):
    cursor = db.cursor()
    query = '''INSERT INTO ATTRIBUTE (id, race, gender, history, film, sport) VALUES (%s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (id, race, gender, history, film, sport))
    cursor.close()
    db.commit()


def view_data(db):
    cursor = db.cursor()
    query = '''SELECT * FROM ATTRIBUTE'''
    cursor.execute(query)
    for (id, race, gender, history, film, sport,) in cursor:
        print(
            " ID       {0:} \n RACE   {1:} \n GENDER  {2:}  \n HISTORY {3:} \n FILM    {4:} \n SPORT   {5:}  \n ".format(
                id, race, gender, history, film, sport, ))
        print()
    cursor.close()


main()
