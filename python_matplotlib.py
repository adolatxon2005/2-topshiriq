import matplotlib.pyplot as plt 


a = [1, 2, 3, 4, 5] 
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21] 
plt.plot(a) 

# o doiralar uchun, r esa
# qizil uchun
plt.plot(b, "or") 

plt.plot(list(range(0, 22, 3))) 

# x o'qini nomlash
plt.xlabel('Day ->') 

# y o'qini nomlash
plt.ylabel('Temp ->') 

c = [4, 2, 6, 8, 3, 20, 13, 15] 
plt.plot(c, label = '4th Rep') 

# joriy o'qlar buyrug'ini olish
ax = plt.gca() 

# shaxs ustidan buyruq oling
# grafik tanasining chegara chizig'i 
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False) 

# diapazoni yoki chegaralarini belgilang
# belgilangan diapazongacha bo'lgan chap chegara chizig'i 
ax.spines['left'].set_bounds(-3, 40) 

# qaysi intervalni belgilang
# x o'qi belgilarni o'rnatadi
plt.xticks(list(range(-3, 10))) 

# y o'qi bo'lgan intervallarni o'rnating
# belgilarni o'rnating 
plt.yticks(list(range(-3, 20, 3))) 

# afsona qaysi rangni bildiradi
# nimani anglatadi 
ax.legend(['1st Rep', '2nd Rep', '3rd Rep', '4th Rep']) 

# annotate buyrug'i yozishga yordam beradi
# GRAFIKDA har qanday matn xy belgisini bildiradi
# grafikdagi pozitsiya 
plt.annotate('Temperature V / s Days', xy = (1.01, -2.15)) 

# Grafikga sarlavha beradi 
plt.title('All Features Discussed') 

plt.show() 

