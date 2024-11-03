from DataBaseSync import DataBaseSync


def main():
    db = DataBaseSync({'vc': 'bf'}, 'Threading')
    db.set_value('a', 'b')
    db.set_value('c', 'd')
    print(db.get_value('a'))
    d = db.delete_value('c')
    print(db)


if __name__ == '__main__':
    main()
