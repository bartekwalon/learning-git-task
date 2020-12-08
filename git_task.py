shopping_list = {
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "piekarnia": ['chleb','bulki','pączek']
}
sum=sum(map(len, shopping_list.values()))
for key, value in shopping_list.items():
    print(
        "Idę do " +str.capitalize(key) +" kupię tu następujące rzeczy: " +str(value)+"."
        )
print("W sumie kupuję " +str(sum)+ " produktów.")

print("hello")