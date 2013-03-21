Metamod (Under Initial Development)
===================================

Metamod is a generic reuseable Django app to handle moderation strategy.
You can defined your own custom moderation behaviour and strategy (see strategy design pattern).

Use case 1: 
If you have a Boutique object created by boutique owner, you need to ensure that the boutique clothes meet certain quality check. 
If This boutique listing a new cloth, it will be disabled upon creation. Moderating cloth for the first time will visible the cloth.
When Homeowner change some attribute of the cloth, this cloth will still be enabled but also requires to be moderated for revision.
In such use case, you can write your backend in which moderation could either be approve, postpone, or reject.

Use case 2:
If you have a Q&A site, you need to allow the Question and answer to be visible immidiately for everyone, unless the content is inappropriate.
In this case, you can write your backend in which moderation of flagged objects, to ignore or disable.

Quick start
-----------

1. Add "metamod" to your INSTALLED\_APPS.
2. Run `python manage.py syncdb` or `python manage.py migrate metamod` if you used south migration
