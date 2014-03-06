from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from library.feeds import ArticlesFeed

from sitemaps import ArticlesSitemap, SiteSitemap

feeds = {
    'articles': ArticlesFeed,
}

sitemaps = {
    'articles': ArticlesSitemap,
    'pages': SiteSitemap(['index'])
}

urlpatterns = patterns('',
    #base
    url(r'^$', 'library.views.article_list', name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.STATIC_ROOT,}
	),
    (r'^comments/', include('django_comments.urls')),
    #backbone.js
    (r'^backbone/news/$', 'library.views.backbone_news'),
    (r'^backbone/articles/$', 'library.views.backbone_article_list'),
    #feeds
    #(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    #general
    url(r'^search/(?P<search_string>[-\w]+)$', 'anothernoob.views.search_view'),
    #league of legends
    url(r'leagueoflegends/', 'leagueoflegends.views.league_index'),
    #library
    url(r'^article/(?P<url_slug>[-\w]+)/(?P<article_id>\d+)$', 'library.views.article_single'),
    url(r'^preview/(?P<url_slug>[-\w]+)/(?P<article_id>\d+)$', 'library.views.preview_article'),
    #sitemaps
    (r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #social login
    url(r'', include('social_auth.urls')),
    url(r'account/check/profile', 'social.views.check_profile'),
    url(r'account/get/email', 'anothernoob.views.get_email'),
    url(r'logout/', 'anothernoob.views.logout_view'),
    #taggit autosuggest
    (r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    #upload redactor
    url(r"^ajax/photos/upload/$", "library.views.upload_photos", name="upload_photos"),
    url(r"^ajax/photos/recent/$", "library.views.recent_photos", name="recent_photos"),
)
