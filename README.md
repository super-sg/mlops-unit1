# MLOps Unit 1 Project

## Objective

This project demonstrates basic MLOps practices including version control, data preprocessing, model training, and project structuring.

## Dataset Used

The dataset used is "anime_characters.csv", which contains information about anime characters such as name, favorites, and other attributes.

## Project Structure

* data/: Contains dataset files
* src/: Contains Python scripts
* models/: Contains trained ML models

## Steps to Run the Project

1. Install dependencies:
   pip install -r requirements.txt

2. Run preprocessing:
   python src/preprocess.py

3. Train the model:
   python src/train_model.py

## Output

* Processed dataset
* Trained ML model (linear_model.pkl)

## Environment Setup (Reproducibility)

Follow these steps to recreate the project environment:

1. Clone the repository:
   git clone https://github.com/super-sg/mlops-unit1.git

2. Navigate into the project folder:
   cd mlops-unit1

3. (Optional but recommended) Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:

   * Windows: venv\Scripts\activate
   * Mac/Linux: source venv/bin/activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the project:
   python src/preprocess.py
   python src/train_model.py
