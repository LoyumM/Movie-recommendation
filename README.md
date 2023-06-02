# Movie-recommendation
The data is converted into a count vectorizer matrix after which by using cosine similarity, similar movies are generated

data source : [link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The web app is deployed at https://loyumm-movie-recommendation-streamlit-app-5j0ywf.streamlit.app/


## To run it locally:
The app is deployed on streamlit cloud and will be deployed using other platforms later. However, it is also available for offline run. To do so, open terminal and do the followig steps:

Clone the repo
`git clone 'https://github.com/LoyumM/salary-prediction.git'`

Create a virtual environment
`conda create --p venv python=3.8 -y`

Activate environment
`conda activate venv/`

Install the required modules
`pip install -r requirements.txt`

Run the application
`streamlit run streamlit_app.py`