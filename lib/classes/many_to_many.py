class Article:
    all_articles = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._set_title(title)
        Article.all_append(self)

        # set_title locks the title after the first assignment
    def _set_title_(self, title):
        if hasattr(self, title):
            return
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = title

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be a Magazine instance.")
        self._magazine = value

    def __str__(self):
        return f"Title: {self.title}, Author:{self.author}, Magazine:{self.magazine}"    

        
class Author:
    def __init__(self, name):
        self._set_name(name)

# _set_name ensures validation and uses hasttr to keep the writable only once
    def _set_name_(self, name):
        if hasattr(self, '_name'):
            return 
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

# name property exposes the stored string,with no setter so it stays read-only
    @property 
    def name(self):
        return self._name

    # def __str__(self):
    #     return self.name
    pass

    def magazines(self):
        return list({article.magizine for article in self.articles()})
        pass
# add_article keeps validation centralized and immediately appends the new Article to Article.all_articles.
    def add_article(self, magazine, title):
        if not isinstance (magizine, Magazine):
            raise ValueError("magazine must be a Magazine instance.")
            return Article(self, magazine, title)
        pass
# topic_areas deduplicates categories and returns None if the authour hasn't published anything.
    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list({mag.category for mag in magazines})

    def __str__(self):
        return self.name
        pass

class Magazine:
    all_magazine = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise ValueError("Magazine name must be a atring between 2 and 16 characters.")
        self._name = value
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(valur, str) or len(value) == 0:
            raise ValueError("Magazine category be a non-empty string.")
        self._category = value 

    def articles(self):
        return [artucle for article in Article.all_articles if article.magazines is self]
        pass

    def contributors(self):
        return list({article.author for article in self.articles()})
        pass

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
        pass

    def contributing_authors(self):
        counts = {}
        for article in slef.articles():
            counts[article.author] = counts.get(article.author, 0) + 1
        prolific = [author for author, total in counts.items() if total > 2]
        return prolific or None

     # top_publisher scans all magazines using their articles() helper; it returns None when no articles exist.
    @classmethod
    def top_publisher(cls):
        if not Article.all_articles:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))

    def __str__(self):
        # return f"Magazine Name:{self.name} Category:{self.category}"
        return f"{self.name}"
        pass

author1 = Author("Christine")
author2 = Author("Ian")
# handled by the name property
print(author1.name)
# Handled by __str__
print(author1)
# Throws error due to AUthor name property lacking setter method
# author1.name = "Ian"

# author1.name

magazine1 = Magazine("ToDo", "Vehicle")
magazine2 = Magazine("Beauty", "Cosmetics")
# handled by the name property
# print(magazine1.name)
# handled by the category property
# print(magazine1.category)
# Handled by __str__
# print(magazine1)

magazine1.name = "Mech"
magazine1.category = "Motor"
print(magazine1)

# article1 = Article("Christine", "Mag1", "Article Title")
# # handled by the title property
# print(article1.title)
# # Handled by __str__
# print(article1)

# print(author1.articles)
article1 = Article(author1, magazine1, "First article")
# article1.magazine = magazine2
# article1.author = author1
print(article1)

# Test the author methods
author1.add_article(magazine1, "Bugatti")
print([article.title for article in author1.articles()])
print([article.name for article in author1.magazines()])
# print([article1.magazine for mag in author1.topic_areas()])

# Test the magazine methods
print([article.title for article in magazine1.articles()])
print([article.name for article in magazine1.contributors()])