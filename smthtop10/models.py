from django.db import models

# Create your models here.
class Post():
    def __init__(self,author="unknow",content="unknow",signature="unknown",reference="unknown",attached=False):
        self.author=author
        self.content=content
        self.attached=attached
        self.signature=signature
        self.reference=reference
    def __str__(self):
        return "%s:\n%s" % (self.author.encode("utf8"),self.content.encode("utf8"))
        
class Feed():
    def __init__(self,title="unknown"):
        self.list=list()
        self.title=title
        self.numOfPosts=0
    def append(self,post):
        self.list.append(post)
        self.numOfPosts=self.numOfPosts+1
    def __str__(self):
        return self.title.encode("utf8")