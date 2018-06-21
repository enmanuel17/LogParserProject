#!/usr/bin/env python3
# Creates reports based off the records store in a database.
import psycopg2

# Storas the database name to connect to
DBNAME = "news"


# Runs queries on the postgresql database.
def query_runner(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except Exception as e:
        print("Unable to connect to the database")
        exit(-1)


def main():

    # Stores 3 SQL queiries to answer the report questions.
    most_popular_articles = """
    select title as article, count(*) as views
    from log join articles
    on log.path like concat('%',articles.slug)
    group by title
    order by views
    desc
    limit 3;"""
    most_popular_authors = """
    select name,sum(views) as total_views
    from
        (select title as article,author, count(*) as views
        from log join articles
        on log.path like concat('%',articles.slug)
        group by title,author)
        as author_views
    join authors
    on author = authors.id
    group by name
    order by total_views
    desc;"""
    one_percent_errors = """
    select date, cast(error_percentage as int) from
    (select date,(cast(errors as float) / cast(total_requests as float) * 100)
    as error_percentage
    from (select date,total_requests,errors
    from (select dates.date,count(*) as errors
    from log join dates
    on cast(time as date) = dates.date
    where status != '200 OK'
    group by dates.date,status order by date)
    as errors join (select cast(time as date),count(*)
    as total_requests from log group by cast(time as date)) as requests
    on errors.date = requests.time) as subq)
    as error_percentages where error_percentage > 1;"""

    # prints  the response from each query in a nice format.
    result1 = query_runner(most_popular_articles)
    print("These are the most popular three articles of all time\n")
    for i in result1:
        title = i[0]
        views = str(i[1])
        print("Title \"" + title + "\" --- " + views + " views")
    print("\n")

    result2 = query_runner(most_popular_authors)
    print("These are the most popular article authors of all time\n")
    for i in result2:
        author = i[0]
        views = str(i[1])
        print("Author \"" + author + "\" --- " + views + " views")
    print("\n")

    result3 = query_runner(one_percent_errors)
    print("On the following date, more than 1% of requests lead to errors\n")
    for i in result3:
        date = str(i[0])
        percent = str(i[1])
        print(date + " --- "+percent + "% errors")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nExited by user!')
