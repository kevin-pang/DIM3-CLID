from django.contrib import admin
from auction.models import User, Product, Bid, Comment, Rating

admin.site.register(User);
admin.site.register(Product);
admin.site.register(Bid);
admin.site.register(Comment);
admin.site.register(Rating);