# Function to insert random data into the table
def instering_rand_data(connection, num_records=100):
    global cursor  # Add global declaration
    try:
        cursor = connection.cursor()
        fake = Faker('en_IN')

        for _ in range(num_records):
            name = fake.first_name() + " " + fake.last_name()
            age = fake.random_int(min=24, max=55)  # Adjusted maximum age
            address = f"{fake.building_number()} {fake.street_name()} {fake.city()}"
            # Generate mobile number ensuring the desired format
            mobile_number = "+91" + str(fake.random_element(elements=(6, 7, 8, 9))) + ''.join(
                [str(random.randint(0, 9)) for _ in range(9)])
            gender = fake.random_element(elements=("Male", "Female"))
            education_details = fake.random_element(elements=("B.tech", "Mtech", "MBA", "BBA", "BSC", "BCOM"))
            salary = fake.random_int(min=30000, max=150000)  # Adjusted salary range
            annual_salary = salary * 12
            doj = fake.date_between(start_date=datetime.date(2022, 1, 1), end_date=datetime.date(2022, 12, 31))
            department = fake.random_element(elements=("Engineering", "HR", "Sales", "Finance", "Marketing"))
            position = fake.random_element(elements=(
            "Manager", "Executive Manager", "Developer", "Data Analyst", "Data Scientist", "Cyber Security Engineer",
            "IT Systems Security Manager", "Applications Architect"))
            project_name = fake.random_element(elements=(
            "Project Alpha", "Project Beta", "Project Gamma", "Project Delta", "Project Epsilon",
            "Project Zeta", "Project Eta", "Project Theta", "Project Iota", "Project Kappa"))
            tech_stack = fake.random_element(elements=("Python", "SQL", "Flutter", "React", "Java"))
            # Randomly select manager name from the provided list
            manager = random.choice([
                "John Doe", "Jane Smith", "Michael Johnson", "Emily Brown", "William Davis", "Emma Wilson",
                "Daniel Martinez", "Olivia Anderson", "James Taylor", "Sophia Thomas", "David Garcia", "Isabella Lopez",
                "Joseph Martin", "Charlotte Perez", "Robert Hernandez", "Amelia Gonzalez", "John Miller", "Mia Lee",
                "Richard King", "Ella Lewis", "Charles Hall", "Ava Walker", "Matthew Young", "Harper Moore",
                "Anthony White", "Grace Hill", "Thomas Harris", "Scarlett Nelson", "Steven Clark", "Chloe Green",
                "Christopher Allen", "Zoe Carter", "Ryan Wright", "Nora Adams", "Mark Robinson", "Lily Baker",
                "Kevin Scott", "Avery Hall", "David Hill", "Luna Mitchell", "Brian Martinez", "Layla Perez",
                "Jason Baker", "Evelyn Turner", "Jeffrey Torres", "Hannah Ward", "Gary Foster", "Aria Rogers",
                "Larry Sanchez", "Madison Price", "Justin Reed", "Nova Phillips", "Brandon Cooper", "Ellie Ross",
                "Eric Flores", "Stella Wood", "Jacob Ross", "Samantha Stewart", "Scott Ramirez", "Violet Evans",
                "Ronald Butler", "Ruby Rivera", "Kenneth Wright", "Leah Foster", "Peter Long", "Clara Bell",
                "George Coleman", "Julia Murphy", "Donald Gray", "Penelope Reed", "Albert Kelly", "Eva Collins",
                "Philip Russell", "Anna Watson", "Billy Howard", "Hazel Peterson", "Gregory Cook", "Maria Coleman",
                "Frank Bell", "Naomi Brooks", "Terry Powell", "Alexa Washington", "Dennis Price", "Lillian Jenkins",
                "Walter Barnes", "Lucy Perry", "Roger Morris", "Jasmine Hayes", "Keith Howard", "Brooklyn Alexander",
                "Howard Ortiz", "Angelina Russell"
            ])

            # Insert data into the table
            cursor.execute("""
                INSERT INTO emss1 (Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, Annual_salary, DOJ, Department, Position, Project_Name, Tech_Stack, Manager)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, age, address, mobile_number, gender, education_details, salary, annual_salary, doj, department,
                  position, project_name, tech_stack, manager))

        connection.commit()
        print("Random data inserted successfully.")
    except Error as e:
        print(f"Error inserting random data: {e}")
    finally:
        if connection.is_connected():
            cursor.close()



            cursor.close()
