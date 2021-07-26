### **User API** - **`/users/`** 

* `auth/registration/` - link to register a new user  
  **POST**  
  ```json  
  {  
    //input
    "username":"user1",   
    "email":"user1@gmail.com",    
    "last_name":"user1",  
    "first_name":"user1",
    "password":"user1user1"  
  }  
  ```  
  *`Response 201`*  
  ```json  
  {  
    //output
    "username":"user1",   
    "email":"user1@gmail.com",    
    "last_name":"user1",  
    "first_name":"user1"  
  }  
  ```  
  
* `auth/login/` - login link for user  
  **POST**  
  ```json  
  {  
    //input
    "email":"user1@gmail.com",    
    "password":"user1user1"  
  }  
  ```   
  *`Response 200`*  
  ```json  
  {  
    //output
    "username":"user1",  
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywidXNlcm5hbWUiOiJ1c2VyMSIsImVtYWlsIjoidXNlcjFAZ21haWwuY29tIn0.gknDOogiYJBYvfwTHGbfIgvu5NG0figGJwmi3SOcq30"
  }  
  ```  
  
* `auth/retrieve-update-destroy/<int:id_user>/` - link to retrieve, update, destroy a user  
  `auth/retrieve-update-destroy/3/`   
  **GET** - retrieve   
  *`Response 200`*  
  ```json  
  { 
    //output
    "id":3,  
    "username":"user1",  
    "email":"user1@gmail.com",  
    "last_name":"user1",  
    "first_name":"user1"  
  }  
  ```  
  **PATCH** - update  
  ```json  
  {  
    //input (You can skip any field)  
    "username":"user2",  
    "email":"user2@gmail.com",  
    "last_name":"user2",   
    "first_name":"user2"   
  }  
  ```    
  *`Response 200`*  
  ```json  
  {  
    //output
    "id":3,  
    "username":"user2",  
    "email":"user2@gmail.com",  
    "last_name":"user2",   
    "first_name":"user2"  
  }  
  ```  
  **DELETE** - delete    
  *`Response 204`*  
  ```json   
  {   
    //output   
  }   
  ```   
   
* `auth/change-password/<int:user_id>/` - link to change user password  
  `auth/change-password/3/`
  **PATCH**    
  ```json    
  {
    //input
    "password":"user2user2"  
  }  
  ```    
  *`Response 200`*   
  ```json
  {
    //output
  }   
  ```   
   
* `auth/VerifyJWTUser/` - link to verify JWT token  
  **POST**    
  ```json  
  {  
    //input
    "username":"user2",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywidXNlcm5hbWUiOiJ1c2VyMSIsImVtYWlsIjoidXNlcjFAZ21haWwuY29tIn0.gknDOogiYJBYvfwTHGbfIgvu5NG0figGJwmi3SOcq30"
  }  
  ```    
  *`Response 200`*  
  ```json  
  {  
    //output   
    "id": 3,  
    "email": "user2@gmail.com",  
    "username": "user2",  
    "last_name": "user2",   
    "first_name": "user2"  
  }  
  ```  

* `user-list/` - link to the list of users  
  **GET**    
  ```json  
  [  
    //output
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

* `user-followers/create-delete/` - link to subscribe or unsubscribe the user
  **POST**
  ```json
  {
    //input
    "user":3,
    "user_follower":1
  }
  ```   
  If subscription already exists   
  *`Response 200`*   
  ```json
  {
    //output
    "user":3,
    "user_follower":1
  }
  ```  
  If not    
  *`Response 201`*   
  ```json
  {
    //output
    "user":3,
    "user_follower":1
  }
  ```   
   
* `user-followers/all-user/<int:user_id>/` - link to the list of user subscribers
  `user-followers/all-user/3/`  
  **GET**  
  *`Response 200`*   
  ```json   
  [
    //output
    {
      "user": 3,
      "user_follower": 1
    }
  ]   
  ```      
   
* `user-followers/all-user-follower/<int:id_follower>/` - link to all user subscriptions
  `user-followers/all-user-follower/1/`   
  **GET**   
  *`Response 200`*   
  ```json   
  [   
    //output
    {
      "user": 3,
      "user_follower": 1
    }
  ]   
  ```  

* `posts/` - link to the list of all posts of all users
  **POST**
  ```json
  {
    //input
    "text":"Hello first",
    "author":1
  }
  ```
  *`Response 201`*
  ```json
  {
    //output
    "id": 1,
    "text": "Hello first",
    "author": 1
  }
  ```
  **GET**
  *`Response 200`*   
  ```json
  [
    //output
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

* `posts/posts-of-user/<int:user_id>/` - link to the list of user posts
  `posts/posts-of-user/3/`
  **GET**   
  *`Response 200`*
  ```json   
  [
    //output
    {
      "id": 2,
      "text": "Hello second",
      "author": 3
    }
  ]
  ```   

* `posts/retrieve-update-destroy/<int:id>/` - link to retrieve, update, destroy user's post
  `posts/retrieve-update-destroy/1/`
  **GET**
  *`Response 200`*
  ```json
  {
    //output
    "id": 1,
    "text": "Hello first",
    "author": 1
  }
  ```   
  **PATCH**   
  *`Response 200`*   
  ```json
  {
    //input
    "text":"Hello fourth",
    "author":3
  }
  ```   
  *`Response 200`*   
  ```json
  {
    "id": 1,
    "text": "Hello fourth",
    "author": 3
  }
  ```   
  **DELETE**
  *`Response 204`*
  ```json
  {
    //output
  }
  ```   

* `posts/like/create-delete/<int:post_id>/` - link to create a like or remove like from user's post
  `posts/like/create-delete/2/`
  **POST**
  ```json
  {
    //input
    "id":1
  }
  ```
  If like already exists   
  *`Response 200`*
  ```json
  {
    //output
  }
  ```
  If not   
  *`Response 201`*
  ```json
  {
    //output
  }
  ```


* `posts/like/all/<int:post_id>/` - link to the list of like of user's post   
  `posts/like/all/2/`
  **GET**
  *`Response 200`*
  ```json
  [
    //output
    {
      "id": 3,
      "post": 2,
      "user": 1
    }
  ]
  ```

* `posts/comment/create/<int:post_id>/` - link to the create comment for a user's post
  `posts/comment/create/2/`
  **POST**
  ```json
  {
    //input
    "user_id":3,
    "comment":"Good job"
  }
  ``` 
  *`Response 201`*
  ```json
  {
    //output
    "id": 1,
    "post": 2,
    "user": 3,
    "comment": "Good job"
  }   
  ``` 
  
* `posts/comment/all/<int:post_id>/` - link to the list of all comments of the user's post 
  `posts/comment/all/2/`
  **GET**
  *`Response 200`*
  ```json
  [
    //output
    {
      "id": 1,
      "post": 2,
      "user": 3,
      "comment": "Good job"
    }
  ]
  ```
  
* `posts/comment/delete/<int:comment_id>/` - link to the remove comment for a user's post
    `posts/comment/delete/1/`
    **DELETE**
    *`Response 200`*
    ```json
    {
      //output
    }
    ```
