# password generator 
# you can add or remove any letter in x1 example (x X , \ @ # $ & * _ - 
x1=["a","b","c","d","e","1","2","3","4","5","6","7","8","9"]
# print('enter a value')
appendFile =open("password.txt","a")
# this for loops give you 8 digits password with the all possible values
# you can add or re move for to adjust how long the password is. by adding one for loop, you need to add to S3 too
for q in x1:	
	for w in x1:
		for f in x1:	
			for i in x1:
				for j in x1:
					for d in x1:
						for g in x1:
							for g8 in x1:
								s3=q+w+f+i+j+d+g+g8
								appendFile.write(str(s3))
								appendFile.write('\n')
									# print(s3)
appendFile.close()
