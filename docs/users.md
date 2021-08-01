# **User API** - **`/users/`**   
      
    
## **Authentication and similar functions**
    
### **Registration**    
* **POST** `auth/registration/`    
  INPUT    
  ```json  
  {  
    "username":"user1",   
    "email":"user1@gmail.com",    
    "last_name":"user1",  
    "first_name":"user1",
    "password":"user1user1"  
  }  
  ```    
  OUTPUT    
  *`Response 201`*    
  ```json  
  {  
    "username":"user1",   
    "email":"user1@gmail.com",    
    "last_name":"user1",  
    "first_name":"user1"  
  }  
  ```    
    
### **Login**    
* **POST** `auth/login/`    
  INPUT    
  ```json   
  {  
    "email":"user1@gmail.com",    
    "password":"user1user1"  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {  
    "username":"user1",  
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywidXNlcm5hbWUiOiJ1c2VyMSIsImVtYWlsIjoidXNlcjFAZ21haWwuY29tIn0.gknDOogiYJBYvfwTHGbfIgvu5NG0figGJwmi3SOcq30"
  }  
  ```  
    
### **Retrieve, Update, Destroy a user**    
* **GET** `auth/retrieve-update-destroy/<int:id_user>/`    
  OUTPUT    
  *`Response 200`*  
  ```json    
  { 
    "id":3,  
    "username":"user1",  
    "email":"user1@gmail.com",  
    "last_name":"user1",  
    "first_name":"user1"  
  }  
  ```  
* **PATCH** `auth/retrieve-update-destroy/<int:id_user>/`                         
  You can skip almost all fields except one          
  INPUT    
  ```json  
  {  
    "username":"user2",  
    "email":"user2@gmail.com",  
    "last_name":"user2",   
    "first_name":"user2"   
  }  
  ```    
  OUTPUT    
  *`Response 200`*  
  ```json  
  {  
    "id":3,  
    "username":"user2",  
    "email":"user2@gmail.com",  
    "last_name":"user2",   
    "first_name":"user2"  
  }  
  ```  
* **DELETE** `auth/retrieve-update-destroy/<int:id_user>/`    
  OUTPUT    
  *`Response 204`*   

### **Changing password**    
* **PATCH** `auth/change-password/<int:user_id>/`    
  INPUT    
  ```json    
  {
    "password":"user2user2"  
  }      
  ```   
  OUTPUT    
  *`Response 200`*    
    
### **Verify JWT token**    
* **POST** `auth/VerifyJWTUser/`    
  INPUT     
  ```json  
  {  
    "username":"user2",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywidXNlcm5hbWUiOiJ1c2VyMSIsImVtYWlsIjoidXNlcjFAZ21haWwuY29tIn0.gknDOogiYJBYvfwTHGbfIgvu5NG0figGJwmi3SOcq30"
  }  
  ```   
  OUTPUT   
  *`Response 200`*  
  ```json   
  {    
    "id": 3,  
    "email": "user2@gmail.com",  
    "username": "user2",  
    "last_name": "user2",   
    "first_name": "user2"  
  }  
  ```   
    
    
## **Subscriptions and similar functions**

### **List of all user**    
* **GET**  `user-list/`    
  OUTPUT    
  *`Response 200`*     
  ```json  
  [  
    {  
        "id": 3,  
        "username": "user2",  
        "email": "user2@gmail.com",  
        "last_name": "user2",  
        "first_name": "user2"  
    },      
    {  
        "id": 1,  
        "username": "a",  
        "email": "a@gmail.com",  
        "last_name": "a",  
        "first_name": "a"  
    }  
  ]  
  ```  
    
### **Subscribe or unsubscribe**      
* **POST** `user-followers/create-delete/`    
  INPUT    
  ```json
  {
    "user":3,
    "user_follower":1
  }
  ```  
  OUTPUT     
  If subscription already exists   
  *`Response 200`*   
  ```json
  {
    "user":3,
    "user_follower":1
  }
  ```  
  If not    
  *`Response 201`*   
  ```json
  {
    "user":3,
    "user_follower":1
  }
  ```     
    
### **List of all user subscribers**    
* **GET** `user-followers/all-user/<int:user_id>/`     
  OUTPUT    
  *`Response 200`*    
  ```json   
  [
    {
      "user": 3,
      "user_follower": 1
    }
  ]   
  ```    

### **List of all user subscriptions**    
* **GET** `user-followers/all-user-follower/<int:id_follower>/`    
  OUTPUT    
  *`Response 200`*   
  ```json   
  [   
    {
      "user": 3,
      "user_follower": 1
    }
  ]   
  ```  
    
    
## **Posts and similar functions**   
    
### **Create and get Posts**   
* **POST** `posts/`    
  INPUT    
  ```json
  {
    "text":"Hello first",
    "author":1
  } 
  ```    
  OUTPUT    
  *`Response 201`*   
  ```json
  {
    "id": 1,
    "text": "Hello first",
    "author": 1
  }
  ```    
* **GET** `posts/`    
  OUTPUT    
  *`Response 200`*    
  ```json    
  [
    {
      "id": 2,
      "text": "Hello second",
      "author": 3
    },
    {
      "id": 1,
      "text": "Hello first",
      "author": 1
    }
  ]
  ```   

### **User posts**    
* **GET** `posts/posts-of-user/<int:user_id>/`     
  OUTPUT     
  *`Response 200`*    
  ```json   
  [
    {
      "id": 2,
      "text": "Hello second",
      "author": 3
    }
  ]
  ```   
    
### **Retrieve, Update, Destroy a post**    
* **GET** `posts/retrieve-update-destroy/<int:id>/`     
  OUTPUT     
  *`Response 200`*   
  ```json
  {
    "id": 1,
    "text": "Hello first",
    "author": 1
  }
  ```   
* **PATCH** `posts/retrieve-update-destroy/<int:id>/`  
  You can skip almost all fields except one   
  INPUT    
  ```json
  {
    "text":"Hello fourth",
    "author":3
  }
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json
  {
    "id": 1,
    "text": "Hello fourth",
    "author": 3
  }
  ```   
* **DELETE** `posts/retrieve-update-destroy/<int:id>/`   
  OUTPUT    
  *`Response 204`*   
    
    
## **Likes and similar functions**   

### **Create-delete like**    
* **POST** `posts/like/create-delete/<int:post_id>/`    
  INPUT      
  ```json
  {
    "id":1
  }
  ```  
  OUTPUT    
  If like already exists   
  *`Response 200`*   

  If not   
  *`Response 201`*  
    
### **List of like of user's post**    
* **GET** `posts/like/all/<int:post_id>/`    
  OUTPUT    
  *`Response 200`*   
  ```json
  [
    {
      "id": 3,
      "post": 2,
      "user": 1
    }
  ]
  ```    
   
    
## **Comments and similar functions**    
    
### **Create comments**   
* **POST** `posts/comment/create/<int:post_id>/`     
  INPUT   
  ```json
  {
    "user_id":3,
    "comment":"Good job"
  }
  ```  
  OUTPUT    
  *`Response 201`*   
  ```json
  {
    "id": 1,
    "post": 2,
    "user": 3,
    "comment": "Good job"
  }   
  ```  

### **List of all comments of user's post**     
* **GET** `posts/comment/all/<int:post_id>/`    
  OUTPUT    
  *`Response 200`*   
  ```json
  [
    {
      "id": 1,
      "post": 2,
      "user": 3,
      "comment": "Good job"
    }
  ]
  ```    

### **Remove comment for user's post**    
* **DELETE** `posts/comment/delete/<int:comment_id>/`    
  OUTPUT    
  *`Response 200`*    
