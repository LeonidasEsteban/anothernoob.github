from django.contrib.syndication.views import Feed
from library.models import Articles

class ArticlesFeed(Feed):
    title='Another Noob'
    link='http://anothernoob.com'
    description=''

    def items(self):
        return Articles.objects.all()

    def item_pubdate(self, item):
        return item.date

    def item_author_name(self, item):
        return '%s %s' % (item.author.first_name, item.author.last_name)