class Article:
    all_articles = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

        # set_title locks the title after the first assignment
    def _set_title_(self, title):
        if hasattr(self, title):
            return
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.title = title

    @property
    def title(self):
        return self.title
    
    @property
    def author(self):
        return self.author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class.")
        self.author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value)
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
        self.name = name

    @property 
    def name(self):
        return self.name

    # def __str__(self):
    #     return self.name
    pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    def __str__(self):
        return f"{self.name} ({self.category})"
        m1 = Magazine("Vogue", "Fashion")
        print(m1)   

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

author1 = 
print(author1)