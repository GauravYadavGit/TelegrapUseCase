import csv
from collections import Counter


def process_hitlog(hitlog_file):
    # Read the hitlog CSV file and process the data
    articles_counter = Counter()

    with open(hitlog_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            page_url = row['page_url']
            if page_url.startswith('/articles/'):
                articles_counter[page_url] += 1

    return articles_counter


def find_top_articles(articles_counter, n):
    # Find the top n articles based on their occurrence
    top_articles = articles_counter.most_common(n)
    return top_articles


def write_to_csv(output_file, top_articles):
    # Write the top articles to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['page_name', 'page_url', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article, count in top_articles:
            writer.writerow({'page_name': 'Article', 'page_url': article, 'total': count})


if __name__ == "__main__":
    hitlog_file = r'C:\\Users\\Gaurav\\OneDrive\\Documents\\input.csv'
    output_file = 'top_articles.csv'
    num_top_articles = 3

    # Process the hitlog data and find the top articles
    articles_counter = process_hitlog(hitlog_file)
    top_articles = find_top_articles(articles_counter, num_top_articles)

    # Write the top articles to a CSV file
    write_to_csv(output_file, top_articles)
