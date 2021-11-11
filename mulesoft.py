import sqlite3
link=sqlite3.connect('moviesdb.sqlite')
current=link.cursor()
current.executescript('''
DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    actor TEXT,
    actress TEXT,
    director TEXT,
    year_of_release INTEGER
);
''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Paramaathma', 'Puneeth Rajkumar', 'Deepa Sannidhi', 'Yograj Bhat', 2011)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Appu', 'Puneeth Rajkumar', 'Rakshitha', 'Puri Jaganath', 2002)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Tuck Jagadish', 'Nani', 'Ritu Varma', 'Shiva Nirvana', 2021)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Shershaah', 'Sidharth Malhotra', 'Kiara Advani', 'Vishnuvardhan', 2021)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Maharshi', 'Mahesh Babu', 'Pooja Hegde', 'Vamshi Paidipally', 2019)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('The Imitation Game', 'Benedict Cumberbatch', 'Keira Knightley', 'Morten Tyldum', 2018)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Uyare', 'Tovino Thomas', 'Parvathy Menon', 'Manu Ashokan', 2019)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Zindagi Na Milegi Dobara', 'Hrithik Roshan', 'Katrina Kaif', 'Zoya Akthar', 2011)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Airaa', 'Kalaiyarasan', 'Nayanthara', 'Sarjun', 2019)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('KGF', 'Yash', 'Srinidhi Shetty', 'Prashanth Neel', 2018)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Master', 'Vijay', 'Malavika Mohanan', 'Lokesh Kanagaraj', 2021)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Oh My Friend', 'Siddharth', 'Shruthi Hassan', 'Venu Sri Ram', 2011)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Yeh Jawaani Hai Deewani', 'Ranbir Kapoor', 'Deepika Padukone', 'Ayan Mukerji', 2013)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Ratashan', 'Vishnu Vishaal', 'Amala Paul', 'Ram Kumar', 2018)''')
current.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Aanandam', 'Arun Kurian', 'Siddhi Mahajankatti', 'Ganesh Raj', 2016)''')

sql_all = 'SELECT * FROM Movies'
print ("\n{:<5} {:<30} {:<25}{:<25} {:<25} {:<20}\n".format('Id','Title','Actor','Actress','Director','Year Of Release'))
for row in current.execute(sql_all):
    id,title,actor,actress,director,year_of_release=row
    print ("{:<5} {:<30} {:<25}{:<25} {:<25} {:<20}".format(id,title,actor,actress,director,year_of_release))

actor_search=input("\nEnter the actor name: ")
print('\nMovies starring '+actor_search+' are: \n' )
print("{:<30}{:<25}{:<25}{:<20}\n".format('Title','Actress','Director','Year of Release'))
for row in current.execute('SELECT title,actress,director,year_of_release FROM Movies WHERE actor= ?',(actor_search,)):
    title,actress,director,year_of_release=row
    print("{:<30}{:<25}{:<25}{:<20}".format(title,actress,director,year_of_release))
    link.commit()    
  
