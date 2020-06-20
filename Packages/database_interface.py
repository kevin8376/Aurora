import mysql.connector

key = input('Please Enter mysql root password : ')

try:
    db = mysql.connector.connect(host='localhost', user='root', passwd=key)
    del key
    if db.is_connected():
        print('Successfully connected')
    p = db.cursor(buffered=True)

    def execute_sql(query):
        """used to execute sql query and fetch the complete result set"""
        p.execute(query)
        if p.rowcount > 0:
            return p.fetchall()

    def execute_sql_from_file(path):
        """used to execute a sql file"""
        sql_file = open(path)
        sql_code = sql_file.read()
        sql_file.close()
        sql_commands = sql_code.split(';')
        for command in sql_commands:
            p.execute(command)

    def create_player_id(player_name):
        p.execute('USE AURORA')
        p.execute("SELECT * FROM game_stats;")
        return f'{player_name[0]}{player_name[-1]}{p.rowcount:08}'

    def get_player_id(player_name):
        p.execute('USE AURORA;')
        player_id = execute_sql(f'SELECT PLAYER_ID FROM game_stats WHERE PLAYER_NAME = "{player_name}"')[0][0]
        return player_id

    def is_unlocked(player_name, name, a_type):
        p.execute('USE AURORA;')
        if a_type == 'spell':
            a_type = 'player_spells'
        elif a_type == 'troop':
            a_type = 'player_troops'
        else:
            return
        data_set = execute_sql(f'SELECT {name} FROM {a_type} WHERE PLAYER_ID = "{get_player_id(player_name)}";')
        if data_set is not None and data_set[0][0] == 1:
            return True
        return False

    def create_player(player_name):
        """This function creates a player_profile"""

        # initializing database and checking that no player with same name exists
        # here name refers to players username
        p.execute('USE AURORA;')
        if (player_name,) in execute_sql('SELECT PLAYER_NAME FROM game_stats;'):
            raise Exception('duplicate_player_name')

        # child tables
        tables = ['player_troops', 'player_spells', 'spells',
                  'delta', 'tardis', 'benzamite', 'mandalore', 'nemesis', 'armada', 'elysium', 'demogorgon']

        # generating player_id using player_name
        player_id = create_player_id(player_name)

        # adding data into parent tables
        p.execute(f'INSERT INTO game_stats (PLAYER_ID, PLAYER_NAME) VALUES ("{player_id}", "{player_name}");')

        # adding data into child tables
        for table in tables:
            p.execute(f'INSERT INTO {table} (PLAYER_ID) VALUES ("{player_id}");')

        p.execute('COMMIT;')

    # running default sql file that contains the structure of games database
    execute_sql_from_file('../SQL/script001.sql')

    if __name__ == '__main__':
        p.close()
        db.close()


except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")
    exit()
