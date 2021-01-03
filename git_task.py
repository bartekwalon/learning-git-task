shopping_list = {
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "piekarnia": ['chleb','bulki','pączek']
}
sum=sum(map(len, shopping_list.values()))
for key, value in shopping_list.items():
    print(
        f"Idę do {key.capitalize()} kupię tu następujące rzeczy: {value}."
        )
print(f"W sumie kupuję {sum} produktów.")

print("hello")