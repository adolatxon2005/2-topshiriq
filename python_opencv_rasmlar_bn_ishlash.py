# Developed by Ibrohimova Adolatxon
import  cv2  
# rasmni kulrang rang sifatida o‘qing  
img = cv2.imread(r 'Images\cat.jpeg‘ )  
# tasvir balandligi, kengligini oling  
(h, w) = img.shape[: 2 ]  
# tasvirning markazini hisoblang  
markaz = (w /  2 , h /  2 )    
burchak 90 =  90  
burchak 180 =  180  
burchak 270 =  270    
masshtab =  1,0    
# Markazda ushlab soat miliga teskari aylanishni bajaring  
#  90  daraja  
M = cv2.getRotationMatrix2D(markaz, burchak90, masshtab)  
rotated90 = cv2.warpAffine(img, M, (h, w))    
#  180  daraja  
M = cv2.getRotationMatrix2D(markaz, burchak 180, masshtab)  
rotated180 = cv2.warpAffine(img, M, (w, h))    
#  270  daraja  
M = cv2.getRotationMatrix2D(markaz, burchak 270, masshtab)  
rotated270 = cv2.warpAffine(img, M, (h, w))    
cv2.imshow ( 'Asl rasm' , img)  
cv2.waitKey( 0 ) # tugma bosilmaguncha kutadi  
cv2.destroyAllWindows() # tasvirni ko‘rsatadigan oynani yo‘q qiladi    
cv2.imshow( 'Rasm 90 gradusga aylantirildi' , aylantirildi90)  
cv2.waitKey( 0 ) # tugma bosilmaguncha kutadi  
cv2.destroyAllWindows() # tasvirni ko‘rsatadigan oynani yo‘q qiladi    
cv2.imshow( 'Tasvir 180 gradusga aylantirildi' , aylantirildi180)  
cv2.waitKey( 0 ) # tugma bosilmaguncha kutadi  
cv2.destroyAllWindows() # tasvirni ko‘rsatadigan oynani yo‘q qiladi    
cv2.imshow( 'Tasvir 270 gradusga aylantirildi' , aylantirildi270)  
cv2.waitKey( 0 ) # tugma bosilmaguncha kutadi  
cv2.destroyAllWindows() # tasvirni ko‘rsatadigan oynani yo‘q qiladi  
