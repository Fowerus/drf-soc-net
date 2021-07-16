# **Django-Rest-Framework Social network**

## **Inroduction**

It is a social network API who supports all basic functions in any social network. Users can create new account, communities, make post and mush more which I will talk in chapter "Functionality details"

## **Installation**

* Establish a virtual environment(recommend use python3)  
  In python3 you can do that with with `python3 -m venv <environment name>`
* Install all libraries from requirements.txt  
  You can do that with run `python3 -m pip install -r requirements.txt`

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

## **Other**

This API is good for scaling and it need a ability to send or receive an image in chat, publish image and the opportunity for a user set a photo.