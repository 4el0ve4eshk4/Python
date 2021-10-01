mashin=['tesla', 'mazda', 'suzuki', 'lexus', 'volkswagen'];
#mashin.remove("suzuki");
print(mashin);
item="mazda";
mashin.remove(item);
print(mashin);
massage=f"Такие машины у нас остались: {mashin[0].title()}, {mashin[1].title()}, {mashin[2].title()}, {mashin[3].title()}"
print(massage);
mashin.sort();
print(mashin);
mashin.sort(reverse=1);
print(mashin);
mashin.reverse();
print(mashin);
t=len(mashin);
print(t);
