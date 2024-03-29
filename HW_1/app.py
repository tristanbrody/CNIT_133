from flask import Flask, request, jsonify, render_template
from flask_debugtoolbar import DebugToolbar
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("hw8.html")


@app.route("/gethint")
def get_hint():
    user_input = request.args.get("firstname", None)
    res = {"hint": [], "hint_available": False}
    if user_input is not None:
        res["hint"] = [name for name in NAMES if name.lower().startswith(user_input)]
    if len(res["hint"]) > 0:
        res["hint_available"] = True
    return jsonify(res)


NAMES = [
    "Jack",
    "Lewis",
    "James",
    "Logan",
    "Daniel",
    "Ryan",
    "Aaron",
    "Oliver",
    "Liam",
    "Jamie",
    "Ethan",
    "Alexander",
    "Cameron",
    "Finlay",
    "Kyle",
    "Adam",
    "Harry",
    "Matthew",
    "Callum",
    "Lucas",
    "Nathan",
    "Aiden",
    "Dylan",
    "Charlie",
    "Connor",
    "Thomas",
    "Alfie",
    "Joshua",
    "William",
    "Jayden",
    "Andrew",
    "Kai",
    "Max",
    "Ben",
    "Samuel",
    "Luke",
    "Tyler",
    "Rory",
    "David",
    "Michael",
    "Riley",
    "Noah",
    "Cole",
    "Joseph",
    "John",
    "Archie",
    "Jacob",
    "Fraser",
    "Rhys",
    "Ross",
    "Calum",
    "Jay",
    "Josh",
    "Euan",
    "Mason",
    "Owen",
    "Sam",
    "Leo",
    "Robert",
    "Scott",
    "Leon",
    "Robbie",
    "Benjamin",
    "Caleb",
    "Oscar",
    "Harris",
    "Murray",
    "Sean",
    "Christopher",
    "Kieran",
    "Aidan",
    "Jake",
    "Evan",
    "Kayden",
    "Arran",
    "Angus",
    "Brodie",
    "Ewan",
    "Muhammad",
    "Alex",
    "Declan",
    "Finn",
    "Blair",
    "Ollie",
    "Reece",
    "Corey",
    "Kian",
    "Harrison",
    "Taylor",
    "Kaiden",
    "Kenzie",
    "Cody",
    "Craig",
    "Mohammed",
    "Calvin",
    "Mark",
    "Jude",
    "Luca",
    "Ciaran",
    "George",
    "Zak",
    "Zac",
    "Charles",
    "Gregor",
    "Hamish",
    "Isaac",
    "Harvey",
    "Shay",
    "Struan",
    "Lee",
    "Steven",
    "Joe",
    "Lennon",
    "Patrick",
    "Jason",
    "Louis",
    "Olly",
    "Bailey",
    "Marcus",
    "Peter",
    "Sebastian",
    "Gabriel",
    "Jackson",
    "Zack",
    "Ashton",
    "Brandon",
    "Reuben",
    "Theo",
    "Paul",
    "Conor",
    "Hayden",
    "Lachlan",
    "Ruaridh",
    "Innes",
    "Stuart",
    "Jordan",
    "Sonny",
    "Alan",
    "Blake",
    "Zachary",
    "Cooper",
    "Ellis",
    "Caiden",
    "Fergus",
    "Jakub",
    "Zach",
    "Findlay",
    "Alistair",
    "Elliot",
    "Harley",
    "Anthony",
    "Callan",
    "Filip",
    "Louie",
    "Lyle",
    "Mohammad",
    "Brody",
    "Cayden",
    "Cian",
    "Marc",
    "Danny",
    "Shaun",
    "Austin",
    "Joel",
    "Nicholas",
    "Rio",
    "Rocco",
    "Dean",
    "Jonathan",
    "Carson",
    "Duncan",
    "Mitchell",
    "Ruairidh",
    "Stephen",
    "Dominic",
    "Kerr",
    "Edward",
    "Lloyd",
    "Mackenzie",
    "Martin",
    "Ali",
    "Henry",
    "Kevin",
    "Tom",
    "Alasdair",
    "Billy",
    "Freddie",
    "Keir",
    "Levi",
    "Junior",
    "Allan",
    "Campbell",
    "Darren",
    "Drew",
    "Oskar",
    "Arron",
    "Ayden",
    "Douglas",
    "Frederick",
    "Gary",
    "Seth",
    "Bruce",
    "Kaleb",
    "Maxwell",
    "Richard",
    "Rowan",
    "Toby",
    "Xander",
    "Alastair",
    "Colin",
    "Finley",
    "Jaxon",
    "Keiran",
    "Magnus",
    "Mateusz",
    "Mckenzie",
    "Nathaniel",
    "Felix",
    "Grant",
    "Zander",
    "Antoni",
    "Curtis",
    "Kacper",
    "Layton",
    "Niall",
    "Travis",
    "Tristan",
    "Adrian",
    "Flynn",
    "Hugh",
    "Ian",
    "Kaden",
    "Kieron",
    "Lochlan",
    "Morgan",
    "Nico",
    "Ronan",
    "Caelan",
    "Christian",
    "Jaden",
    "Justin",
    "Robin",
    "Eli",
    "Frankie",
    "Lauchlan",
    "Lennox",
    "Marco",
    "Mikey",
    "Vincent",
    "Arthur",
    "Aston",
    "Boyd",
    "Casey",
    "Dominik",
    "Iain",
    "Jaiden",
    "Jan",
    "Keegan",
    "Mac",
    "Marcel",
    "Ruari",
    "Rudy",
    "Abdul",
    "Bradley",
    "Cohen",
    "Damian",
    "Damien",
    "Dexter",
    "Dillon",
    "Elliott",
    "Hugo",
    "Leighton",
    "Marley",
    "Neil",
    "Ruben",
    "Szymon",
    "Zane",
    "Ahmed",
    "Ayaan",
    "Conner",
    "Hector",
    "Miller",
    "Milo",
    "Quinn",
    "Reilly",
    "Roman",
    "Shane",
    "Stewart",
    "Brogan",
    "Donald",
    "Elijah",
    "Hunter",
    "Ibrahim",
    "Jasper",
    "Kane",
    "Lukas",
    "Michal",
    "Nairn",
    "Ramsay",
    "Ruairi",
    "Rudi",
    "Simon",
    "Barry",
    "Bobby",
    "Brian",
    "Cruz",
    "Eoin",
    "Frazer",
    "Jai",
    "Jak",
    "Jenson",
    "Leyton",
    "Muhammed",
    "Nicolas",
    "Patryk",
    "Roan",
    "Saul",
    "Tommy",
    "Abdullah",
    "Aedan",
    "Alfred",
    "Arlo",
    "Bartosz",
    "Beau",
    "Cailean",
    "Clark",
    "Daniyal",
    "Eric",
    "Graeme",
    "Graham",
    "Greg",
    "Hamza",
    "Jaxson",
    "Johnny",
    "Jonah",
    "Marshall",
    "Micah",
    "Rayan",
    "Reiss",
    "Rohan",
    "Ryley",
    "Saif",
    "Victor",
    "Ajay",
    "Brendan",
    "Brooklyn",
    "Carter",
    "Coby",
    "Cory",
    "Dale",
    "Gavin",
    "Ivan",
    "Kelvin",
    "Kenneth",
    "Kody",
    "Mathew",
    "Mikolaj",
    "Miles",
    "Mohamed",
    "Myles",
    "Olivier",
    "Piotr",
    "Rayyan",
    "Shea",
    "Wiktor",
    "Brayden",
    "Caden",
    "Cain",
    "Conall",
    "Daryl",
    "Devon",
    "Emmanuel",
    "Fletcher",
    "Franciszek",
    "Garry",
    "Kalvin",
    "Oliwier",
    "Omar",
    "Regan",
    "Syed",
    "Warren",
    "Xavier",
    "Aleksander",
    "Asher",
    "Danyl",
    "Glen",
    "Kris",
    "Kyran",
    "Lawrie",
    "Lyall",
    "Maison",
    "Matteo",
    "Murdo",
    "Mylo",
    "Phoenix",
    "Stanley",
    "Will",
    "Zain",
    "Andy",
    "Anton",
    "Armaan",
    "Cairn",
    "Conrad",
    "Dawid",
    "Derren",
    "Francis",
    "Gareth",
    "Gordon",
    "Haris",
    "Jaydon",
    "Joey",
    "Leland",
    "Leonardo",
    "Maksymilian",
    "Malcolm",
    "Nikodem",
    "Philip",
    "Ruaraidh",
    "Russell",
    "Santiago",
    "Shae",
    "Shayne",
    "Torin",
    "Vinnie",
    "Wojciech",
    "Aarron",
    "Ahmad",
    "Aidyn",
    "Albert",
    "Alec",
    "Amir",
    "Antony",
    "Archibald",
    "Aydin",
    "Baillie",
    "Bryan",
    "Calan",
    "Cillian",
    "Clay",
    "Conlan",
    "Connell",
    "Cullen",
    "Dara",
    "Devin",
    "Devlin",
    "Donnie",
    "Dorian",
    "Dougal",
    "Elias",
    "Eoghan",
    "Fionn",
    "Fred",
    "Glenn",
    "Igor",
    "Innis",
    "Ismail",
    "Jensen",
    "Jimmy",
    "Kobi",
    "Korey",
    "Laurence",
    "Lucca",
    "Luis",
    "Musa",
    "Natan",
    "Olaf",
    "Oran",
    "Ray",
    "Raymond",
    "Reegan",
    "Remy",
    "Richie",
    "Ritchie",
    "Romeo",
    "Ronnie",
    "Rylan",
    "Rylie",
    "Troy",
    "Tymon",
    "Yousef",
    "Yusuf",
    "Aaran",
    "Aden",
    "Ally",
    "Antonio",
    "Bo",
    "Cade",
    "Callen",
    "Carlo",
    "Casper",
    "Cormac",
    "Damon",
    "Darragh",
    "Darryl",
    "Davis",
    "Derek",
    "Eddie",
    "Emil",
    "Emilio",
    "Enzo",
    "Ewen",
    "Frank",
    "Guy",
    "Hassan",
    "Isa",
    "Julian",
    "Kade",
    "Kaidyn",
    "Kamil",
    "Karol",
    "Kenzi",
    "Kole",
    "Kristopher",
    "Lincoln",
    "Lochlann",
    "Luka",
    "Maciej",
    "Malachy",
    "Markus",
    "Maximillian",
    "Muir",
    "Nikolas",
    "Oisin",
    "Otis",
    "Pawel",
    "Preston",
    "Ralph",
    "Rayhan",
    "Reagan",
    "Rehan",
    "Rhuari",
    "Rhyan",
    "Roddy",
    "Rylee",
    "Sami",
    "Sandy",
    "Scot",
    "Spencer",
    "Stanislaw",
    "Teejay",
    "Theodore",
    "Tomas",
    "Tomasz",
    "Tony",
    "Tymoteusz",
    "Wilson",
    "Zakariya",
    "Alessandro",
    "Alexandre",
    "Alisdair",
    "Aran",
    "Ari",
    "Artur",
    "Aryan",
    "Ashwin",
    "Aulay",
    "Axel",
    "Bernard",
    "Bilal",
    "Blaine",
    "Brandan",
    "Bryce",
    "Bryden",
    "Bryn",
    "Calder",
    "Cale",
    "Cieran",
    "Codey",
    "Coen",
    "Conal",
    "Crawford",
    "Daragh",
    "Darwin",
    "Dennis",
    "Dermot",
    "Eesa",
    "Emilis",
    "Eryk",
    "Etienne",
    "Faizan",
    "Freddy",
    "Fynn",
    "Greig",
    "Haroon",
    "Haydn",
    "Hubert",
    "Hudson",
    "Humza",
    "Ivor",
    "Jared",
    "Jaydan",
    "Jayson",
    "Kabir",
    "Kaidan",
    "Kal",
    "Kallan",
    "Kenley",
    "Khai",
    "Kier",
    "Kingsley",
    "Kiran",
    "Kodi",
    "Koen",
    "Konrad",
    "Kristian",
    "Kristofer",
    "Kye",
    "Kyron",
    "Lleyton",
    "Malachi",
    "Maximilian",
    "Maximus",
    "Milosz",
    "Montgomery",
    "Munro",
    "Nataniel",
    "Nicol",
    "Niko",
    "Olli",
    "Pierce",
    "Reese",
    "Reily",
    "Rhyley",
    "Rian",
    "Roderick",
    "Ronald",
    "Rossi",
    "Ruan",
    "Sameer",
    "Seumas",
    "Shaye",
    "Solomon",
    "Taha",
    "Timothy",
    "Tobias",
    "Ty",
    "Usman",
    "Abdirahman",
    "Abel",
    "Abraham",
    "Adan",
    "Adel",
    "Alexzander",
    "Alix",
    "Ameer",
    "Andrei",
    "Aodhan",
    "Arden",
    "Arin",
    "Arjun",
    "Aron",
    "Ayan",
    "Ayman",
    "Ayyan",
    "Azaan",
    "Azan",
    "Baxter",
    "Bentley",
    "Blane",
    "Bodhi",
    "Braiden",
    "Brandyn",
    "Brendon",
    "Bruno",
    "Byron",
    "Cadan",
    "Cai",
    "Chang",
    "Chase",
    "Chris",
    "Codi",
    "Codie",
    "Cody-James",
    "Colby",
    "Colton",
    "Conan",
    "Conlon",
    "Connal",
    "Corbin",
    "Corin",
    "Cosmo",
    "Daniels",
    "Deacon",
    "Declyn",
    "Denis",
    "Derry",
    "Devyn",
    "Dillan",
    "Eachann",
    "Eden",
    "Edgar",
    "Edmund",
    "Erik",
    "Fabian",
    "Faris",
    "Finnlay",
    "Fionnlagh",
    "Franco",
    "Frederic",
    "Gabrielius",
    "Gene",
    "Gerard",
    "Ghulam",
    "Gino",
    "Gio",
    "Haaris",
    "Hasan",
    "Hashim",
    "Huzaifa",
    "Ieuan",
    "Ilyas",
    "Imran",
    "Isaiah",
    "Ismaeel",
    "Jac",
    "Jace",
    "Jamieson",
    "Jayce",
    "Jaydn",
    "Jeremy",
    "Jia",
    "John-Paul",
    "Jonathon",
    "Jordon",
    "Kaan",
    "Kaelan",
    "Kain",
    "Kamran",
    "Kamron",
    "Kayleb",
    "Keane",
    "Keelan",
    "Kegan",
    "Kellen",
    "Kevins",
    "Kieren",
    "Kobe",
    "Koby",
    "Krystian",
    "Ksawery",
    "Kyan",
    "Laiton",
    "Lance",
    "Li",
    "Loghan",
    "Lomond",
    "Luc",
    "Macauley",
    "Mack",
    "Madden",
    "Mahdi",
    "Maksim",
    "Mikail",
    "Milan",
    "Moses",
    "Mustafa",
    "Nikita",
    "Noel",
    "Norman",
    "Phillip",
    "Quentin",
    "Raphael",
    "Rayaan",
    "Reigan",
    "Reo",
    "Ricky",
    "Rico",
    "Rogan",
    "Roy",
    "Salar",
    "Samir",
    "Samson",
    "Seamus",
    "Shahzaib",
    "Smith",
    "Sol",
    "Sonni",
    "Spike",
    "T",
    "Tai",
    "Terence",
    "Thom",
    "Thomas-James",
    "Thorfinn",
    "Tian",
    "Tyler-Jay",
    "Tyreece",
    "Tyrese",
    "Tyrone",
    "Wayne",
    "Wen",
    "Wilbur",
    "Woody",
    "Yazan",
    "Yi",
    "Yu",
    "Yuvraj",
    "Zakaria",
    "Zayn",
    "Aadam",
    "Aarav",
    "Aarran",
    "Abderrahmane",
    "Abdur-Rahman",
    "Abdurrahman",
    "Addison",
    "Adeolu",
    "Aditya",
    "Aeron",
    "Aethan",
    "Affan",
    "Ahsan",
    "Akim",
    "Alans",
    "Alejandro",
    "Aleksandrs",
    "Alessio",
    "Alexandru",
    "Alister",
    "Alvin",
    "Amaan",
    "Aman",
    "Amar",
    "Anas",
    "Anders",
    "Andrea",
    "Andrzej",
    "Anish",
    "Annan",
    "Anson",
    "Arda",
    "Argyll",
    "Arman",
    "Arnav",
    "Arnold",
    "Ash",
    "Ashraf",
    "Auley",
    "Austen",
    "Awais",
    "Aydan",
    "Aymen",
    "Aziz",
    "Bailie",
    "Barri",
    "Beinn",
    "Blue",
    "Borys",
    "Brad",
    "Bradan",
    "Brady",
    "Bradyn",
    "Braeden",
    "Bram",
    "Branden",
    "Braydon",
    "Brennan",
    "Brett",
    "Broden",
    "Brydon",
    "Caeleb",
    "Cailen",
    "Callin",
    "Carl",
    "Carrick",
    "Carrson",
    "Cathal",
    "Cezary",
    "Charley",
    "Chester",
    "Chukwubuikem",
    "Clayton",
    "Clyde",
    "Cobey",
    "Cobie",
    "Coden",
    "Cohan",
    "Coinneach",
    "Coll",
    "Connelly",
    "Conon",
    "Corbyn",
    "Corran",
    "Couper",
    "Cyrus",
    "Damion",
    "Dane",
    "Dante",
    "Darach",
    "Darron",
    "Davie",
    "Dax",
    "Dayne",
    "Deividas",
    "Denholm",
    "Deniz",
    "Denver",
    "Deon",
    "Derin",
    "Derrin",
    "Diarmuid",
    "Diego",
    "Diesel",
    "Dimitri",
    "Dino",
    "Dolan",
    "Donovan",
    "Dougie",
    "Eamonn",
    "Eben",
    "Edwin",
    "Ekam",
    "Eliott",
    "Elvis",
    "Emanuel",
    "Emerson",
    "Emile",
    "Erland",
    "Ernest",
    "Ernie",
    "Eshan",
    "Ethen",
    "Fahad",
    "Fahim",
    "Fareed",
    "Fredrik",
    "Fynlay",
    "Gerrard",
    "Gibson",
    "Gilbert",
    "Giovanni",
    "Gray",
    "Grayson",
    "Haiden",
    "Haider",
    "Hamid",
    "Hao",
    "Harlan",
    "Harlie",
    "Harlow",
    "Harold",
    "Hendrix",
    "Herbert",
    "Hong",
    "Hussain",
    "Idris",
    "Ihsan",
    "Irvine",
    "Issa",
    "Ivo",
    "Jacek",
    "Jackie",
    "Jadon",
    "Jaidan",
    "Jaime",
    "Jase",
    "Javier",
    "Jax",
    "Jayden-James",
    "Jayme",
    "Jaysen",
    "Jesse",
    "Johan",
    "Johannes",
    "John-Robert",
    "Johnnie",
    "Jon",
    "Jonasz",
    "Jonny",
    "Jorden",
    "Josef",
    "Joss",
    "Jozef",
    "Jun",
    "Kael",
    "Kallen",
    "Kalvyn",
    "Karam",
    "Kavin",
    "Kaydin",
    "Kaylan",
    "Keagan",
    "Keaghan",
    "Keanu",
    "Keaton",
    "Keenan",
    "Keigan",
    "Keiren",
    "Keiron",
    "Kelan",
    "Kell",
    "Kellan",
    "Kerem",
    "Keyaan",
    "Khalid",
    "Kiain",
    "Kiegan",
    "Killian",
    "Kirk",
    "Kit",
    "Klay",
    "Kohl",
    "Konnor",
    "Koray",
    "Kori",
    "Kornel",
    "Kory",
    "Krish",
    "Krzysztof",
    "Kuba",
    "Kurtis",
    "Kyeron",
    "Kyler",
    "Kyren",
    "Laith",
    "Laurie",
    "Lawson",
    "Leeroy",
    "Leith",
    "Lemuel",
    "Lenny",
    "Leonard",
    "Leonid",
    "Leslie",
    "Lionel",
    "Loic",
    "Lorcan",
    "Lucan",
    "Ludovic",
    "Lukasz",
    "Lynden",
    "Macaulay",
    "Mackie",
    "Mahmoud",
    "Maksym",
    "Mani",
    "Mario",
    "Marwan",
    "Massimo",
    "Matas",
    "Mate",
    "Mateo",
    "Mathias",
    "Matt",
    "Maxi",
    "Maxim",
    "Maxime",
    "Maxx",
    "Mckinley",
    "Mieszko",
    "Miguel",
    "Mikaeel",
    "Millar",
    "Mohanad",
    "Murdoch",
    "Murtaza",
    "Naif",
    "Nate",
    "Nelson",
    "Neo",
    "Odhran",
    "Odin",
    "Orhan",
    "Orran",
    "Orrin",
    "Ossian",
    "Paddy",
    "Padraig",
    "Paton",
    "Patrik",
    "Pearse",
    "Presley",
    "Raees",
    "Raegan",
    "Rafael",
    "Raiden",
    "Raja",
    "Rami",
    "Ramin",
    "Ramsey",
    "Ranald",
    "Rannoch",
    "Rex",
    "Rheagan",
    "Rhian",
    "Rhiley",
    "Rhuraidh",
    "Rhylen",
    "Riyad",
    "Rob",
    "Rocky",
    "Ronin",
    "Ruadhan",
    "Ruaidhri",
    "Rui",
    "Ryaan",
    "Ryden",
    "Rylen",
    "Sammy",
    "Sean-Paul",
    "Seonaidh",
    "Seoras",
    "Shawn",
    "Shayaan",
    "Shayan",
    "Sheldon",
    "Sinclair",
    "Sorley",
    "Stevie",
    "Sulaiman",
    "Sylvan",
    "T-Jay",
    "Taio",
    "Talha",
    "Tate",
    "Tay",
    "Ted",
    "Thiago",
    "Tomass",
    "Torren",
    "Torrin",
    "Travi",
    "Tylor",
    "Uilleam",
    "Umair",
    "Umar",
    "Umer",
    "Vakaris",
    "Vaughn",
    "Viggo",
    "Viraj",
    "Vojtech",
    "Wilfred",
    "Winston",
    "Wyatt",
    "Yahia",
    "Yahya",
    "Yan",
    "Yousif",
    "Yuan",
    "Yuri",
    "Zachariah",
    "Zackary",
    "Zakk",
    "Zayan",
    "Zenon",
    "Ziyad",
    "A-Jay",
    "Aaban",
    "Aaden",
    "Aadi",
    "Aadil",
    "Aadyn",
    "Aagat",
    "Aahil",
    "Aarnav",
    "Aaron-John",
    "Aaryn",
    "Aashdon",
    "Aaston",
    "Abbad",
    "Abbas",
    "Abdalhai",
    "Abdalkhalq",
    "Abdelrahman",
    "Abdelrauof",
    "Abdorahman",
    "Abdoul",
    "Abdualeem",
    "Abduallah",
    "Abdul-Hakim",
    "Abdul-Karim",
    "Abdul-Nafi",
    "Abdul-Rehman",
    "Abdul-Samad",
    "Abdula",
    "Abdulhaq",
    "Abdulkarim",
    "Abdull",
    "Abdulmohymen",
    "Abdulrahim",
    "Abdulrhman",
    "Abdur",
    "Abdur-Rahim",
    "Abdurrhman",
    "Abdusalam",
    "Abe",
    "Abedraouf",
    "Abhinav",
    "Abhiram",
    "Abiola",
    "Abobaker",
    "Abubakar",
    "Ace",
    "Adabpreet",
    "Adedimeji",
    "Adeeb",
    "Adejinmi",
    "Adem",
    "Adeswara",
    "Adetayo",
    "Adham",
    "Adhamh",
    "Adhvik",
    "Adil",
    "Adley",
    "Adnan",
    "Adrian-Lee",
    "Adryell",
    "Adyn",
    "Affonso",
    "Afton",
    "Aghilas",
    "Ahmet",
    "Ahmid",
    "Ahron",
    "Aidan-Scott",
    "Aidanlee",
    "Aide",
    "Aidi",
    "Aidian",
    "Aighan",
    "Ainoras",
    "Airen",
    "Airil",
    "Airyn",
    "Aithan",
    "Aj",
    "Ajaipal",
    "Ajmail",
    "Aki",
    "Akib",
    "Akshaj",
    "Akshar",
    "Al-Houssen",
    "Alan-John",
    "Aland",
    "Alasdhair",
    "Alban",
    "Aldrin",
    "Aleister",
    "Aleksandr",
    "Aleksejs",
    "Ales",
    "Alexander-James",
    "Alexandreau-Le-Prince",
    "Alexin",
    "Alfie-George",
    "Alfie-John",
    "Alick",
    "Alistar",
    "Alixander",
    "Aliyan",
    "Allen",
    "Allister",
    "Alphonsus",
    "Alwaleed",
    "Alwyn",
    "Alyx",
    "Alyxs",
    "Amaar",
    "Amad",
    "Amadou",
    "Amandeep",
    "Amanjeet",
    "Amanveer",
    "Amin",
    "Amine",
    "Amiogho",
    "Amirreza",
    "Amitoj",
    "Ammaar",
    "Ammar",
    "Amrit",
    "Anaan",
    "Anamol",
    "Anayat",
    "Anderson",
    "Andre",
    "Andreas",
    "Andres",
    "Andrius",
    "Anees",
    "Aneirin",
    "Aneurin",
    "Angelo",
    "Aniket",
    "Anir",
    "Anis",
    "Anizoba",
    "Anjan",
    "Anmol",
    "Ansh",
    "Antek",
    "Anthany",
    "Anthony-John",
    "Anthony-Junior",
    "Antoine",
    "Anup",
    "Aonghas",
    "Aous",
    "Aqeel",
    "Aqil",
    "Arainn",
    "Arbaaz",
    "Archie-Jay",
    "Ardil",
    "Areeb",
    "Areen",
    "Argyle",
    "Arhaan",
    "Arhab",
    "Arian",
    "Arien",
    "Arihaant",
    "Aristarkh",
    "Ariz",
    "Arjan",
    "Arkadiusz",
    "Arkle",
    "Armaghan",
    "Armando",
    "Arne",
    "Arnod",
    "Aronas",
    "Arris",
    "Arryn",
    "Arsal",
    "Arsalan",
    "Arshia",
    "Arshveer",
    "Arta",
    "Arthor",
    "Arturas",
    "Arturs",
    "Arun",
    "Arvin",
    "Aryaman",
    "Asad",
    "Ashley",
    "Asim",
    "Aslan",
    "Aswin",
    "Athanasios",
    "Atholl",
    "Atif",
    "Atila",
    "Attilio",
    "Auob",
    "Auryn",
    "Austyn",
    "Aveer",
    "Avery",
    "Aviral",
    "Avyukt",
    "Ayaz",
    "Ayden-James",
    "Ayham",
    "Ayibatonye",
    "Ayodeji",
    "Ayomiyato",
    "Ayoub",
    "Ayush",
    "Azaia",
    "Azhar",
    "Babatunde",
    "Baden",
    "Bailley",
    "Bajan",
    "Baldev",
    "Balfour",
    "Baljeet",
    "Bambeli",
    "Baran",
    "Barclay",
    "Bardia",
    "Barna",
    "Barnaby",
    "Barrie",
    "Bartek",
    "Bartlomiej",
    "Basim",
    "Bassiru",
    "Bay",
    "Bayley",
    "Bayly",
    "Bence",
    "Benedek",
    "Benedict",
    "Benicio",
    "Benny",
    "Berk",
    "Bertram",
    "Bion",
    "Bison",
    "Bixuan",
    "Biyron",
    "Blaike",
    "Blayne",
    "Blessings",
    "Bobby-Joe",
    "Boden",
    "Boette",
    "Boluwatife",
    "Bosco",
    "Boston",
    "Bourdieu",
    "Bowie",
    "Braden",
    "Bragi",
    "Braidy",
    "Braidyn-Drew",
    "Branach",
    "Brandin",
    "Brandon-Lee",
    "Brandonlee",
    "Brannon",
    "Braydin",
    "Brenden",
    "Brian-Thomas",
    "Broc",
    "Brodi",
    "Brodie-Alexander",
    "Brodyn",
    "Brogen",
    "Brogin",
    "Bruan",
    "Brydan",
    "Brydyn",
    "Buddy",
    "C-Jay",
    "Caddell",
    "Cadyn-Lee",
    "Caedan",
    "Caeden",
    "Cael",
    "Caelahn",
    "Caelin",
    "Caesar",
    "Cahir",
    "Caiden-John",
    "Caidyn-James",
    "Cailin",
    "Caillan",
    "Caillen",
    "Caillin",
    "Cailloch",
    "Cailob",
    "Caine",
    "Cainnech",
    "Cairo",
    "Cal",
    "Calam",
    "Calen",
    "Calib",
    "Callaghan",
    "Calogero",
    "Calvey",
    "Calvyn",
    "Caly",
    "Cambell",
    "Camilo",
    "Camryn",
    "Caolan",
    "Carey",
    "Carlos",
    "Carlyle",
    "Carson-Lewis",
    "Carwyn",
    "Casch",
    "Cash",
    "Cass",
    "Cassius",
    "Cavan",
    "Cayan",
    "Cayden-Lee",
    "Caydin",
    "Caydon",
    "Caylan",
    "Caylim",
    "Ceiran",
    "Celin",
    "Celyn",
    "Chace",
    "Chad",
    "Chael",
    "Chaitanya",
    "Chance",
    "Charis",
    "Charls",
    "Chazael",
    "Che",
    "Che-Jaedon",
    "Chetan",
    "Chetanveer",
    "Chia-Cheng",
    "Chidozie",
    "Chidubellum",
    "Chidumebi",
    "Chiemerie",
    "Chimaihe",
    "Chinedum",
    "Chinonso",
    "Chinwike",
    "Chiwetel",
    "Christiano",
    "Chukwudubem",
    "Chukwuebuka",
    "Cianan",
    "Cj",
    "Clae",
    "Clarke",
    "Claude",
    "Claudiu",
    "Clement",
    "Clint",
    "Clinton",
    "Clive",
    "Clivejakson",
    "Coben",
    "Cobi-Dean",
    "Cobin",
    "Cobyn",
    "Cochrane",
    "Codylee",
    "Codyn",
    "Coel",
    "Cohyn",
    "Coire",
    "Collin",
    "Comhan",
    "Comrie",
    "Connall",
    "Connan",
    "Connar",
    "Connon",
    "Coray",
    "Corben",
    "Corbie",
    "Corey-Jaidan",
    "Corey-Lee",
    "Corey-Ray",
    "Corie",
    "Cornelius",
    "Corrigan",
    "Corry",
    "Corwen",
    "Cox",
    "Cristian",
    "Cristofor",
    "Cruize",
    "Cruze",
    "Csongor",
    "Cuillin",
    "Cully",
    "Cupar",
    "Cyd",
    "Cye",
    "Cyril",
    "Darcy",
    "Daanish",
    "Daanyaal",
    "Daegan",
    "Dael",
    "Daimien",
    "Dainis",
    "Dainton",
    "Dairis",
    "Daivik",
    "Daiwik",
    "Dakarai",
    "Dakota",
    "Daley",
    "Dalin",
    "Dalton",
    "Daly",
    "Damir",
    "Dan",
    "Danaidh",
    "Daney",
    "Dani",
    "Danial",
    "Daniel-James",
    "Daniele",
    "Danielo",
    "Danila",
    "Danilo",
    "Dannie",
    "Danniel",
    "Dannon",
    "Danny-Junior",
    "Danny-Lee",
    "Danoush",
    "Danyaal",
    "Daoud",
    "Darcy",
    "Dario",
    "Dariusz",
    "Darko",
    "Darnell",
    "Darraich",
    "Darrell",
    "Darrin",
    "Darroch",
    "Daryn",
    "Dastins",
    "Datca",
    "David-Jordan",
    "Davide",
    "Davidlee",
    "Davy",
    "Davyn",
    "Dawood",
    "Dawoud",
    "Dawson",
    "Dayle",
    "Daylon",
    "Dayn",
    "Daynton",
    "Dayu",
    "De",
    "Deacan",
    "Deakan",
    "Decklyn",
    "Declan-Junior",
    "Deco",
    "Dee",
    "Deegan",
    "Deejay",
    "Deimantas",
    "Deklan",
    "Deklin",
    "Delano",
    "Demnan",
    "Dennon",
    "Denzel",
    "Deri",
    "Derrak",
    "Derrick",
    "Derryn",
    "Desmond",
    "Dev",
    "Devan",
    "Devron",
    "Dhilan",
    "Dhillon",
    "Dhruv",
    "Diarmid",
    "Diaz",
    "Digby",
    "Dilan",
    "Dilbagh",
    "Dilip",
    "Dilraj",
    "Dilveer",
    "Dio",
    "Dion",
    "Dirko",
    "Divy",
    "Django",
    "Dmitry",
    "Domhnall",
    "Dominiks",
    "Dominykas",
    "Don",
    "Donald-James",
    "Dougald",
    "Dougall",
    "Dovydas",
    "Dray",
    "Drever",
    "Dubhglas",
    "Dudek",
    "Duncan-James",
    "Duncan-Milan",
    "Dustin",
    "Dwayne",
    "Dylan-Mckenzie",
    "Dylan-Thomas",
    "Dylin",
    "Dyllen",
    "Eamon",
    "Earl",
    "Eason",
    "Eathan",
    "Ed",
    "Edan",
    "Eden-Lionell",
    "Edidiong",
    "Edmond",
    "Eduard",
    "Efetobore",
    "Efosa",
    "Ehan",
    "Ehsaan",
    "Ehsan",
    "Eimantas",
    "Einar",
    "Eion",
    "Eisa",
    "Ekenechukwu",
    "El-Shadai",
    "Elden",
    "Elgar",
    "Elias-Francis",
    "Elija",
    "Elio",
    "Eliot",
    "Elisha",
    "Elohim",
    "Eloi",
    "Elwood",
    "Emanuele",
    "Emanuiel",
    "Emiliano",
    "Emir",
    "Emirhan",
    "Emlyn",
    "Emre",
    "Enea",
    "Enes",
    "Ennis",
    "Enrikas",
    "Enrique",
    "Eparama",
    "Eray",
    "Eren",
    "Erick",
    "Erin",
    "Erion",
    "Erlend",
    "Erskine",
    "Ervin",
    "Erwin",
    "Esa",
    "Esli",
    "Essien",
    "Ethan-Ali",
    "Ethan-Paul",
    "Etinosa",
    "Evann",
    "Everett",
    "Evin",
    "Ezel",
    "Ezra",
    "Fabien",
    "Fabio",
    "Fahd",
    "Faheem",
    "Faithrich",
    "Faiz",
    "Faizaan-Ul-Hassan",
    "Fallon",
    "Fan",
    "Faraj",
    "Fardin",
    "Fareiz",
    "Fares",
    "Farrell",
    "Faryl",
    "Favoured",
    "Fawwaz",
    "Fayaaz",
    "Fazeel",
    "Fearghal",
    "Federico",
    "Feras",
    "Fergal",
    "Fergie",
    "Fiachra",
    "Filipe",
    "Finbar",
    "Findley",
    "Finlaggan",
    "Finnbarr",
    "Finnley",
    "Fintan",
    "Finton",
    "Fionan",
    "Fizaan",
    "Flinn",
    "Floyd",
    "Flyn",
    "Flynne",
    "Forbes",
    "Ford",
    "Forrest",
    "Francisco",
    "Franek",
    "Franki",
    "Frankie-Ray",
    "Franky",
    "Fraser-Lee",
    "Frasier",
    "Fredric",
    "Fyfe",
    "Fyvie",
    "Gab",
    "Gabe",
    "Gabor",
    "Gaetano",
    "Galip",
    "Gamaliel",
    "Garland",
    "Garvie",
    "Garvveer",
    "Gaspar",
    "Gaspard",
    "Gaura-Kisora",
    "Gedeon",
    "Geordie",
    "Georgie",
    "Gethin",
    "Ghillies",
    "Gian",
    "Gianluca",
    "Gideon",
    "Gilson",
    "Giulio",
    "Giuseppe",
    "Gizzy",
    "Gleb",
    "Glebs",
    "Godwin",
    "Goodluck",
    "Gracjan",
    "Grady",
    "Graison",
    "Grayden",
    "Gregg",
    "Gregoire",
    "Gregory",
    "Greyson",
    "Griffin",
    "Grzegorz",
    "Gurdit",
    "Gurditta",
    "Guriopal",
    "Gurrajvir",
    "Gurseace",
    "Gurseerit",
    "Gursewak",
    "Gursharan",
    "Gustavs",
    "Gvidas",
    "Haadhi",
    "Haadi",
    "Haaziq",
    "Hadee",
    "Hadley",
    "Hadyn",
    "Haidarali",
    "Haidn",
    "Haig",
    "Hakki",
    "Halcro",
    "Hamad",
    "Hammad",
    "Hamzah",
    "Hamzh",
    "Han",
    "Hani",
    "Hank",
    "Hanley",
    "Hanli",
    "Hanno",
    "Hanro",
    "Hans",
    "Hanzalah",
    "Haoqi",
    "Haozhe",
    "Hardy",
    "Harees",
    "Harigovind",
    "Harison",
    "Harjas",
    "Harlye",
    "Harown",
    "Harri",
    "Harrison-Blake",
    "Harry-James",
    "Harvie",
    "Hasen",
    "Hashir",
    "Hasnain",
    "Haydan",
    "Hayden-Mac",
    "Haydyn",
    "Haziim",
    "Hazim",
    "Heath",
    "Heaven",
    "Helgi",
    "Hendry",
    "Henendem-Obasi",
    "Henley",
    "Henrik",
    "Henrique",
    "Henryk",
    "Hezekiah",
    "Hiren",
    "Hisham",
    "Hitansh",
    "Holiness",
    "Howard",
    "Howie",
    "Hridhaan",
    "Huck",
    "Huey",
    "Humayun",
    "Humzah",
    "Huratio",
    "Husnain",
    "Husnayn",
    "Hussan",
    "Iacov",
    "Ibraheem",
    "Ibrahem",
    "Ideachi",
    "Idriss",
    "Ifeakanwanne",
    "Ifeanyichukwu",
    "Ignac",
    "Ignacy",
    "Igors",
    "Ikechukwu",
    "Ikenna",
    "Ilan",
    "Imaad",
    "Iman",
    "Immanuel",
    "Imo",
    "Indrid",
    "Inness",
    "Ioan",
    "Ires",
    "Iretemi",
    "Irfan",
    "Irtaza",
    "Irvin",
    "Is-Haaq",
    "Isaak",
    "Isaeah",
    "Isah",
    "Isaque",
    "Ishaq",
    "Isidoros",
    "Isio",
    "Israel",
    "Issac",
    "Issam",
    "Isxaq",
    "Iulian",
    "Ivie",
    "Izaan",
    "Izak",
    "Izakeel",
    "Izaki",
    "Izen",
    "Izuwa",
    "J",
    "Jacen",
    "Jacko-Square",
    "Jacky",
    "Jaco",
    "Jacob-John",
    "Jae",
    "Jaelyn",
    "Jaeyoun",
    "Jafar",
    "Jagjeevan",
    "Jago",
    "Jahan",
    "Jaicob-David",
    "Jaidon",
    "Jailyn",
    "Jaimie",
    "Jais",
    "Jaivon",
    "Jaiyen",
    "Jakob",
    "Jamall",
    "James-John",
    "James-Paul",
    "Jamey",
    "Jamie-Junior",
    "Jamie-Scott",
    "Jamiey",
    "Jamin",
    "Janek",
    "Janiece",
    "Jann",
    "Jannes",
    "Jarlath",
    "Jarron",
    "Jarvie",
    "Jarvis",
    "Jase-James",
    "Jashandeep",
    "Jaskeerat",
    "Jasper-John",
    "Javed",
    "Jawaad",
    "Jaxen",
    "Jaxxon",
    "Jay-Dominic",
    "Jay-J",
    "Jay-Jay",
    "Jay-Lee",
    "Jay-P",
    "Jay-Peter",
    "Jay-Scott",
    "Jayan",
    "Jayanthsayee",
    "Jayasekera",
    "Jayden-Mckenzie",
    "Jayden-Oliver",
    "Jayden-Paul",
    "Jayden-Sean",
    "Jayden-Thomas",
    "Jaydyn",
    "Jaye",
    "Jayk",
    "Jaymes",
    "Jaymie",
    "Jayvn",
    "Jayy",
    "Jean",
    "Jeb",
    "Jeck",
    "Jed",
    "Jeden",
    "Jedison",
    "Jedrzej",
    "Jeevun",
    "Jefferson",
    "Jeidan",
    "Jem",
    "Jeran",
    "Jeremiah",
    "Jeremiasz",
    "Jerry",
    "Jesujenyo",
    "Ji",
    "Jianle",
    "Jianxuan",
    "Jidechukwu",
    "Jie",
    "Jin",
    "Jiri",
    "Jiwan",
    "Jiya",
    "Jo",
    "Joachim",
    "Joahnny",
    "Joao",
    "Joash",
    "Joe-Alexander",
    "Joesph",
    "John-Jaydyn",
    "John-William",
    "Johnalexander",
    "Johnathan",
    "Johnathon",
    "Johnboy",
    "Johnie",
    "Johnjames",
    "Johnmason",
    "Johno",
    "Johnston",
    "Johnwilliam",
    "Jolyon",
    "Jon-Jo",
    "Jon-Paul",
    "Jonaide",
    "Jonas",
    "Jonathin",
    "Jonnie",
    "Jonnie-Scott",
    "Jonpaul",
    "Jonty",
    "Joosep",
    "Jordan-James",
    "Jordi",
    "Jordie",
    "Jordin",
    "Jordy",
    "Jose",
    "Josh-Jaden",
    "Josh-James",
    "Joshandeep",
    "Joshua-Jack",
    "Joshua-James",
    "Josie",
    "Jotham",
    "Jovan",
    "Jowaine",
    "Juan",
    "Judah",
    "Jules",
    "Junaid",
    "Junayd",
    "Junxi",
    "Justin-Lee",
    "Justis",
    "Kadan",
    "Kadian",
    "Kadin",
    "Kadir",
    "Kadyn-Rhys",
    "Kaelem",
    "Kaelen",
    "Kaelyn",
    "Kah",
    "Kahlin",
    "Kai-Morgan",
    "Kaian",
    "Kaide",
    "Kaiden-Scott",
    "Kaidon",
    "Kaii",
    "Kaileb",
    "Kailen",
    "Kailin",
    "Kaino",
    "Kaio",
    "Kairen",
    "Kairoh",
    "Kairon",
    "Kaison",
    "Kaivan",
    "Kaiwei",
    "Kaiyue",
    "Kaizer",
    "Kalan",
    "Kaleem",
    "Kalen",
    "Kaleyll",
    "Kalian",
    "Kalib",
    "Kalle",
    "Kallum",
    "Kam",
    "Kameran",
    "Kameron",
    "Kamili",
    "Kamrayn",
    "Kamsiyochukwu",
    "Kan",
    "Kang",
    "Kankanamge",
    "Kanyin",
    "Kar",
    "Karambir",
    "Karamo",
    "Karanjeet",
    "Karanjot",
    "Kareem",
    "Karim",
    "Karl",
    "Karolis",
    "Karoly",
    "Karsen",
    "Karson",
    "Karsson",
    "Karsyn",
    "Karter",
    "Karthik",
    "Kas",
    "Kash",
    "Kasim",
    "Kasper",
    "Kaya",
    "Kaydhen",
    "Kaydn",
    "Kaydon",
    "Kaylen",
    "Kayler",
    "Kaylib",
    "Kaylob",
    "Kayra",
    "Kaysan",
    "Kayson",
    "Keanan",
    "Keanen",
    "Keaten",
    "Keating",
    "Kebron",
    "Keelen",
    "Keelyn",
    "Keeran",
    "Kei",
    "Keighan",
    "Keio",
    "Keion",
    "Keiran-Neely",
    "Keith",
    "Kelden",
    "Kelly",
    "Kelton",
    "Kemal",
    "Kenan",
    "Kendo",
    "Kendrix",
    "Kennedy",
    "Kenny",
    "Kennzie",
    "Kensei",
    "Kenzie-Jay",
    "Kenzie-Jo",
    "Kenzie-William",
    "Keon",
    "Kereb",
    "Kerrin",
    "Kerwin",
    "Keryn",
    "Keshav",
    "Kester",
    "Kevir",
    "Keyan",
    "Khabat",
    "Khaiden",
    "Khaidyn",
    "Khairin",
    "Khalil",
    "Khayden",
    "Khaydian",
    "Khian",
    "Khodyn",
    "Khol",
    "Khris",
    "Khrithick",
    "Khurram",
    "Khye",
    "Khylan",
    "Kialan",
    "Kiayn",
    "Kiean",
    "Kiedis",
    "Kiefer",
    "Kien",
    "Kierin",
    "Kiern",
    "Kierrin",
    "Kilner",
    "Kim",
    "Kimathi",
    "Kin",
    "Kingston",
    "Kinnan",
    "Kinnon",
    "Kirac",
    "Kishan",
    "Klajus",
    "Knowledge",
    "Koban",
    "Kobie",
    "Kobus",
    "Koby-Joe",
    "Kobyn",
    "Kodey",
    "Kodie",
    "Kohdyn",
    "Kohen",
    "Kolvin",
    "Kona",
    "Konan",
    "Konlay",
    "Konnan",
    "Korben",
    "Korbin",
    "Korbyn",
    "Kordell",
    "Kory-Leigh",
    "Kosha",
    "Kosma",
    "Kristians",
    "Kristofer-James",
    "Kruz",
    "Kruze",
    "Kunal",
    "Kurt",
    "Kushal",
    "Kuzey",
    "Kyden",
    "Kylan",
    "Kymani",
    "Kyrin",
    "Kyro",
    "Kyron-Shogun",
    "Laeton",
    "Laggan",
    "Lailand",
    "Laird",
    "Lakshman",
    "Lally",
    "Landon",
    "Lannon",
]
