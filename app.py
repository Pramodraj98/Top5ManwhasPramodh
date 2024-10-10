from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

RDS_HOST = 'manhwa-db.clcgwyiis95h.ap-south-1.rds.amazonaws.com'
RDS_DB_NAME = 'manhwa-db'
RDS_USERNAME = 'admin'
RDS_PASSWORD = 'EusYMeaGobS0rteSbUD2'

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOST}:5432/{RDS_DB_NAME}"
db = SQLAlchemy(app)

class Manhwa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    writer = db.Column(db.String(50), nullable=False)
    art = db.Column(db.String(50), nullable=False)
    reads = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manhwa')
def get_manhwa():
    manhwa_data = [
        {
            "title": "1.  Solo Leveling",
            "genre": "Action, Fantasy",
            "Writer": "Chugong",
            "Art": "Redice Studio",
            "Reads": "2.5B",
            "description": "One of the best action fantasy manhwa and the most talked about adaptation in recent times is undoubtedly Solo Leveling. It is set in a world where humans have discovered supernatural skills, while our protagonist, Sung Jin-Woo, is a nobody with his E-Rank hunting skills. Things will take an interesting turn for him when he becomes the sole survivor of a dungeon raid. Awakened with strange new powers, Sung Jin-Woo will level up from being the weakest Hunter and eventually become the most powerful entity in the universe.",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/sololevelling.png"
        },
        {
            "title": "2.  Tower of God",
            "genre": "Adventure, Fantasy",
            "Writer":  "SIU (Lee Jong Hui)",
            "Art": "2010 – Present",
            "Reads": "1.2B",
            "description": "Even if you are not a manhwa fan, you must have heard of Tower of God. This action fantasy manhwa became especially popular after its anime adaptation. Tower of God focuses on Twenty-Fifth Bam, the young protagonist of the manhwa, who is determined to climb a mysterious Tower to find his friend Rachel. It is to be noted that the titular tower has different floors, and each floor has different obstacles. His quest is not going to be an easy one, and whether or not he will be able to meet his friend remains to be seen. Tower of God Season 2 has also been recently released..",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/Towergod.jpeg"
        },
        {
            "title": "3.  Hardcore Leveling Warrior",
            "genre": "Adventure, Action",
            "Writer":  "Sehoon Kim",
            "Art": "Completed",
            "Reads": "233.3M",
            "description": "Gong Won-Ho is the top player of Lucid Adventure because he uses his alias, Hardcore Leveling Warrior, to stay on top. However, one day, the unimaginable happens – he gets defeated, and now he has to get back on the top from the bottom. The most fascinating aspect of this action fantasy manhwa is how he climbed his way to the top in the first place.",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/Hardcore+Leveling+Warrior.jpeg"
        },
        {
            "title": "4.  Noblesse",
            "genre": "Fantasy",
            "Writer":  "Jeho Son",
            "Art": "Kwangsu Lee",
            "Reads": "439.7M",
            "description": "After being in a slumber for over 800 years, Cadis Etrama Di Raizel, aka Rai, wakes up in an unfamiliar modern world. Fortunately, he meets his loyal servant Frankenstein, who is now the owner of a high school. After attending the school, Rai tries to live an ordinary life, concealing his true identity; however, that won’t happen for long. This supernatural action fantasy manhwa will keep you engaged with its beautiful illustration and unique narrative till the end.",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/Noblesse.jpeg"
        },
        {
            "title": "5.  Lore Olympus",
            "genre": "Romance",
            "Writer":  "Rachel Smythe",
            "Art": "Every Sunday",
            "Reads": "1.4B",
            "description": "We can’t talk about the best fantasy manhwa and not mention Lore Olympus. Have you ever read Greek Mythology? Do you find it interesting? Well, a lot of people certainly do. However, the storyline and the order of events can be a little too difficult for most people to remember or even understand. ‘Lore Olympus’ is such a webtoon based on Greek mythology, with an easy-to-understand plot that uses modern-day events and lifestyle. The plot is primarily based on Hades and Persephone’s love story. Moreover, it also covers the lifestyle of all the gods surrounding them and the events of great importance.",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/Lore+Olympus.jpeg"
        },
        {
            "title": "6.  The Remarried Empress",
            "genre": "Romance",
            "Writer":  "Alphatart",
            "Art": "Sumpul",
            "Reads": "436M",
            "description": "Navier, the empress of the Eastern Empire, was shattered in front of her when her husband Sovieshu, Emperor of the Eastern Empire, wanted to divorce her because she couldn’t give him an heir. He cast her aside when she couldn’t bear him a child, even though they groomed her to become the perfect empress ever since her childhood. Read The Remarried Empress to find out more about her struggles and dilemmas when an unexpected variable appeared in her life.",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/The+Remarried+Empress.jpeg"
        },
        {
            "title": "7.  Leveling Up My Husband to the Max",
            "genre": "Romance",
            "Writer":  "Uginon, Nuova, Curlin",
            "Art": "Completed",
            "Reads": "83.1M",
            "description": "The central character of Leveling Up My Husband to the Max, Amber, is in turmoil with her controlling mother-in-law and cruel husband. Following the time-travel theme, Amber is sent back 10 years into the past, and she confronts her husband, who now adores her. With her knowledge of the potential future, she tries to change her husband, navigate the complexities of the past, and create a new narrative for herself.",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/Leveling+Up+My+Husband+to+the+Max.jpg"
        },
        {
            "title": "8.  From A Knight to A Lady",
            "genre": "Romance",
            "Writer":  "Ink, Hyerim Sung",
            "Art": "Every Sunday",
            "Reads": "70.4M",
            "description": "Estelle is a young knight in the Kingdom of Ersha who fought with immense strength until her last breath for her country. Sadly, her most trusted comrade kills her. Miraculously, 3 years later, she finds herself reincarnated as Lucifella, the rumored partner of the crown prince of Jansgar, the enemy kingdom. What’s more? She is now the betrothed of Duke Heint, her mortal enemy from her last life.",
            "image_url": "https://myanimeimages.s3.ap-south-1.amazonaws.com/From+A+Knight+to+A+Lady.jpeg"
        }
    ]
    return jsonify(manhwa_data)

if __name__ == '__main__':
    app.run(debug=True)
