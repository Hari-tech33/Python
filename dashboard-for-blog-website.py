blog_views = [150,800,2500,600,1200,450,3000]

trending_post = 0

for x in blog_views:
    if x > 1000:
        print("Trending")
        trending_post +=1
    elif x in range(500, 1000):
        print("Average")
    else:
        print("Low Traffic")

print("Total Number Views", sum(blog_views))

print("Trending Posts", trending_post)

        

