import tweepy

auth = tweepy.OAuthHandler("ziV0Y1q6jjqv5pcRlPCEeTaJx", "Bj0M24yk4VKhzt7XcqGiVFVc4Urtsb6Rxr7Rdfn6kEV4NrqS5g")
auth.set_access_token("AAAAAAAAAAAAAAAAAAAAAJpPYwEAAAAAp%2BUiDtle8Qmn6zjfSyldAcDTZCU%3D5dnftB6GO4ILvl13yyYvLuwbsvBTbBSxQx3VgpmV7NOHNB6C1o", "1215640503938510848-pqWG7iuBj2VSPAXuu0sQCxD5PWmagf")

api = tweepy.API(auth)

api = api.home_timeline()
user = api.me()
print(user.username)