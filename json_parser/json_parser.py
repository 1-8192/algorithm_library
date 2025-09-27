"""
HTTP GET Request and JSON Parser Template code
"""

import requests
import os
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    """Data class for JSONPlaceholder post objects"""
    userId: int
    id: int
    title: str
    body: str
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Post':
        return cls(
            userId=data['userId'],
            id=data['id'],
            title=data['title'],
            body=data['body']
        )


@dataclass
class User:
    """Data class for JSONPlaceholder user objects"""
    id: int
    name: str
    username: str
    email: str
    phone: str
    website: str
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        return cls(
            id=data['id'],
            name=data['name'],
            username=data['username'],
            email=data['email'],
            phone=data['phone'],
            website=data['website']
        )


@dataclass
class Comment:
    """Data class for JSONPlaceholder comment objects"""
    postId: int
    id: int
    name: str
    email: str
    body: str
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Comment':
        return cls(
            postId=data['postId'],
            id=data['id'],
            name=data['name'],
            email=data['email'],
            body=data['body']
        )

class Json_Parser:
    """HTTP client for making GET requests and parsing JSON responses"""
    
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
        self.session = requests.Session()
        
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

    def get(self, endpoint, params = None):
        """
        Make HTTP GET request and return parsed JSON response
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            print(f"Making GET request to: {url}")
            if params:
                print(f"Parameters: {params}")
                
            response = self.session.get(url, params=params)
            response.raise_for_status()  # Raises HTTPError for bad responses
            
            print(f"Response status: {response.status_code}")
            print(f"Response headers: {dict(response.headers)}")
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"HTTP request failed: {e}")
            raise
        except json.JSONDecodeError as e:
            print(f"JSON parsing failed: {e}")
            raise
    
    def get_posts(self, user_id = None):
        """Get all posts or posts by specific user"""
        params = {'userId': user_id} if user_id else None
        data = self.get('/posts', params)
        return [Post.from_dict(item) for item in data]
    
    def get_post(self, post_id):
        """Get a specific post by ID"""
        data = self.get(f'/posts/{post_id}')
        return Post.from_dict(data)
    
    def get_users(self):
        """Get all users"""
        data = self.get('/users')
        return [User.from_dict(item) for item in data]
    
    def get_user(self, user_id):
        """Get a specific user by ID"""
        data = self.get(f'/users/{user_id}')
        return User.from_dict(data)
    
    def get_comments(self, post_id):
        """Get all comments or comments for a specific post"""
        if post_id:
            data = self.get(f'/posts/{post_id}/comments')
        else:
            data = self.get('/comments')
        return [Comment.from_dict(item) for item in data]

def run_tests():
    client = Json_Parser()

    print("\n1. Testing GET /posts")
    posts = client.get_posts()
    print(f"Retrieved {len(posts)} posts")
    if posts:
        first_post = posts[0]
        print(f"First post: ID={first_post.id}, Title='{first_post.title[:50]}...'")
        
    print("\n2. Testing GET /posts/1")
    post = client.get_post(1)
    print(f"Post 1: {post.title}")
    print(f"Body: {post.body[:100]}...")
        
    print("\n3. Testing GET /users")
    users = client.get_users()
    print(f"Retrieved {len(users)} users")
    if users:
        first_user = users[0]
        print(f"First user: {first_user.name} ({first_user.email})")
        
    print("\n4. Testing GET /users/1")
    user = client.get_user(1)
    print(f"User 1: {user.name} - {user.username}")
        
    print("\n5. Testing GET /posts?userId=1")
    user_posts = client.get_posts(user_id=1)
    print(f"User 1 has {len(user_posts)} posts")
        
    print("\n6. Testing GET /posts/1/comments")
    comments = client.get_comments(post_id=1)
    print(f"Post 1 has {len(comments)} comments")
    if comments:
        first_comment = comments[0]
        print(f"First comment by: {first_comment.email}")

if __name__ == "__main__":
    run_tests()
