import sqlite3

# start

DB_NAME = "college_data.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create colleges table with 'info' column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS colleges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            website TEXT NOT NULL,
            annual_fees INTEGER NOT NULL,
            info TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS branches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            college_id INTEGER,
            branch TEXT NOT NULL,
            cet_cutoff INTEGER NOT NULL,
            jee_cutoff INTEGER NOT NULL,
            FOREIGN KEY (college_id) REFERENCES colleges(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and tables updated successfully!")

def insert_sample_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Check if colleges already exist
    cursor.execute("SELECT COUNT(*) FROM colleges")
    count = cursor.fetchone()[0]

    if count == 0:
        colleges = [
    ("Shri Ramdeobaba College of Engineering and Management (RCOEM)", "https://www.rknec.edu/", 270000, "A leading engineering and management institute known for its academic excellence and industry partnerships."),
    ("G. H. Raisoni College of Engineering", "https://ghrce.raisoni.net/", 170000, "A reputed institute fostering innovation, research, and technical expertise."),
    ("Yeshwantrao Chavan College of Engineering", "https://ycce.edu/", 120000, "An esteemed engineering college recognized for its strong academic curriculum and placement opportunities."),
    ("KDK College of Engineering", "https://kdkce.edu.in/", 123000, "A well-known institute dedicated to quality education and technical skill development."),
    ("Jhulelal Institute of Technology", "https://www.jitnagpur.edu.in/", 112000, "An emerging institute offering modern infrastructure and industry-oriented programs."),
    ("Priyadarshini J. L. College of Engineering", "http://pjlce.edu.in/", 94000, "A progressive engineering college committed to academic and research excellence."),
    ("Priyadarshini Bhagwati College of Engineering", "https://pbcoe.edu.in/", 91800, "A reputed institution providing quality technical education and hands-on learning."),
    ("Symbiosis Institute of Technology", "https://sitnagpur.edu.in/", 91800, "A premier institute offering world-class engineering education with a focus on innovation."),
    ("Priyadarshini College of Engineering", "http://pcenagpur.edu.in/", 180000, "A well-established engineering institute known for academic excellence and student success."),
    ("Smt. Radhikatai Pandav College of Engineering", "https://srpce.ac.in/", 90000, "An engineering college dedicated to providing quality education with practical exposure."),
    ("Anjuman College of Engineering & Technology", "https://www.anjumanengg.edu.in/", 75000, "A renowned institute promoting technical education with a strong industry focus."),
    ("Cummins College of Engineering for Women, Nagpur", "https://www.cumminscollege.edu.in/", 100000, "A premier women's engineering college emphasizing innovation and empowerment."),
    ("G. H. Raisoni Academy of Engineering and Technology", "https://ghrcemn.raisoni.net/", 180000, "A distinguished institution offering cutting-edge engineering programs."),
    ("Government College of Engineering, Nagpur", "https://gcoen.ac.in/", 116000, "A government-run engineering college known for excellence in academics and research."),
    ("Guru Nanak Institute of Engineering & Management", "https://gniem.ac.in/", 62000, "A reputed institute imparting technical education with a strong emphasis on skill development."),
    ("JD College of Engineering and Management", "https://jdcoem.ac.in/", 79500, "An innovative engineering college with modern facilities and a research-driven approach."),
    ("Kavikulguru Institute of Technology and Science", "https://www.kits.edu/", 88750, "A prominent institute focusing on academic rigor and practical learning."),
    ("Laxminarayan Innovation Technological University", "https://litu.edu.in/", 110000, "A dynamic university fostering innovation and technical excellence."),
    ("National Fire Service College", "https://nfscnagpur.nic.in/", 96000, "A specialized institute known for training professionals in fire safety and engineering."),
    ("Nuva College of Engineering & Technology", "http://www.nuvaedu.com/", 53000, "An emerging engineering institute offering skill-based education and training."),
    ("Rajiv Gandhi College of Engineering & Research", "https://www.rcert.ac.in/", 108000, "A growing engineering college known for quality education and research opportunities."),
    ("S. B. Jain Institute of Technology, Management and Research", "https://www.sbjit.edu.in/", 100000, "An institute dedicated to technical and managerial education with a modern approach."),
    ("Shri Govindrao Wanjari College of Engineering and Technology", "https://www.gwcet.ac.in/", 180000, "A reputed institute offering specialized engineering programs with industry connections."),
    ("St. Vincent Pallotti College of Engineering and Technology", "https://www.stvincentngp.edu.in/", 110000, "An esteemed engineering college known for its rigorous academics and placements."),
    ("Suryodaya College of Engineering & Technology", "https://scetngp.com/", 78250, "A forward-thinking institute focused on technical education and professional growth."),
    ("Wainganga College of Engineering and Management", "https://www.wcem.in/", 79500, "An emerging college providing industry-oriented technical education."),
    ("Tulsiramji Gaikwad-Patil College of Engineering", "https://www.tgpcet.com/", 89500, "An engineering institute known for quality education and career-focused training."),
]


        cursor.executemany('''
            INSERT INTO colleges (name, website, annual_fees, info) VALUES ( ?, ?, ?, ?)
        ''', colleges)

        conn.commit()
        print("Sample data inserted successfully!")

    # Insert branches
    cursor.execute("SELECT COUNT(*) FROM branches")
    branch_count = cursor.fetchone()[0]

    if branch_count == 0:
        branches = [
            (1, "Electrical Engineering", 91.9, 95),
            (1, "Civil and Environmental Engineering", 83.24, 95),
            (1, "Electronics and Communication Engineering", 93.69, 95),
            (1, "Information Technology", 97.67, 95),
            (1, "Computer Science and Engineering", 98.08, 93),
            (1, "Mechanical and Smart Manufacturing", 90.69, 95),
            (1, "Biomedical Electronics Engineering", 83.88, 95),
            (1, "Computer Science and Engineering (Artificial Intelligence and Machine Learning)", 97.76, 95),
            (1, "Computer Science and Engineering (Cyber Secuirity)", 95.95, 95),
            (1, "Computer Science and Engineering (Data Science and Analytics)", 96.44, 95),
            (1, "Electronics and Computer Science", 94.04, 95),

            (2, "Computer Science and Engineering", 93.01, 94),
            (2, "Electronics and Telecommunication Engineering", 86.91, 91),
            (2, "Mechanical Engineering", 63.7, 94),
            (2, "civil Engineering", 68.94, 94),
            (2, "Electronics Engineering", 80.05, 94),
            (2, "Information Technology", 91.89, 94),
            (2, "Electrical Engineering", 73.28, 94),
            (2, "Computer Science and Engineering (Artificial Intelligence)", 92.68, 94),
            (2, "Artificial Intelligence",87.78, 94),
            (2, "Data Science", 88.52, 94),
            (2, "Computer Science and Engineering (Artificial Intelligence and Machine Learning)", 91.46, 94),
            (2, "Computer Science and Engineering (Cyber Secuirity)", 89, 94),
            (2, "Computer Science and Engineering (IoT)", 89.18, 94),
            
            (3, "Computer Science and Engineering", 94.65, 90),
            (3, "Electronics and Telecommunication Engineering", 89.7, 88),
            (3, "Mechanical Engineering", 78.42, 88),
            (3, "Electronics Engineering", 88.15, 88),
            (3, "Information Technology", 93.53, 88),
            (3, "Electrical Engineering", 78.34, 88),
            (3, "Artificial Intelligence and Data Science", 92.35, 88),
            (3, "Computer Science and Engineering (Artificial Intelligence and Machine Learning)", 92.84, 88),
            (3, "Computer Science and Engineering (IoT and cyber secuirity)", 93.97, 88),
            (3, "Computer Science and Design", 90.87, 88), 
            (3, "Computer Technology", 93.25, 88),
            (3, "Civil Engineering", 71.41, 88),
            
            (4, "Computer Science and Engineering", 78.44, 80),
            (4, "Electronics and Teleommunication Engineering", 69.63, 78),
            (4, "Mechanical Engineering", 50.93, 78),
            (4, "Civil Engineering", 45.34, 78),
            (4, "Electrical Engineering", 65.36, 78),
            (4, "Information Technology", 76.13, 78),
            (4, "Artificial Intelligence and Data Science", 74.28, 78),
            
            (5, "Computer Science and Engineering", 71.27, 82),
            (5, "Electronics and Communication Engineering", 65.43, 80),
            (5, "Mechanical Engineering", 32.47, 82),
            (5, "Electrical Engineering", 52.25, 82),
            (5, "Electronics and Communication (Advanced Communicatio Technology)", 67.16, 82),
            (5, "Computer Science and Engineering (Artificial Intelligence and Machine Learning)", 32.47, 82),
            
            (6, "Computer Science and Engineering", 83.38, 82),
            (6, "Electronics and Telecommunication Engineering", 74.87, 82),
            (6, "civil Engineering", 68.94, 82),
            (6, "Electrical Engineering", 66.96, 82),
            (6, "Artificial Intelligence Engineering", 79.47, 82),

            (7, "Computer Science and Engineering", 76.14, 82),
            (7, "Electronics and Communication Engineering", 67.84, 82),
            (7, "Mechanical Engineering", 51.22, 82),
            (7, "civil Engineering", 41.84, 82),
            (7, "Information Technology", 73.58, 82),

            (9, "Electrical Engineering (Electronics and Power)", 67.96, 82),
            (9, "Aeronautical Engineering", 67.4, 67.4),
            (9, "Computer Technology", 85.93, 82),
            (9, "in Civil Engineering", 49.56, 82),
            (9, "Information Technology", 86.35, 82),
            (9, "Mechanical Engineering", 53.17, 82),
            (9, "Electronics and Telecommunication Engineering", 79.79, 82),
            (9, " Electrical Engineering", 62.74, 82),
            (9, "Biotechnology", 66.68, 82),
            (9, "Industrial IoT", 78.41, 78.41),
            (9, " Robotics and Artificial Intelligence", 82.32, 82.32),
            (9, "Chemical Engineering", 63.98, 63.98),
            (9, "Artificial Intelligence and Data Science", 85.18, 85.18),
            (9, "Electronics and Communication Engineering", 75.35, 75.35),
            (9, "Computer Science and Engineering", 88.27, 88.27),
            
            (10, "Electronics and Telecommunication Engineering", 51.79, 51.79),
            (10, "Computer Engineering", 49.51,49.51),
            (10, "Mechanical Engineering", 28.87, 28.87),
            (10, "Civil Engineering", 27.15, 27.15),
            (10, "Electrical Engineering", 23.99,23.99),
            (10, "Computer Science and Engineering",59.34, 59.34),
            
            (11, "Mechanical Engineering", 41.84,41.84),
            (11, "Electronics and Telecommunication Engineering", 50.93,50.93),
            (11, "Electrical Engineering", 46.51,46.51),
            (11, "Computer Science and Engineering", 69.76, 69.76),
            (11, "Civil Engineering", 34.8,34.8),
            (11, "Artificial Intelligence and Data Science", 62.87,62.87),
            
            (12, "Mechanical Engineering", 12.8,34.8),

            (13, "Electrical Engineering", 66.08, 66.08),
            
            (14, "Electrical Engineering", 78.06, 78.06),
            (14, "Civil Engineering", 78.52, 78.52),
            (14, "Computer Science and Engineering", 96.34, 96.34),
            (14, "Electronics and Telecommunication Engineering", 94.14, 94.14),
            (14, "Mechanical Engineering", 73.96, 73.96),
            
            (15, "Electrical Engineering", 35.67, 35.67),
            (15, "Civil Engineering", 43.12, 43.12),
            (15, "Mechanical Engineering", 15.6, 15.6),
            (15, "Computer Science and Engineering", 83.54, 83.54),
            
            (16, "Electronics and Telecommunication Engineering", 60.98, 60.98),
            (16, "Mechanical Engineering",49.48, 49.48),
            (16, "Computer Science and Engineering", 	79.8,	79.8),
            (16, "Civil Engineering", 43.12, 43.12),
            (16, "Information Technology", 71.64, 71.64),
            (16, "CElectrical Engineering", 	49.62, 	49.62),
            (16, "Artificial Intelligence (AI)", 69.22, 69.22),
            (16, "Computer Science and Engineering (Data Science)",	69.78,	69.78),
            
            (17, "Civil Engineering", 	43.85,	43.85),
            (17, "Electronics and Communication Engineering", 57.41, 57.41),
            (17, "Electrical Engineering", 47.46, 47.46),
            (17, "Mechanical Engineering", 37.6, 37.6),
            (17, "Computer Technology", 80.74, 80.74),
            (17, "Information Technology", 72.5, 72.5),

            (18, "Chemical Engineering", 93.62, 93.62),
            (18, "Oil Technology", 73.42, 73.42),
            (18, "Food Technology", 93.78, 93.78),
            (18, "Paper and Pulp Technology", 71.06, 71.06),
            (18, "Plastic and Polymer Technology", 79.08, 79.08),
            (18, "Petrochemical Technology", 83.07, 83.07),
            (18, "Surface Coating Technology", 86.22, 86.22),
            
            (19, "Fire Engineering", 84, 84),
            
            (21, " Mechanical Engineering", 54.18, 54.18),
            (21, "Civil Engineering", 17.75,17.75),
            (21, "Electronics and Communication Engineering", 55.12, 55.12),
            (21, "Electrical Engineering", 35.67, 35.67),
            (21, "Mining Engineering", 38.54,38.54),
            (21, "Computer Science and Engineering(Data Science)", 53.74, 53.74),
            (21, "Computer Science and Engineering", 76.13, 76.13),
            
            (22, "Mechanical Engineering", 50.62, 50.62),
            (22, "Electrical Engineering", 71.36, 71.36),
            (22, "Electronics and Telecommuniation Engineering", 78.41, 78.41),
            (22, "Computer Science and Engineering", 83.39, 83.39),
            (22, "Computer Science Engineering (Data Science)", 81.24, 81.24),
            (22, "Computer Science and Engineering (Artificial Intelligence and Machine Learning)", 82.21, 82.21),
            
            (23, "Computer Science and Engineering", 45, 45),
            (23, "Electronics and Telecommunication", 40, 40),
            (23, "Electrical Engineering", 35, 35),
            (23, "Mechanical Engineering", 30, 30),
            (23, "Civil Engineering", 25, 25),
            
            (24, " Mechanical Engineering", 56.99, 56.99),
            (24, "Computer Engineering", 91.75, 91.75),
            (24, "Electronics and Telecommunication Engineering", 81.52, 81.52),
            (24, " Information Technology", 92.32, 92.32),
            (24, "Electrical Engineering", 75.87, 75.87),
            (24, "Computer Science and Engineering (Data Science)", 86.17, 86.17),
            (24, "Artificial Intelligence", 86.17, 86.17),
            (24, "Computer Science and Business Systems", 85.16, 85.16),
            (24, "Computer Science and Engineering (Cyber Security)", 84.52, 84.52),
            (24, " Industrial IoT",84.52, 84.52),
            (24, "Civil Engineering", 73.26, 73.26),
            
            (25, "Computer Engineering", 69.31, 69.31),
            (25, "Civil Engineering", 25.55, 25.55),
            (25, "Electrical Engineering", 42.56, 42.56),
            (25, "Mechanical Engineering", 28.38, 28.38),
            (25, "Electronics and Telecommunication Engineering", 56.75, 56.75),
            (25, "Computer Science and Engineering(Data Science)", 61.44, 61.44),
            
            (26, " Computer Science and Engineering", 	59.87, 	59.87),
            (26, "Electronics and Telecommunication Engineering", 44.06, 44.06),
            (26, "Mechanical Engineering", 16.24, 16.24),
            (26, "Civil Engineering", 6.57, 6.57),
            (26, "Electrical Engineering", 45.65, 45.65),
            (26, "Artificial Intelligence and Data Science", 53.82, 53.82),
             
            (27, "Mechanical Engineering", 42.56, 42.56),
            (27, "Computer Science and Engineering", 71.17, 71.17),
            (27, "Civil Engineering", 59.93, 59.93),
            (27, " Information Technology", 68.82, 68.82),
            (27, "Electronics and Communication Engineering", 58.88, 58.88),
            (27, "Electrical Engineering", 54.01, 54.01),
            (27, "Aeronautical Engineering", 52.25, 52.25),
            (27, "Biotechnology", 30.96, 30.96),
            (27, "Computer Science and Engineering (Data Science)", 68.82, 68.82)
            
        ]

        cursor.executemany('''
            INSERT INTO branches (college_id, branch, cet_cutoff, jee_cutoff) 
            VALUES (?, ?, ?, ?)
        ''', branches)

        conn.commit()
        print("Branch data inserted successfully!")

    conn.close()

def fetch_colleges():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, website, annual_fees, info FROM colleges")
    colleges = cursor.fetchall()

    for college in colleges:
        college_name = college[0]
        college_website = college[1]
        annual_fees = college[2]
        college_info = college[3]

        print(f"College: {college_name}\nFees: ₹{annual_fees}\nWebsite: {college_website}\nInfo: {college_info}\n")

    conn.close()

if __name__ == "__main__":
    create_database()  # Ensure the database schema is correct
    insert_sample_data()  # Insert sample data if not present
    fetch_colleges()  # Display stored data
