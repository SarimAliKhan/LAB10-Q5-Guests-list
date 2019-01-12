print("Sarim Ali Khan")
print("Lab10")
print("Question 05")
parents_list = {"MsNoor&fam": {'name': 'Noor ul huda', 'family_mem': '5'},
"MrSarim&fam": {'name': 'Sarim', 'family_mem': '6'},
"MsNoor&fam": {'name': 'Noor ul huda', 'family_mem': '5'},
"MrLokash&fam": {'name': 'Lokash Fateh', 'family_mem': '3'},
"MrWasim&fam": {'name': 'Wasim', 'family_mem': '7'},
"MrFaisal&fam": {'name': 'Faisal Ali', 'family_mem': '2'},
"MsHania&fam": {'name': 'Hania amir', 'family_mem': '4'}}

my_list = {"MsHania&fam": {'name': 'Hania amir', 'family_mem': '4'},
"MrJahanzaib&fam": {'name': 'Jahanzaib wali', 'family_mem': '6'},
"MsNoor&fam": {'name': 'Noor ul huda', 'family_mem': '5'},
"MrFateh&fam": {'name': 'Fateh rehman', 'family_mem': '3'},
"MrHasan&fam": {'name': 'Hasan jawed', 'family_mem': '8'},
"MrSarim&fam": {'name': 'Sarim', 'family_mem': '6'},
"MrFarhan&fam": {'name': 'Farhan najmi', 'family_mem': '6'}}

def Guests(first,second):
    s = 0
    for k in first:
        if first.get(k) == second.get(k):
            s = s+1
            print("You and your parents both have his/her name in the list so that's why this"
                    "family can be invited :",k)

    for i in second:
        if first.get(i) != second.get(i):
            print("no,this guest was not invited either by you or your parents :",i)
    print('These are the',s,"guests which are invited in your sister's wedding")


print(Guests(parents_list,my_list))