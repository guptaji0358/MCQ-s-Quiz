import random 
import html

Questions = {
  "response_code": 0,
  "results": [
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Music",
      "question": "According to a song by Belinda Carlisle, Heaven is a place on what?",
      "correct_answer": "Earth",
      "incorrect_answers": [
        "Venus",
        "Mars",
        "Uranus"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "What is the name of Layer 7 of the OSI model?",
      "correct_answer": "Application",
      "incorrect_answers": [
        "Session",
        "Network",
        "Present"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Cartoon &amp; Animations",
      "question": "Who created the Cartoon Network series &quot;Regular Show&quot;?",
      "correct_answer": "J. G. Quintel",
      "incorrect_answers": [
        "Ben Bocquelet",
        "Pendleton Ward",
        "Rebecca Sugar"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Vehicles",
      "question": "Jaguar Cars was previously owned by which car manfacturer?",
      "correct_answer": "Ford",
      "incorrect_answers": [
        "Chrysler",
        "General Motors",
        "Fiat"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime &amp; Manga",
      "question": "Who is the colossal titan in &quot;Attack On Titan&quot;?",
      "correct_answer": "Bertolt Hoover",
      "incorrect_answers": [
        "Reiner",
        "Eren",
        "Sasha"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Music",
      "question": "&quot;Hallelujah&quot; is a song written by which Canadian recording artist?",
      "correct_answer": "Leonard Cohen",
      "incorrect_answers": [
        "Kory Lefkowits",
        "Ryan Letourneau ",
        "Justin Bieber "
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "What&#039;s the Team Fortress 2 Scout&#039;s city of origin?",
      "correct_answer": "Boston",
      "incorrect_answers": [
        "Sydney",
        "Detroit",
        "New York"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Celebrities",
      "question": "By which name is Ramon Estevez better known as?",
      "correct_answer": "Martin Sheen",
      "incorrect_answers": [
        "Charlie Sheen",
        "Ramon Sheen",
        "Emilio Estevez"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "History",
      "question": "In which country was the Statue of Liberty built and exported to the United States of America?",
      "correct_answer": "France",
      "incorrect_answers": [
        "Germany",
        "Spain",
        "England"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "Which of the following is NOT one of the main characters in Grand Theft Auto V&rsquo;s story mode?",
      "correct_answer": "Tommy Vercetti",
      "incorrect_answers": [
        "Michael de Santa",
        "Franklin Clinton",
        "Trevor Phillips"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Geography",
      "question": "Which of the following former Yugoslavian states is landlocked?",
      "correct_answer": "Serbia",
      "incorrect_answers": [
        "Bosnia and Herzegovina",
        "Montenegro",
        "Croatia"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Board Games",
      "question": "Carcassonne is based on which French town?",
      "correct_answer": "Carcassonne",
      "incorrect_answers": [
        "Paris",
        "Marseille",
        "Clermont-Ferrand"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Cartoon &amp; Animations",
      "question": "In the show &quot;Steven Universe&quot;, who are the main two employees of The Big Donut?",
      "correct_answer": "Sadie and Lars",
      "incorrect_answers": [
        "Steven and James",
        "Erik and Julie",
        "Bob and May"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "In Pokemon, the ability Wonder Guard is exclusive to which Pokemon? ",
      "correct_answer": "Shedinja ",
      "incorrect_answers": [
        "Sableye",
        "Spiritomb",
        "Silvally "
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Science &amp; Nature",
      "question": "What is the standard atomic weight of a Plutonium nucleus?",
      "correct_answer": "244",
      "incorrect_answers": [
        "94",
        "481",
        "128"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "Which of the following names is the &quot;Mega Man&quot; Franchise known as in Japan?",
      "correct_answer": "Rockman",
      "incorrect_answers": [
        "Paperman",
        "Scissorsman",
        "Mega Man"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "General Knowledge",
      "question": "Which of the following nations was NOT a belligerent in World War I?",
      "correct_answer": "Denmark",
      "incorrect_answers": [
        "Portugal",
        "Greece",
        "Romania"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "Who in Pulp Fiction says &quot;No, they got the metric system there, they wouldn&#039;t know what the f*** a Quarter Pounder is.&quot;",
      "correct_answer": "Vincent Vega",
      "incorrect_answers": [
        "Jules Winnfield",
        "Jimmie Dimmick",
        "Butch Coolidge"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "What is the maximum HP in Terraria?",
      "correct_answer": "500",
      "incorrect_answers": [
        "400",
        "1000",
        "100"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Music",
      "question": "Kanye West&#039;s &quot;Gold Digger&quot; featured which Oscar-winning actor?",
      "correct_answer": "Jamie Foxx",
      "incorrect_answers": [
        "Alec Baldwin",
        "Dwayne Johnson",
        " Bruce Willis"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime &amp; Manga",
      "question": "Which of the following originated as a manga?",
      "correct_answer": "Akira",
      "incorrect_answers": [
        "Cowboy Bebop",
        "High School DxD",
        "Gurren Lagann"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Science &amp; Nature",
      "question": "Which noble gas has the lowest atomic number?",
      "correct_answer": "Helium",
      "incorrect_answers": [
        "Neon",
        "Argon",
        "Krypton"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "General Knowledge",
      "question": "Which restaurant&#039;s mascot is a clown?",
      "correct_answer": "McDonald&#039;s",
      "incorrect_answers": [
        "Whataburger",
        "Burger King",
        "Sonic"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Science: Mathematics",
      "question": "The metric prefix &quot;atto-&quot; makes a measurement how much smaller than the base unit?",
      "correct_answer": "One Quintillionth",
      "incorrect_answers": [
        "One Billionth",
        "One Quadrillionth",
        "One Septillionth"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "&quot;The first rule is: you don&#039;t talk about it&quot; is a reference to which movie?",
      "correct_answer": "Fight Club",
      "incorrect_answers": [
        "The Island",
        "Unthinkable",
        "American Pie"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Cartoon &amp; Animations",
      "question": "What is the name of the creatures that the protagonists of the webshow RWBY fight against?",
      "correct_answer": "Grimm",
      "incorrect_answers": [
        "Reavers",
        "Heartless",
        "Dark Ones"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Board Games",
      "question": "In which year was the pen and paper RPG &quot;Deadlands&quot; released?",
      "correct_answer": "1996",
      "incorrect_answers": [
        "2003",
        "1999",
        "1993"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime &amp; Manga",
      "question": "In the 9th Pokemon movie, who is the Prince of the Sea?",
      "correct_answer": "Manaphy",
      "incorrect_answers": [
        "Ash",
        "May",
        "Phantom"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Music",
      "question": "What is the name of Finnish DJ Darude&#039;s hit single released in October 1999?",
      "correct_answer": "Sandstorm",
      "incorrect_answers": [
        "Dust Devil",
        "Sirocco",
        "Khamsin"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "Which of the following is a class in the game &quot;Hearthstone&quot;?",
      "correct_answer": "Priest",
      "incorrect_answers": [
        "Sage",
        "Cleric",
        "Monk"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Politics",
      "question": "Which of the following Pacific Islander countries is ruled by a constitutional monarchy?",
      "correct_answer": "Tonga",
      "incorrect_answers": [
        "Palau",
        "Fiji",
        "Kiribati"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Board Games",
      "question": "On a standard Monopoly board, which square is diagonally opposite &#039;Go&#039;? ",
      "correct_answer": "Free Parking",
      "incorrect_answers": [
        "Go to Jail",
        "Jail",
        "The Electric Company"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "General Knowledge",
      "question": "Which one of these is not a typical European sword design?",
      "correct_answer": "Scimitar",
      "incorrect_answers": [
        "Falchion",
        "Ulfberht",
        "Flamberge"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Science: Mathematics",
      "question": "What is the symbol for Displacement?",
      "correct_answer": "&Delta;r",
      "incorrect_answers": [
        "dr",
        "Dp",
        "r"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime &amp; Manga",
      "question": "In &quot;Inuyasha&quot;, what are the heros are looking to collect?",
      "correct_answer": "Jewel Shards",
      "incorrect_answers": [
        "Dragon Balls",
        "Rave Stones",
        "Sacred Stones"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "History",
      "question": "Who discovered Penicillin?",
      "correct_answer": "Alexander Flemming",
      "incorrect_answers": [
        "Marie Curie",
        "Alfred Nobel",
        "Louis Pasteur"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "General Knowledge",
      "question": "What is the Spanish word for &quot;donkey&quot;?",
      "correct_answer": "Burro",
      "incorrect_answers": [
        "Caballo",
        "Toro",
        "Perro"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "What is the name of the fictional retro-mod band starring Austin Powers as the lead vocalist?",
      "correct_answer": "Ming Tea",
      "incorrect_answers": [
        "Cough Fi",
        "Spear Mint",
        "Mister E"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "General Knowledge",
      "question": "Which of the following presidents is not on Mount Rushmore?",
      "correct_answer": "John F. Kennedy",
      "incorrect_answers": [
        "Theodore Roosevelt",
        "Abraham Lincoln",
        "Thomas Jefferson"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "M.U.G.E.N. is the name for what type of Game Engine?",
      "correct_answer": "Fighting Game",
      "incorrect_answers": [
        "Platforming Game",
        "Shooter Game",
        "Puzzle Game"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "What was the original name of Crash Bandicoot?",
      "correct_answer": "Willie Wombat",
      "incorrect_answers": [
        "Coco Bandicoot",
        "Marvelous Mole",
        "Wally Wombat"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime &amp; Manga",
      "question": "What is the last name of Edward and Alphonse in the Fullmetal Alchemist series.",
      "correct_answer": "Elric",
      "incorrect_answers": [
        "Ellis",
        "Eliek",
        "Elwood"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "General Knowledge",
      "question": "&quot;A3&quot;, &quot;B1&quot;, and &quot;Legal&quot; are typical names of sizes for what object?",
      "correct_answer": "Paper",
      "incorrect_answers": [
        "Airplanes",
        "Law books",
        "Phone screens"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "In &quot;Call Of Duty: Zombies&quot;, what is the name of the machine that upgrades weapons?",
      "correct_answer": "Pack-A-Punch",
      "incorrect_answers": [
        "Wunderfizz",
        "Gersch Device",
        "Mule Kick"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Sports",
      "question": "Which player holds the NHL record of 2,857 points?",
      "correct_answer": "Wayne Gretzky",
      "incorrect_answers": [
        "Mario Lemieux ",
        "Sidney Crosby",
        "Gordie Howe"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "Which of the following was a map that was in Team Fortress 2 at launch?",
      "correct_answer": "Gravel Pit",
      "incorrect_answers": [
        "Hoodoo",
        "Gold Rush",
        "Upward"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "General Knowledge",
      "question": "When was the website reddit founded ?",
      "correct_answer": "2005",
      "incorrect_answers": [
        "2008",
        "2004",
        "2006"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Celebrities",
      "question": "Gwyneth Paltrow has a daughter named...?",
      "correct_answer": "Apple",
      "incorrect_answers": [
        "Lily",
        "French",
        "Dakota"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "How many kilobytes in one gigabyte (in decimal)?",
      "correct_answer": "1000000",
      "incorrect_answers": [
        "1024",
        "1000",
        "1048576"
      ]
    },
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Video Games",
      "question": "Lanky, Funky, and Chunky are all characters featured in which series owned by Nintendo?",
      "correct_answer": "Donkey Kong",
      "incorrect_answers": [
        "Mario",
        "Kirby",
        "Zelda"
      ]
    }
  ]
}

quiz_data = []

for q in Questions["results"]:

    question = html.unescape(q["question"]).strip()
    correct = html.unescape(q["correct_answer"]).strip()
    wrong = [html.unescape(w).strip() for w in q["incorrect_answers"]]

    options = wrong + [correct]
    random.shuffle(options)

    quiz_data.append({
        "question": question,
        "options": options,
        "answer": correct
    })
