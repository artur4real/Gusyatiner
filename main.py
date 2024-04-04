def load_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip().split(', ') for line in file]

def calculate_fill_percentage(sales_table, hall_capacity):
    return (len(sales_table) / hall_capacity) * 100 if hall_capacity else None

def find_most_popular_genre(films_table):
    genre_count = {}
    for film in films_table[1:]:
        genre_count[film[2]] = genre_count.get(film[2], 0) + 1
    return max(genre_count, key=genre_count.get) if genre_count else None

def main():
    halls_table, films_table, sales_table = map(load_table, ['hall.txt', 'film.txt', 'sale.txt'])

    hall_capacity = int(halls_table[1][1]) if len(halls_table) > 1 else None

    fill_percentage = calculate_fill_percentage(sales_table, hall_capacity)
    print("Процент наполнения зала по сеансам:", fill_percentage or "Ошибка: таблица залов не содержит данных.")

    most_popular_genre = find_most_popular_genre(films_table)
    print("Самый популярный жанр:", most_popular_genre or "Ошибка: таблица фильмов не содержит данных.")

if __name__ == "__main__":
    main()
