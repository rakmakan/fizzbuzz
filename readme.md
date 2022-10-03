# Task 2
In this work, I have created a sentiment classifier using the [transformer model](https://huggingface.co/mrm8488/t5-base-finetuned-imdb-sentiment) (T5) 
pretrained on the [IMDB dataset](https://huggingface.co/datasets/imdb). I am using the hugging face [inference API](https://huggingface.co/docs/api-inference/detailed_parameters) to 
request the pretrained model to return the sentiment on the input text. 


## Reason for using the model:
I have chose this model as this have the highest accuracy and f1-score among the other finetuned models.
The doumentation did not provide the loss and numbr of epoch they have used for training. I have tried other model such as
https://huggingface.co/aychang/roberta-base-imdb but results where not satisfactory.

|              | precision  |  recall   |  f1-score  | support |
|:------------:|:----------:|:---------:|:----------:|:-------:|
|   negative   |    0.95    |   0.95    |    0.95    |  12500  |
|   positive   |    0.95    |   0.95    |    0.95    |  12500  |
|  ----------  | ---------- | --------- | ---------- | ------- |
|   accuracy   |            |           |    0.95    |  25000  |
|  macro avg   |    0.95    |   0.95    |    0.95    |  25000  |
| weighted avg |    0.95    |   0.95    |    0.95    |  25000  |


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
   
## Requesting the docker to get a sentiment of a movie review
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
