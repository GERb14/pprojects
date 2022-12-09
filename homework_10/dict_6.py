my_text = """Любіть Україну, як сонце любіть,

як вітер, і трави, і води...

В годину щасливу і в радості мить,

любіть у годину негоди.



Любіть Україну у сні й наяву,

вишневу свою Україну,

красу її, вічно живу і нову,

і мову її солов'їну.



Без неї — ніщо ми, як порох і дим,

розвіяний в полі вітрами...

Любіть Україну всім серцем своїм

і всіми своїми ділами."""
my_text1 = my_text.replace('.', ' ').replace(',', ' ').replace('—', ' ').split()
result = {i: my_text1.count(i) for i in my_text1}
print(result)
var = list(result.values())
for i, j in result.items():
    if j == max(var):
        print(" Word -", "'", i, "'", " appears the most times:", max(var))
