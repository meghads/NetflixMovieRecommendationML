# Netflix Movie Recommendation System

This project implements a **Netflix Movie Recommendation System** using the **Eclat Algorithm**, a frequent pattern mining approach. The system identifies pairs of movies often watched together by analyzing a dataset of user transactions.

---

## Features

- **Eclat Algorithm**: Utilized for discovering frequently occurring itemsets (movie pairs) in user transactions.
- **Dataset Analysis**: Processes a dataset of Netflix movie transactions to identify associations.
- **Customizable Parameters**: Adjust parameters like support, confidence, and lift for tailored results.
- **Visualization**: Outputs results in a clear, tabular format showcasing the top associated movie pairs.

---

## How It Works

1. **Data Collection**:
   - The dataset (`NetfilxMovies.xlsx`) contains transactional data, where each row represents a user's movie-watching activity.

2. **Data Preprocessing**:
   - Transactions are extracted by iterating over the dataset rows and columns.
   - Each transaction is stored as a list of movies watched by a user.

3. **Model Training**:
   - The **Eclat Algorithm** is applied to the transactions with the following parameters:
     - `min_support`: Minimum support threshold (0.002).
     - `min_confidence`: Minimum confidence threshold (0.2).
     - `min_lift`: Minimum lift threshold (3).
     - `min_length` and `max_length`: Constraints for the number of items in an itemset (2).

4. **Visualization**:
   - Results are displayed in a structured format, highlighting pairs of movies with their corresponding support values.
   - The top 15 movie pairs with the highest support are showcased.

---

## Steps to Run the System

1. **Clone the Repository**:
   Download or clone the repository to your local machine.

2. **Prepare the Dataset**:
   Ensure you have an Excel file named `NetfilxMovies.xlsx` in the same directory as the script. The dataset should:
   - Contain rows representing user transactions.
   - Have columns for movies watched by each user.

3. **Install Dependencies**:
   - Install the required Python libraries using:
     ```bash
     pip install apyori
     ```

4. **Run the Script**:
   - Navigate to the project directory in your terminal or IDE.
   - Execute the script with the command:
     ```bash
     python netflix_movie_recommendation_ml.py
     ```

5. **View Results**:
   - The script outputs the raw results and a clean, tabular representation of frequently watched movie pairs.

---

## Example Output

```plaintext
Movie 1                Movie 2                Support
-----------------------------------------------------
Inception              Interstellar           0.005
The Dark Knight        Memento                0.004
Shutter Island         Fight Club             0.003
Avatar                 The Matrix             0.003
The Prestige           Tenet                  0.002
...
```

