# **DRF API Social network**

## **Inroduction**

It is a social network API who supports all basic functions in any social network. Users can create new account, communities, make post and mush more which I will talk in chapter "Functionality details"

## **Installation**

* Go to backend `cd backend/`
* Establish a virtual environment(recommend use python3)  
  In python3 you can do that with with `python3 -m venv <environment name>`
* Activate the virtual environment `source <environment name>/bin/activate`
* Install all libraries from requirements.txt  
  You can do that with run `python3 -m pip install -r requirements.txt`
* Install all migrations `python3 manage.py makemigrations && python3 manage.py migrate`
* Do not forget to create a superuser account `python3 manage.py createsuperuser`  

## **Running**

For running you just need run `python3 manage.py runserver`

## **Functionality details**

Users can  
* Create communities    
* Create posts on his page and community page(If he is an admin or author)   
* Make like    
* Make comments    
* Subscribe or receive subscriptions from other accounts    
* Create chats with one or more accounts    
* Exchange messages in current chat    
* Can add or remove admin(If he admin of any community)    
* Change information about yourself    
    
Visit /docs/index.md to learn about API functions    

## **Other**

This API is good for scaling and it need a ability to send or receive an image in chat, publish image and the opportunity for a user set a photo.
