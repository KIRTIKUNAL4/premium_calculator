from starbase import Connection
print("Imported Package")
c = Connection("192.168.56.101","8000")
print("Connection Established")
ratings = c.table('ratings')
print("Created Table Ratings")
if (ratings.exists()):
    print("Dropping existing ratings table")
    ratings.drop()
print("Ready to create ratings")
ratings.create('rating')
print("Parsing the ml-100k ratings data...")
ratingFile=open(r"C:\Users\Anwesh Mohapatra\Downloads\Compressed\movielens-100k-dataset\ml-100k\u.data","r")
batch = ratings.batch()
for line in ratingFile:
    (userID,movieID,rating,timestamp)=line.split()
    batch.update(userID,{'rating':{movieID: rating}})
ratingFile.close()
print("Commiting ratings data to Hbase via REST service")
batch.commit(finalize=True)
print("Get back ratings for some users...")
print("Ratings for user ID 1:")
print(ratings.fetch('1')['rating']['1'])
print("Ratings for user ID 33:")
print(ratings.fetch('33'))
