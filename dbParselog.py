#!/usr/bin/env python3
# Creates reports based off the records store in a database.
import psycopg2

DBNAME = "news"


# Runs queries on the postgresql database.
def query_runner(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def main():

    most_popular_articles = \
            "select title as article, count(*) as views \
            from log join articles \
            on log.path like concat('%',articles.slug) \
            group by title \
            order by views \
            desc \
            limit 3;"
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
    one_percent_errors = \
            "select date, cast(error_percentage as int) from \
            (select date,(cast(errors as float) / cast(total_requests as float) * 100) as error_percentage \
            from (select date,total_requests,errors \
            from (select dates.date,count(*) as errors \
            from log join dates \
            on cast(time as date) = dates.date \
            where status != '200 OK' \
            group by dates.date,status order by date) \
            as errors join (select cast(time as date),count(*) \
            as total_requests from log group by cast(time as date)) as requests on errors.date = requests.time) as subq) \
            as error_percentages where error_percentage > 1;"

    print(query_runner(most_popular_articles))
    print(query_runner(most_popular_authors))
    print(query_runner(one_percent_errors))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nExited by user!')
