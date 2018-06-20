#!/usr/bin/env python3
#Creates reports based off the records store in a database.
import psycopg2

DBNAME = "news"

def query_runner(query):
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def main():

     #1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
    most_popular_articles = \
            "select title as article, count(*) as views \
            from log join articles \
            on log.path like concat('%',articles.slug) \
            group by title \
            order by views \
            desc limit 3;"
    #2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
    most_popular_authors = \
            "select name,sum(views) as total_views \
            from \
                (select title as article,author, count(*) as views \
                from log join articles \
                on log.path like concat('%',articles.slug) \
                group by title,author) \
                as author_views \
            join authors \
            on author = authors.id \
            group by name \
            order by total_views \
            desc;"
    #3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)
    one_percent_errors = ""

    print(query_runner(most_popular_articles))
    print(query_runner(most_popular_authors))
    #print(query_runner(one_percent_errors))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nExited by user!')
