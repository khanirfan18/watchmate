from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app import models
from watchlist_app.api import serializers





class StreamPlatformTestCase(APITestCase):
     
     def setUp(self):
          self.user = User.objects.create(username='testuser', password='Testuserpass123')
          self.token = Token.objects.get(user__username = self.user)
          self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
     
     
     
          self.stream = models.StreamPlatform.objects.create(name="testflix",
                                                             about="testflix is a test stream platform",
                                                             website="https://testflix.com")
          self.watchlist = models.WatchList.objects.create(platform=self.stream,title="testmovie",description='test movie',active=True)
     
     
     def test_streamplatform_create(self):
          data={
               "name":"testflix",
               "about":"testflix is a test stream platform",
               "website":"https://testflix.com"
          }
          response = self.client.post(reverse('streamplatform-list'), data)
          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


     def test_streamplatform_list(self):
          response = self.client.get(reverse('streamplatform-list'))
          self.assertEqual(response.status_code, status.HTTP_200_OK)


     def test_streamplatform_indv(self):
          response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
          self.assertEqual(response.status_code, status.HTTP_200_OK)




class WatchListTestCase(APITestCase):
     def setUp(self):
          self.user = User.objects.create(username='testuser', password='Testuserpass123')
          self.token = Token.objects.get(user__username = self.user)
          self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
     
          self.stream = models.StreamPlatform.objects.create(name="testflix",
                                                             about="testflix is a test stream platform",
                                                             website="https://testflix.com")
          
          self.watchlist = models.WatchList.objects.create(
          title="testMovie",
          description="this is a test movie desc",
          active=True,
          platform=self.stream)                                                            
          
     
     def test_watchlist_create(self):
          data = {
               "title":"testMovie",
               "description":"this is a test movie desc",
               "active":True,
               "platform":self.stream
          }
          
          response = self.client.post(reverse('movies-list'), data)
          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

          
     def test_watchlist_list(self):
          response = self.client.get(reverse('movies-list'))
          self.assertEqual(response.status_code, status.HTTP_200_OK)

     def test_watchlist_indv(self):
          response = self.client.get(reverse('movie-detail', args=(self.watchlist.id,)))
          self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReviewTestCase(APITestCase):
     
     def setUp(self):
               self.user = User.objects.create(username='testuser', password='Testuserpass123')
               self.token = Token.objects.get(user__username = self.user)
               self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
          
          
          
               self.stream = models.StreamPlatform.objects.create(name="testflix",
                                                                 about="testflix is a test stream platform",
                                                                 website="https://testflix.com")
               self.watchlist = models.WatchList.objects.create(platform=self.stream,title="testmovie",description='test movie',active=True)
               
               
               
               self.watchlist2 = models.WatchList.objects.create(platform=self.stream,title="testmovie",description='test movie',active=True)

               
               self.review = models.Review.objects.create(review_user=self.user,rating=5,description="Nice film",
                                                            watchlist=self.watchlist,active=True)
     
     def test_review_create(self):
               data = {
                    "review_user":self.user,
                    "rating":5,
                    "description":"Nice film",
                    "watchlist":self.watchlist,
                    "active":True
               }
          
               response = self.client.post(reverse('review-create',args=(self.watchlist2.id,)),data)
               self.assertEqual(response.status_code, status.HTTP_201_CREATED)
               
               #extra testcase
               self.assertEqual(models.Review.objects.count(), 2)
               # self.assertEqual(models.Review.objects.get().rating, 5)
               
               
               
               #this test if a are allowed to create 2 review om same content
               response = self.client.post(reverse('review-create',args=(self.watchlist2.id,)),data)
               self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
          
     
     def test_review_create_unauth(self):
               data = {
                    "review_user":self.user,
                    "rating":5,
                    "description":"Nice film",
                    "watchlist":self.watchlist2,
                    "active":True
               }
               
               response = self.client.force_authenticate(user=None, token=None)
               response = self.client.post(reverse('review-create',args=(self.watchlist2.id,)),data)
               self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

     def test_review_update(self):
               data = {
                    "review_user":self.user,
                    "rating":4,
                    "description":"Nice film - updated",
                    "watchlist":self.watchlist,
                    "active":True
               }
               
               response = self.client.put(reverse('review-detail',args=(self.review.id,)),data)
               self.assertEqual(response.status_code, status.HTTP_200_OK)
               
     def test_review_list(self):
               response = self.client.get(reverse('all-reviews', args=(self.watchlist.id,)))
               self.assertEqual(response.status_code, status.HTTP_200_OK)
               
     def test_review_indv(self):
                    response = self.client.get(reverse('review-detail', args=(self.review.id,)))
                    self.assertEqual(response.status_code, status.HTTP_200_OK)
                    
     def test_review_delete(self):
          response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
          self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
          
     def test_review_user(self):
          response = self.client.get('/watch/reviews/?username' + self.user.username)
          self.assertEqual(response.status_code, status.HTTP_200_OK)
