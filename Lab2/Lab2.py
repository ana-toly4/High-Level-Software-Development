with open('netflix_list.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def smart_split(line):
    result = []
    current_word = []
    in_quotes = False
    
    for char in line:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            result.append(''.join(current_word).strip())
            current_word = []
        else:
            current_word.append(char)
            
    result.append(''.join(current_word).strip())
    return result

dataset = [smart_split(line.strip()) for line in lines]

header = dataset[0]
data = dataset[1:]

idx_rating = header.index('rating')
idx_lang = header.index('language')
idx_type = header.index('type')
idx_endYear = header.index('endYear')
idx_cast = header.index('cast')
idx_isAdult = header.index('isAdult')
idx_numVotes = header.index('numVotes')
idx_episodes = header.index('episodes') 
idx_title = header.index('title')

def safe_float(val):
    try:
        return float(val)
    except ValueError:
        return 0.0

def safe_int(val):
    try:
        return int(float(val))
    except ValueError:
        return 0
high_rated_first_5 = [row[:5] for row in data if len(row) > idx_rating and safe_float(row[idx_rating]) > 7.5]
print(f"Знайдено записів з рейтингом > 7.5: {len(high_rated_first_5)}")

def filter_modern_english_shows(dataset_rows):
    for row in dataset_rows:
        if len(row) <= max(idx_lang, idx_type, idx_endYear):
            continue
            
        lang = row[idx_lang].strip().lower()
        show_type = row[idx_type].strip().lower()
        end_year = safe_int(row[idx_endYear])
            
        if lang == 'english' and show_type in ['movie', 'tvseries', 'series'] and end_year > 2015:
            yield row

modern_shows_gen = filter_modern_english_shows(data)

print("\n--- Генератор: Сучасні англомовні шоу (закінчилися після 2015) ---")
for _ in range(5):
    try:
        show = next(modern_shows_gen)
        print(f"- {show[idx_title]} (Рік завершення: {show[idx_endYear]})")
    except StopIteration:
        break

class CastIterator:
    def __init__(self, dataset_rows):
        self.data = dataset_rows
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            row = self.data[self.index]
            self.index += 1
            if len(row) > idx_cast:
                cast_str = row[idx_cast]
                clean_cast = cast_str.replace('[', '').replace(']', '').replace("'", "")
                if len(clean_cast) > 50:
                    return clean_cast
        raise StopIteration

print("\n--- Перші 10 записів акторського складу (>50 символів) ---")
cast_iter = CastIterator(data)
for i in range(10):
    try:
        # Прибрано обрізання, тепер виводиться повний рядок
        print(f"{i+1}. {next(cast_iter)}")
    except StopIteration:
        break
def calculate_dataset_stats(dataset_rows):
    adult_shows = sum(1 for row in dataset_rows if len(row) > idx_isAdult and row[idx_isAdult].strip() == '1')
    
    valid_ratings = [
        safe_float(row[idx_rating]) for row in dataset_rows 
        if len(row) > idx_numVotes and safe_int(row[idx_numVotes]) > 1000
    ]
    
    avg_rating = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 0
    return adult_shows, avg_rating

adult_count, average_rating_1000 = calculate_dataset_stats(data)
print(f"\n--- Статистика Датасету ---")
print(f"Кількість шоу для дорослих (isAdult == 1): {adult_count}")
print(f"Середній рейтинг шоу (>1000 голосів): {average_rating_1000:.2f}")

def episode_generator(dataset_rows):
    for row in dataset_rows:
        if len(row) <= max(idx_episodes, idx_rating, idx_title):
            continue
        episodes = safe_int(row[idx_episodes])
        rating = safe_float(row[idx_rating])
            
        if episodes > 10:
            yield row[idx_title], rating

top_long_shows = [
    title for title, rating in episode_generator(data) 
    if rating > average_rating_1000
]

print(f"\n--- Топ довгі шоу (>10 епізодів та рейтинг > {average_rating_1000:.2f}) ---")
print(f"Знайдено шоу: {len(top_long_shows)}")
for show in top_long_shows[:10]:
    print("-", show)
