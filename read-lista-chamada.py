import csv
from pymongo import MongoClient

def map_to_list():
    try:
        with open('ListaChamada.csv', 'rb') as csvfile:
          names_reader = csv.reader(csvfile, delimiter=',')
          names = []

          for row in names_reader:
            names.append(row)

    except IOException:
        print('An error occurred.')

    else:
        print('file successfully readed')


def map_to_dictionary():
    try:
        with open('ListaChamada.csv', 'rb') as csvfile:
          names_reader = csv.DictReader(csvfile, delimiter=',')
          names = []
          for row in names_reader:
            #names.append(row['Nome2'])
            student_name = dict({'name': row['Nome2']})
            names.append(student_name)

    except IOException:
        print('An error occurred.')

    else:
        print('file successfully readed')

    return names


def insertDataOnMongo(db, studentDataList):
    try:
        students = db.students
    except:
        print('Error getting database.')
    else:
        print('Database successfully selected.')

    try:
        result = students.insert_many(studentDataList)
        print('Data inserted: {0}'.format(result.inserted_ids))
    except:
        print('Data insertion failed.')
    else:
        print('Data successfully inserted in database')


def connectToMongo():
    try:
        client = MongoClient()
        db = client.pymongo_test
    except:
        print('Connection to database failed.')
    else:
        print('successfully connected to database.')

    return db


if __name__ == '__main__':
    #connectToMongo()
    insertDataOnMongo(connectToMongo(), map_to_dictionary())
    # for i, name in enumerate(map_to_dictionary()):
    #     print(name)
