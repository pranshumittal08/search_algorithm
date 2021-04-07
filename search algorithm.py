import numpy as np
import collections
import time

data = ["Guvi Geek Networks Private Limited", "Maximl Labs", "Pur Energy Private Limited", "Agnikul Cosmos", "The ePlane Company", 
				 "PYTORQ Solutions Private Limited", "Bigphi Technologies", "Ather Energy Private Limited", "Rekindle Automations Private Limited", 
				 "Aerostrovilos Energy Private Limited", "Impensus Electronics", "Doodhbhandaar", "Swapeco", "Statlogic India Private Limited",
				 "YNOS Venture Engine"]

#Tokenizing the company names
company_names = [name.split(" ") for name in data]

vocab = list(set([word for name in company_names  for word in name]))

def min_edit_distance(vocab, query):
	'''
	Input: 
		query: a string we are starting with
		vocab: list of words containing the strings we want to end with
	Output:
		med_word: word that is at minimum distance from the query word i.e. most similar to the query word 
	'''
	
	all_distances = []
	query = query.lower()
	ins_cost = 1 #cost of inserting a character from the target word i.e. word in vocab
	del_cost = 1 #Cost of deleting a character from the source word i.e. word in query
	rep_cost = 2 #Cost of swapping the characters from source and target word
	#computing the min-edit-distance for each word in the vocab
	for target_word in vocab:
		n = len(query) #Length of the query word
		m = len(target_word) #Length of the target word
		target_word = target_word.lower()
		#Creating a matrix/array of size (n+1, m+1)
		distance = np.zeros((n+1,m+1), dtype = "int")
		"""The below two lines are for updating the distance matrix with cost of insertion if we were to create the target word given NULL and 
		with the cost of deletion if we were to obtain NULL given the source word"""
		distance[0,:] = range(m+1) #Updating the distance matrix with cost of insertion  
		distance[:,0] = range(n+1) #Updating the distance matrix with cost of deletion 
		#Code to fill remaining of the distance matrix
		for i in range(1,n+1):
			for j in range(1, m+1):
				if query[i-1] != target_word.lower()[j-1]:
					rep_cost = 2
				else:
					rep_cost = 0
				distance[i][j] = min(distance[i-1,j-1] + rep_cost, distance[i-1,j] + del_cost, distance[i,j-1] + ins_cost)
		all_distances.append(distance[-1,-1])
		med_index = all_distances.index(min(all_distances)) #index of the word with min distance
	med_word = vocab[med_index] #most similar word
	
	return med_word

#Function to find the best search result
def best_match(data, prob_tokens):
	"""
	Input:
		data: List of all the company names in the dataset
		prob_tokens: List containing the tokens with minimum distance from the query words
	Output:
		best_match: Name of the company with that closely matches the search query
	"""

	count = collections.defaultdict()
	for company in data: #Looping over each company
		count[company] = 0
		for token in prob_tokens:
			if token in company:
				count[company] += 1

	best_match = sorted(count.items(), key = lambda x: x[1], reverse=True)[0][0]
	return best_match	


query = input("Search company: ").split(" ")
start = time.time()
prob_tokens = [min_edit_distance(vocab, word) for word in query] #List of most probable tokens
print(f"Top Result: {best_match(data, prob_tokens)}") #Obtaining the best search result
print(f"Search Time: {time.time() - start:.4f} secs")
