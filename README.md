# Naive-Bayes-Classifier
Classification using Naive Bayes algorithm

Formula Used: 
p(A|B) = p(B|A) p(A)/p(B)

find= (21-30,medium,married)
{
  age category-> 21-30
  income-> medium
  status-> married
}

p(yes|find)= p(find|yes) * p(yes)/p(find)

p(no|find)=p(no|find) * p(no)/p(find)

if(p(yes|find)+p(no|find) !=1)
{
  perform Normalization
  
 }
 
 Normalization:
 
 p(yes|find) = p(yes|find) / p(yes|find)+p(no|find))
 
 p(no|find) = p(no|find) / p(yes|find) + p(no|find)
 
 p(yes|find)+p(no|find) == 1 
 
 then check which one is higher p(yes|find ) or p(no|find)
 
 then according to that value provide whether he can buy or not 
