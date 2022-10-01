# Task 2
In this work, I have created a sentiment classifier using the [transformer model](https://huggingface.co/aychang/roberta-base-imdb) (RoBERTa) 
pretrained on the [IMDB dataset](https://huggingface.co/datasets/imdb). I am using the hugging face [inference API](https://huggingface.co/docs/api-inference/detailed_parameters) to 
request the pretrained model to return the sentiment on the input text. 



# Follow the step to run the code:
1. Clone the repository using the Github link
2. Run the below command to build the docker image:
   
    <code>
   sudo docker build -t rakshitmakan/lemai . 
       </code>
   
3. Run the docker

    <code>
   sudo docker run -p 5000:8000 rakshitmakan/lemai 
       </code>
   
## Requesting the docker to get a sentiment of a movie revie
### method 1: Using the curl form the terminal 
  <code>
    curl --location --request POST 'http://0.0.0.0:4000/predict' \
    --form 'text="The Movie is great"'
    </code>

### method 2: Using the jupyter notebook
* You can also hit the endpoint running in docker using [Test Request.ipynb](https://github.com/rakmakan/fizzbuzz/blob/master/Test%20Request.ipynb)
* 

# Task 3:

Find explorator data analysis for task 3 in [AG News - Exploratory Data Analysis.ipynb](https://github.com/rakmakan/fizzbuzz/blob/master/AG%20News%20-%20Exploratory%20Data%20Analysis.ipynb)
